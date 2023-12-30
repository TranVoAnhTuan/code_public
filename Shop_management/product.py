class Product:
    iD = ''
    name = ''
    productCategory = None
    brand = None
    quantity = 0
    listPrice = 0.0
    salePrice = 0.0
    currentPrice = 0.0
    def __init__(self, iD: str = iD, name: str = name, productCategory: str = productCategory, brand: object = brand, quantity: int = quantity, listPrice: float = listPrice, salePrice: float = salePrice, currentPrice: float = currentPrice) -> None:
        self.__iD = iD
        self.__name = name
        self.__productCategory = productCategory
        self.__brand = brand
        self.__quantity = quantity
        self.__listPrice = listPrice
        self.__salePrice = salePrice
        self.__currentPrice = currentPrice

    def setID(self, iD: str):
        self.__iD = iD

    def setName(self, name: str):
        self.__name = name

    def setProductCategory(self, category: object):
        self.__productCategory = category

    def setBrand(self, brand: object):
        self.__brand = brand

    def setQuantity(self, quantity: int):
        self.__quantity = quantity

    def updateQuantity(self, quantity: int):
        self.__quantity -= quantity
    
    def setListPrice(self, listPrice: float):
        self.__listPrice = listPrice
        self.__salePrice = listPrice
        self.__currentPrice = listPrice
        
    
    def setSalePrice(self, salePrice: float):
        self.__salePrice = salePrice
    
    def setCurrentPrice(self, currentPrice: float):
        self.__currentPrice = currentPrice

    def getID(self):
        return self.__iD
    
    def getName(self):
        return self.__name
    
    def getProductCategory(self):
        return self.__productCategory.getName()

    def getBrand(self):
        return self.__brand.getName()
    
    def getQuantity(self):
        return self.__quantity
    
    def getListPrice(self):
        return self.__listPrice
    
    def getSalePrice(self):
        return self.__salePrice
    
    def getCurrentPrice(self):
        return self.__currentPrice

    def getInformation(self):
        return f"""
                    iD : {self.__iD}
                    name : {self.__name}
                    price : {self.__currentPrice}
                    """