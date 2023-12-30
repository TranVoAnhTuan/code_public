class User:
    iD = ''
    name = ''
    shop = None
    def __init__(self, iD: str = iD, name: str = name, shop: object = shop) -> None:
        self.__iD = iD
        self.__name = name
        self.__shop = shop

    def setID(self, iD: str):
        self.__iD = iD
    
    def setName(self, name: str):
        self.__name = name
    
    def setShop(self, shop: object):
        self.__shop = shop
    
    def getInformation(self):
        return self.__iD, self.__name, self.__shop.getInformation()
    
    def updateProductCurrentPrice(self,iD: str, currentPrice: float):
        product = self.__shop.getProductID(iD)
        product.setCurrentPrice(currentPrice)