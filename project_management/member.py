class Member:
    iD = ''
    name = ''
    position = None
    task = None
    def __init__(self, iD: str = iD, name: str = name, position: list = position, task: list = task) -> None:
        self.__iD = iD
        self.__name = name
        self.__position = position if position is not None else []
        self.__task = task if task is not None else []

    def setID(self, iD: str):
        self.__iD = iD
    def getID(self):
        return self.__iD
    
    def setName(self, name: str):
        self.__name = name
    def getName(self):
        return self.__name
    
    def addPosition(self, position: object):
        self.__position.append(position)
    def getPosition(self):
        return self.__position

    def addTask(self, task: object):
        self.__task.append(task)
    def checkTaskID(self, iD: str):
        for task in self.__task:
            if task.getID() == iD:
                return True
        else:
            return False
    def getTask(self):
        return self.__task

    def getWarning(self):
        warning = []
        for task in self.__task:
            if task.getWarning():
                warning.append(task.getName())
        return warning
    
