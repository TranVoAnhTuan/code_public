-- A. Tạo database và các bảng chính
IF DB_ID('ALL_ORDER') IS NOT NULL
BEGIN
    ALTER DATABASE ALL_ORDER SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE ALL_ORDER;
END
GO
CREATE DATABASE ALL_ORDER;
GO
USE ALL_ORDER;
GO

-- Dim_Date
CREATE TABLE Dim_Date (
    Order_Date DATE NOT NULL PRIMARY KEY,
    Day INT NULL,
    Month INT NULL,
    Quarter INT NULL,
    Year INT NULL
);
GO

-- Dim_Product
CREATE TABLE Dim_Product (
    Product_ID NVARCHAR(50) NOT NULL PRIMARY KEY,
    Product_Name NVARCHAR(200) NULL,
    Sub_Category NVARCHAR(155) NULL,
    Category NVARCHAR(155) NULL
);
GO

-- Dim_Customer
CREATE TABLE Dim_Customer (
    Customer_ID NVARCHAR(50) NOT NULL PRIMARY KEY,
    Customer_Name NVARCHAR(100) NULL,
    Segment NVARCHAR(100) NULL
);
GO

-- Dim_Region
CREATE TABLE Dim_Region (
    Region_ID INT NOT NULL PRIMARY KEY,
    Country_Region NVARCHAR(50) NULL,
    City NVARCHAR(100) NULL,
    State NVARCHAR(100) NULL,
    Postal_Code FLOAT NULL,
    Region NVARCHAR(50) NULL
);
GO

-- Fact_Sales
CREATE TABLE Fact_Sales (
    Fact_ID INT IDENTITY(1,1) PRIMARY KEY,
    Order_Date DATE NOT NULL,
    Product_ID NVARCHAR(50) NOT NULL,
    Customer_ID NVARCHAR(50) NOT NULL,
    Region_ID INT NOT NULL,
    Ship_Date DATE NULL,
    Ship_Mode NVARCHAR(100) NULL,
    Sales FLOAT NULL,
    Quantity INT NULL,
    Discount FLOAT NULL,
    Profit FLOAT NULL,
    Target FLOAT NULL,
    CONSTRAINT FK_FactSales_Date FOREIGN KEY (Order_Date) REFERENCES Dim_Date(Order_Date),
    CONSTRAINT FK_FactSales_Product FOREIGN KEY (Product_ID) REFERENCES Dim_Product(Product_ID),
    CONSTRAINT FK_FactSales_Customer FOREIGN KEY (Customer_ID) REFERENCES Dim_Customer(Customer_ID),
    CONSTRAINT FK_FactSales_Region FOREIGN KEY (Region_ID) REFERENCES Dim_Region(Region_ID)
);
GO

-- B. Tạo bảng staging
IF OBJECT_ID('staging_order','U') IS NOT NULL
    DROP TABLE staging_order;
GO

CREATE TABLE staging_order (
    Order_Date DATETIME NULL,
    Ship_Date DATETIME NULL,
    Ship_Mode NVARCHAR(100) NULL,
    Customer_ID NVARCHAR(50) NULL,
    Customer_Name NVARCHAR(100) NULL,
    Segment NVARCHAR(100) NULL,
    Country_Region NVARCHAR(50) NULL,
    City NVARCHAR(100) NULL,
    State NVARCHAR(100) NULL,
    Postal_Code FLOAT NULL,
    Region NVARCHAR(50) NULL,
    Product_ID NVARCHAR(50) NULL,
    Product_Name NVARCHAR(200) NULL,
    Sub_Category NVARCHAR(155) NULL,
    Category NVARCHAR(155) NULL,
    Sales FLOAT NULL,
    Quantity INT NULL,
    Discount FLOAT NULL,
    Profit FLOAT NULL,
    Target FLOAT NULL,
    Region_ID INT NULL,
    Day INT NULL,
    Month INT NULL,
    Quarter INT NULL,
    Year INT NULL
);
GO

