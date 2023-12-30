class Project:
    member = []
    task = []
    manager = None
    def __init__(self, member: list = member, task: list = task, manager: object = manager) -> None:
        self.__member = member
        self.__task = task
        self.__manager = manager

    def addMember(self, member: object, position: object):
        self.__member.append(member)
        member.addPosition(position)

    def addTask(self, task: object):
        self.__task.append(task)
        task.setProject(self)

    def setManager(self, manager: object, member: object):
        self.__manager = manager
        manager.setInformation(member)
        manager.setProject(self)
    
    def getCompleted(self):
        for task in self.__task:
            if task.getCompleted():
                print(task.getID()+ '\t' + task.getName() + '\n')

    def getUncompleted(self):
        uncompleted =[]
        for task in self.__task:
            if task.getCompleted() == False:
                uncompleted.append(task)
        return uncompleted
    
    def getMeanTime(self):
        day = 0
        for task in self.__task:
            day += (task.getDeadline() - task.getStartTime()).days
        return (day/len(self.__task))