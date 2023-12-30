from customer import Customer
from product import Product
from user import User
class Shop:
    iD = ''
    name = ''
    product = []
    customer = []
    user = []
    
    def __init__(self, iD: str = iD, name: str = name, product: list = product, customer: list = customer, user: list = user) -> None:
        self.__iD = iD
        self.__name = name
        self.__product = product
        self.__customer = customer
        self.__user = user
    
    def setID(self, iD: str):
        self.__iD = iD

    def setName(self, name: str):
        self.__name = name

    def addToProduct(self, product: object):
        self.__product.append(product)
    
    def addToCustomer(self, customer: object):
        self.__customer.append(customer)
    
    def addToUser(self, user: object):
        self.__user.append(user)
        user.setShop(self)

    def findCustomerID(self, iD: str):
        for customer in self.__customer:
            if customer.getID() == iD:
                return customer.getInformation()
        else:
            return "non-existent user"

    def findCustomerName(self, name: str):
        for customer in self.__customer:
            if customer.getName() == name:
                return customer.getInformation()
        else:
            return "non-existent user"

    def getInformation(self):
        return self.__iD, self.__name

    def getProductID(self, iD: str):
        for product in self.__product:
            if product.getID() == iD:
                return product
    
    def getProductList(self):
        for product in self.__product:
            print(product.getInformation())
        
    def getProductCategoryList(self, category: str):
        print('List of products by category:')
        for product in self.__product:
            if product.getProductCategory() == category:
                print(product.getInformation())
    
    def getProductCurrentPrice(self, currentPrice: float):
        print('List of products by price')
        for product in self.__product:
            if product.getCurrentPrice() <= currentPrice:
                print(product.getInformation())

    def getTotalInventoryCost(self):
        totalInventoryCost = 0.0
        for product in self.__product:
            if product.getQuantity() >= 0:
                totalInventoryCost += (product.getCurrentPrice() * product.getQuantity())
        return totalInventoryCost
    
