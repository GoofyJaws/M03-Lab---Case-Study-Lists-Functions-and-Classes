#Jordy Jordan
#11/11/2022
#M03 Lab - Case Study: Lists, Functions, and Classes

#Parent class
class Vehicle:
    def __init__(self,type):
        self.type = type

    #ask user
    def getType(self):
        self.type = input('Please enter the type of vehicle: ')

#Child class
class Automobile(Vehicle):
    def __init__(self, year, doors, make, model, roof):

        #attributes
        self.year =year
        self.doors = doors
        self.make = make
        self.model = model
        self.roof = roof

    #ask user
    def getYear(self):
        self.year = input('Please enter the vehicle year: ')
        
    def getDoors(self):
        self.doors = input('Please enter the vehicle doors (2-4): ')
        
    def getMake(self):
        self.make = input('Please enter the vehicle make: ')
        
    def getModel(self):
        self.model = input('Please enter the vehicle model: ')

    def getRoof(self):
        self.roof = input('Please enter the vehicle roof (sun roof, solid , or no roof): ')

#creates instance
list1 = Automobile('n','n','n','n','n')
print(5*"\n")
#user inputs
Automobile.getType(list1)
Automobile.getYear(list1)
Automobile.getDoors(list1)
Automobile.getMake(list1)
Automobile.getModel(list1)
Automobile.getRoof(list1)

print(10*"\n")
print("Vehicle type: ", list1.type)
print("Year: ", list1.year)
print("Make: ", list1.make)
print("Model: ", list1.model)
print("Number of doors: ", list1.doors)
print("Type of roof: ", list1.roof)
print(5*"\n")
