
from teacher import Teacher
from diligence import Diligence
class SectionClass:
    iD = ''
    name = ''
    teacher = None
    schedule = []
    studentList = []
    diligenceList = []
    def __init__(self, iD: str = iD, name: str = name, teacher: Teacher = teacher, schedule: list = schedule, studentList: list = studentList, diligenceList: list = diligenceList ) -> None:
        self.__iD = iD
        self.__name = name
        self.__teacher = teacher
        self.__schedule = schedule if schedule else []
        self.__studentList = studentList
        self.__diligencenList = diligenceList if diligenceList else []

    def setID(self, iD: str):
        self.__iD = iD
    
    def setName(self, name: str):
        self.__name = name

    def setTeacher(self, teachear: Teacher):
        self.__teacher = teachear
    
    def setSchedule(self, schedule: str):
        self.__schedule.append(schedule)

    def setStudentList(self, student: Student):
        self.__studentList.append(student)

    def setDiligenceList(self, diligence: Diligence):
        self.__diligencenList.append(diligence)

    def getID(self):
        return self.__iD
    
    def getName(self):
        return self.__name
    
    def getStudentList(self):
        return self.__studentList



    