-- C. Stored Procedure ETL: Load từ staging vào các bảng Dim/Fact
CREATE OR ALTER PROCEDURE dbo.usp_LoadFromStaging
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        BEGIN TRAN;

        MERGE INTO Dim_Date AS D
        USING (
            SELECT DISTINCT CAST(Order_Date AS DATE) AS Order_Date,
                   DAY(Order_Date) AS Day,
                   MONTH(Order_Date) AS Month,
                   DATEPART(QUARTER, Order_Date) AS Quarter,
                   YEAR(Order_Date) AS Year
            FROM staging_order
            WHERE Order_Date IS NOT NULL
        ) AS S
        ON D.Order_Date = S.Order_Date
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (Order_Date, Day, Month, Quarter, Year)
            VALUES (S.Order_Date, S.Day, S.Month, S.Quarter, S.Year);

        MERGE INTO Dim_Product AS D
        USING (
            SELECT DISTINCT Product_ID, Product_Name, Sub_Category, Category
            FROM staging_order WHERE Product_ID IS NOT NULL
        ) AS S
        ON D.Product_ID = S.Product_ID
        WHEN MATCHED AND (
            ISNULL(D.Product_Name,'') <> ISNULL(S.Product_Name,'')
            OR ISNULL(D.Sub_Category,'') <> ISNULL(S.Sub_Category,'')
            OR ISNULL(D.Category,'') <> ISNULL(S.Category,'')
        ) THEN
            UPDATE SET Product_Name = S.Product_Name,
                       Sub_Category = S.Sub_Category,
                       Category = S.Category
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (Product_ID, Product_Name, Sub_Category, Category)
            VALUES (S.Product_ID, S.Product_Name, S.Sub_Category, S.Category);

        MERGE INTO Dim_Customer AS D
        USING (
            SELECT DISTINCT Customer_ID, Customer_Name, Segment
            FROM staging_order WHERE Customer_ID IS NOT NULL
        ) AS S
        ON D.Customer_ID = S.Customer_ID
        WHEN MATCHED AND (
            ISNULL(D.Customer_Name,'') <> ISNULL(S.Customer_Name,'')
            OR ISNULL(D.Segment,'') <> ISNULL(S.Segment,'')
        ) THEN
            UPDATE SET Customer_Name = S.Customer_Name, Segment = S.Segment
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (Customer_ID, Customer_Name, Segment)
            VALUES (S.Customer_ID, S.Customer_Name, S.Segment);

        MERGE INTO Dim_Region AS D
        USING (
            SELECT DISTINCT 
                ISNULL(ABS(CHECKSUM(Country_Region, City, State, Postal_Code, Region)), 0) % 1000000 AS Region_ID,
                Country_Region, City, State, Postal_Code, Region
            FROM staging_order
        ) AS S
        ON D.Region_ID = S.Region_ID
        WHEN MATCHED THEN
            UPDATE SET Country_Region = S.Country_Region, City = S.City,
                       State = S.State, Postal_Code = S.Postal_Code, Region = S.Region
        WHEN NOT MATCHED BY TARGET THEN
            INSERT (Region_ID, Country_Region, City, State, Postal_Code, Region)
            VALUES (S.Region_ID, S.Country_Region, S.City, S.State, S.Postal_Code, S.Region);

        INSERT INTO Fact_Sales (Order_Date, Product_ID, Customer_ID, Region_ID, Ship_Date, Ship_Mode, Sales, Quantity, Discount, Profit, Target)
        SELECT
            CAST(s.Order_Date AS DATE), s.Product_ID, s.Customer_ID,
            ISNULL(drg.Region_ID, ISNULL(s.Region_ID, ABS(CHECKSUM(s.Country_Region, s.City, s.State, s.Postal_Code, s.Region)) % 1000000)),
            CAST(s.Ship_Date AS DATE), s.Ship_Mode, s.Sales, s.Quantity, s.Discount, s.Profit, s.Target
        FROM staging_order s
        LEFT JOIN Dim_Region drg
            ON drg.Country_Region = s.Country_Region
            AND drg.City = s.City
        WHERE NOT EXISTS (
            SELECT 1 FROM Fact_Sales f
            WHERE f.Order_Date = CAST(s.Order_Date AS DATE)
              AND f.Product_ID = s.Product_ID
              AND f.Customer_ID = s.Customer_ID
        );

        COMMIT;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0 ROLLBACK;
        RAISERROR('Error in usp_LoadFromStaging: %s',16,1,ERROR_MESSAGE());
    END CATCH
END;
GO

-- D. Tạo login và user
CREATE LOGIN [ETL_USER] WITH PASSWORD = 'StrongPass!123';
GO
USE ALL_ORDER;
CREATE USER [ETL_USER] FOR LOGIN [ETL_USER];
EXEC sp_addrolemember N'db_owner', N'ETL_USER';
GO

-- E. Tạo SQL Agent Job 
USE msdb;
GO

EXEC sp_add_job @job_name = N'ETL_Load_Weekly', @enabled = 1, @description = N'Load từ staging vào DWH hàng tuần';
GO
EXEC sp_add_jobstep @job_name = N'ETL_Load_Weekly', @step_name = N'Run_ETL_Proc', @subsystem = N'TSQL',
    @command = N'USE ALL_ORDER; EXEC dbo.usp_LoadFromStaging;', @on_success_action = 1, @on_fail_action = 2;
GO
EXEC sp_add_schedule @schedule_name = N'Weekly_Sat_02AM', @freq_type = 8, @freq_interval = 64, @active_start_time = 20000;
GO
EXEC sp_attach_schedule @job_name = N'ETL_Load_Weekly', @schedule_name = N'Weekly_Sat_02AM';
GO
EXEC sp_add_jobserver @job_name = N'ETL_Load_Weekly', @server_name = N'(LOCAL)';
GO
