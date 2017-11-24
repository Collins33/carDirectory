#!/usr/bin/env python3.6
from car import Car

def createCar(model,year,color,price):
    newCar= Car(model,year,color,price)
    return newCar

def saveCar(car):
    car.saveCar()

def delCar(car):
    car.deleteCar()

def findCar(model):
    return Car.findByModel(model)

def checkExistance(model):
    return Car.carExist(model)

def showAllCars():
    return Car.displayCars()



#the main functon to be run
def main():
    print ("Hello welcome to Njau Motors.What is tour name?")
    user_name= input()
    print(f"Hello {user_name}")
    print('\n')

    print("Use this short codes to proceed:cc-create new car,dc-display cars,fc-find a car,ex-exit directory")
    shortCode=input().lower()
    if shortCode == 'cc':
        print("CREATE A CAR")
        print("-"*15)

        print("enter car model")
        model=input()
        print("enter the year of manufacture")
        year=input()
        print("enter car color")
        color=input()
        print("enter car price")
        price=input()

        saveCar(createCar(model,year,color,price))#create and save vehicle

        print('\n')

        print(f"The {model} has been added to the directory")









if __name__ == '__main__':

    main()
