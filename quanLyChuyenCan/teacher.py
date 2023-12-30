from diligence import Diligence
from sectionClass import SectionClass
class Teacher:
    iD = ''
    fullName = ''
    sectionClass = []
    def __init__(self, iD: str = iD, fullName: str = fullName, sectionClass: list = sectionClass) -> None:
        self.__iD = iD
        self.__fullName = fullName
        self.__sectionClass = sectionClass if sectionClass else []

    def setID(self, iD: str):
        self.__iD = iD

    def setFullName(self, fullName: str):
        self.__fullName = fullName
    
    def setSectionClass(self, sectionClass: SectionClass):
        self.__sectionClass.append(sectionClass)
        sectionClass.setTeacher(self)

    def diligenceStudent(self):
        for index in range(len(self.__sectionClass)):
            print(f'{index}: {self.__sectionClass[index].getID}, {self.__sectionClass[index].getName}')
        n = int(input('nhập số của lớp đã chọn: '))
        diligenceClass = Diligence()
        diligenceClass.setDiligence(self.__sectionClass[n].getStudentList)
        self.__sectionClass[n].setDiligence(diligenceClass)
        
