class Discount:
    category = None
    brand = None
    product = ''
    All = False
    deal = 0.0
    start = ''
    end = ''
    def __init__(self, category: object = category, brand: object = brand, product: str = product, All = All, deal: float = deal, start: str = start, end: str = end) -> None:
        self.__category = category
        self.__brand = brand
        self.__productID = product
        self.__all = All
        self.__deal = deal
        self.__start = start
        self.__end = end

    def setCategory(self, category: object):
        self.__category = category

    def setBrand(self, brand: object):
        self.__brand = brand
    
    def setProductID(self, productID: str):
        self.__productID = productID

    def setAll(self, All):
        self.__all = All
    
    def setDeal(self, deal: float):
        self.__deal = deal

    def setTime(self, start: str, end: str):
        self.__start = start
        self.__end = end

    def getCategory(self):
        return self.__category

    def getBrand(self):
        return self.__brand
    
    def getProductID(self):
        return self.__productID
    
    def getAll(self):
        return self.__all
    
    def getDeal(self):
        return self.__deal
    
    def getStartTime(self):
        return self.__start
    
    def getEndTime(self):
        return self.__end