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

    #method to delete car object from list
    def deleteCar(self):
        Car.vehicles.remove(self)

    #find car based on model name
    @classmethod
    def findByModel(cls,model):
        for car in cls.vehicles:
            if car.model == model:
                return car


    @classmethod
    def carExist(cls,model):
        for car in cls.vehicles:
            if car.model == model:
                return True

        return False

    @classmethod
    def displayCars(cls):
        return cls.vehicles            
