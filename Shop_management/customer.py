class Customer:
    iD = ''
    name = ''
    billList = []
    def __init__(self, iD: str = iD, name: str = name, billList: list = billList) -> None:
        self.__iD = iD
        self.__name = name
        self.__billList = billList
    
    def setID(self, iD):
        self.__iD = iD
    
    def setName(self, name):
        self.__name = name
    
    def addToBillList(self, bill: object):
        self.__billList.append(bill)

    def getID(self):
        return self.__iD
    
    def getName(self):
        return self.__name
    
    def getInformation(self):
        return self.__iD, self.__name
    
    def getBillList(self):
        for bill in self.__billList:
            bill.getInformation()