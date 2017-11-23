class Car:
    #class variable
    vehicles=[]

    def __init__(self,model,year,color,price):
        #instance variables
        self.model=model
        self.year=year
        self.color=color
        self.price=price


    #method to save car objects into vehicles
    def saveCar(self):
        #appends new object into the list
        Car.vehicles.append(self)
