class Bill:
    product = []
    customer = None
    discountList = None
    date = ''
    def __init__(self, product: list = product, customer: object = customer, discountList: object = discountList, date: str = date) -> None:
        self.__product = product
        self.__customer = customer
        self.__discountList = discountList
        self.__date = date

    def addToProduct(self, product: object, quantity: int):
            if (product.getQuantity()- quantity) >= 0:
                self.__product.append((product, quantity))
                product.updateQuantity(quantity)
            
    def setCustomer(self, customer: object):
        self.__customer = customer
        customer.addToBillList(self)

    def setDiscountList(self, discountList: object):
        self.__discountList = discountList

    def setDate(self, date: object):
         self.__date = date

    def orderTotal(self):

        discount = self.__discountList.findDiscount(self.__date)
        
        subtotal = 0.0
        for product in self.__product:
            vouchour = 0.0
            for dis in discount:
                if dis.getAll():
                    vouchour += dis.getDeal()
                elif dis.getCategory() != None:
                    if dis.getCategory().getName() == product[0].getProductCategory():
                        vouchour += dis.getDeal()
                elif dis.getBrand() != None:
                    if dis.getBrand().getName() == product[0].getBrand():
                        vouchour += dis.getDeal()
                elif dis.getProductID():
                    if dis.getProductID() == product[0].getID():
                        vouchour += dis.getDeal()
            subtotal += (product[0].getCurrentPrice() - product[0].getCurrentPrice()*vouchour)
        return subtotal

                    
    