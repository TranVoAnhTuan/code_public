class Category:
    iD = ''
    name = ''
    def __init__(self, iD: str = iD, name: str = name) -> None:
        self.__iD = iD
        self.__name = name
    
    def setID(self, iD: str):
        self.__iD = iD
    
    def setName(self, name: str):
        self.__name = name
    
    def getID(self):
        return self.__iD
    
    def getName(self):
        return self.__name
    