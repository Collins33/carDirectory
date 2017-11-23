class Car:
    #class variable
    vehicles=[]

    def __init__(self,model,year,color,price):
        #instance variables
        self.model=model
        self.year=year
        self.color=color
        self.price=price
