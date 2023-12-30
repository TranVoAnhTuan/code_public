class Position:
    position = ''
    project = None
    def __init__(self, position: str = position, project: object = project) -> None:
        self.__position = position
        self.__project = project

    def setPosition(self, position: str):
        self.__position = position
    def getPosition(self):
        return self.__position
    
    def setProject(self, project: object):
        self.__project = project
    def getProject(self):
        return self.__project