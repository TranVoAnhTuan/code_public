from member import Member
from datetime import datetime
class Manager(Member):
    iD = ''
    name = ''
    position = []
    task = []
    project = None
    def __init__(self, iD: str = iD, name: str = name, position: list = position, task: list = task, project: object = project) -> None:
        super().__init__(iD, name, position, task)
        self.__project = project
    
    def setProject(self, project: object):
        self.__project = project

    def setInformation(self, member: object):
        self.__iD = member.getID()
        self.__name = member.getName()
        self.__position = member.getPosition()
        self.__task = member.getTask()

    def assign(self, member: object, task: object):
        if task.getAssigned() == False:
            member.addTask(task)
            task.setMember(member)
            task.setAssigned(True)

    def markCompleted(self, task: object):
        task.setCompleted(True)
        task.setWarning(False)
        now = datetime.now()
        Day = now.day
        Month = now.month
        Year = now.year
        task.setDeadline(Day, Month, Year)

    def trackProgress(self):
        self.__project.getCompleted()
        tasks =  self.__project.getUncompleted()
        for task in tasks:
            x = task.getDeadline() - datetime.now()
            if x.days < 10:
                task.setWarning(True)
    
