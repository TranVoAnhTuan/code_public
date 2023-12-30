from sectionClass import SectionClass
class Student:
    iD = ''
    fullName = ''
    sectionClassList = []
    def __init__(self, iD: str = iD, fullName: str = fullName, sectionClassList: list = sectionClassList) -> None:
        self.__iD = iD
        self.__fullName = fullName
        self.__sectionClassList = sectionClassList if sectionClassList else []

    def setID(self, iD: str):
        self.__iD = iD
    
    def setFullName(self, fullName: str):
        self.__fullName = fullName

    def setSectionClass(self, sectionClass: SectionClass):
        self.__sectionClassList.append(sectionClass)