from datetime import datetime
class Diligence:
    time = ''
    studentDict = {}
    def __init__(self, time: str = time, studentDict: dict = studentDict) -> None:
        self.__time = datetime.now()
        self.__studentDict = {} if studentDict else {}
    
    def setDiligence(self, studentList: list):       
        for student in studentList:
            self.__studentDict[student] = 'có'
        for student in studentList:
            number = int(input("1: vắng có phép; \n 2: vắng không phép; \n 3: đi trễ \n"))
            if number == '1':
                self.__studentDict[student] = 'vắng có phép'
            elif number == '2':
                self.__studentDict[student] = 'vắng không phép'
            elif number == '3':
                self.__studentDict[student] = 'đi trễ'


    def getTime(self):
        return self.__time.year, self.__time.month, self.__time.day
    
    
    
    