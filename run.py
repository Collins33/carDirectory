#!/usr/bin/env python3.6
from car import Car

def createCar(model,year,color,price):
    newCar= Car(model,year,color,price)
    return newCar

def savCar(car):
    car.saveCar()

def delCar(car):
    car.deleteCar()

def findCar(model):
    return Car.findByModel(model)

def checkExistance(model):
    return Car.carExist(model)

def showAllCars():
    return Car.displayCars()                
