from datetime import datetime
class Task:
    iD = ''
    name = ''
    assigned = False
    completed = False
    startTime = datetime.now()
    deadline = datetime.now()
    warning = False
    project = None
    member = None
    def __init__(self, iD: str = iD, name: str = name, assigned: bool = assigned, completed: bool = completed, startTime: datetime = startTime, deadline: datetime = deadline, warning: bool = warning, project: object = project, member: object = project) -> None:
        self.__iD = iD
        self.__name = name
        self.__assigned = assigned
        self.__completed = completed
        self.__startTime = startTime
        self.__deadline = deadline
        self.__warning = warning
        self.__project = project
        self.__member  = member

    def setID(self, iD: str):
        self.__iD = iD
    def getID(self):
        return self.__iD
    
    def setName(self, name: str):
        self.__name = name
    def getName(self):
        return self.__name
    
    def setAssigned(self, assigned: bool):
        self.__assigned = assigned
    def getAssigned(self):
        return self.__assigned
    
    def setCompleted(self, completed: bool):
        self.__completed = completed
    def getCompleted(self):
        return self.__completed
    
    def setStartTime(self, dd: int, mm: int, yy: int):
        self.__startTime = datetime(yy, mm, dd)
    def getStartTime(self):
        return self.__startTime
    
    def setDeadline(self, dd: int, mm: int, yy: int):
        self.__deadline = datetime(yy, mm, dd)
    def getDeadline(self):
        return self.__deadline
    
    def setProject(self, project: object):
        self.__project = project
    def getProject(self):
        return self.__project
    
    def setMember(self, member: object):
        self.__member = member
    def getMember(self):
        return self.__member

    def setWarning(self, warning: bool):
        self.__warning = warning
    def getWarning(self):
        return self.__warning