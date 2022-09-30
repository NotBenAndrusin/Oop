import random

class Insect: 

    def __init__(self,l,w):
        self.__wings = w
        self.__legs = l
        self.__flight = 0


    
    def flight_length(self):
        self.__flight = random.randint(1,10)
        #print("the length of the the flight is" + leng)
        
    def get_flight(self):
        return self.__flight
