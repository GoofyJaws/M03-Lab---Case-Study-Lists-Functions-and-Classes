#Jordy Jordan
#11/11/2022
#M03 Lab - Case Study: Lists, Functions, and Classes
#This program will ask the user for information about a vehicle and will displayed the information 
#Type, year, doors, make, model , and roof are the only questions the user will need to answer

#Parent class
class Vehicle:
    def __init__(self,type):
        #attributes
        self.type = type

    #ask user about the type
    def getType(self):
        self.type = input('Please enter the type of vehicle: ')

#Child class
class Automobile(Vehicle):
    #the type of vehicle is already in in the parent class
    def __init__(self, year, doors, make, model, roof):

        #attributes
        self.year =year
        self.doors = doors
        self.make = make
        self.model = model
        self.roof = roof

    #ask the user about the vehicle
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
print(5*"\n")#prints 5 empty lines
#enables the user to answer the questions
Automobile.getType(list1)
Automobile.getYear(list1)
Automobile.getDoors(list1)
Automobile.getMake(list1)
Automobile.getModel(list1)
Automobile.getRoof(list1)

print(10*"\n")#prints 10 empty lines

#displays the information in an easy-to-read way
print("Vehicle type: ", list1.type)
print("Year: ", list1.year)
print("Make: ", list1.make)
print("Model: ", list1.model)
print("Number of doors: ", list1.doors)
print("Type of roof: ", list1.roof)

print(5*"\n")#prints 5 empty lines
