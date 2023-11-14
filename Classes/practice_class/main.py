#We need A class of Person with attributes: name - age
from abc import ABC,abstractmethod

#ABSTRACT CLASS !
class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


#INHERITS FROM ABSTRACT CLASS
class Triangle(Polygon):

    # overriding abstract method based on
    # new Class Specifications
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding Triangle method based on
    # new Class Specifications
    def noofsides(self):
        print("I have 5 sides")

