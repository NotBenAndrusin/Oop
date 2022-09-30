class Employee:
    def __init__(self, name, id, depart, title, salary):
        self.__name = name
        self.__id = id
        self.__depart = depart
        self.__title = title
        self.__salary = salary
    
    def getName(self):
        return self.__name
    
    def getID(self):
        return self.__id
    
    def getDepartment(self):
        return self.__depart
    
    def getTitle(self):
        return self.__title
    
    def getSalary(self):
        return self.__salary
