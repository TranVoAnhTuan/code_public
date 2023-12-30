class Brand:
    iD = ''
    name = ''
    country = ''
    def __init__(self, iD: str = iD, name: str = name, country: str = country) -> None:
        self.__iD = iD
        self.__name = name
        self.__country = country

    def setID(self, iD: str):
        self.__iD = iD
    
    def setName(self, name: str):
        self.__name = name

    def setCountry(self, country: str):
        self.__country = country

    def getID(self):
        return self.__iD
    
    def getName(self):
        return self.__name
    
    def getCountry(self):
        return self.__country