import unittest #unittest module
from car import Car #import the car class


class TestCar(unittest.TestCase):

    def setUp(self):
        #this will be run before each Test
        #It will be creating a new object
        self.new_car = Car("Nissan","2007","blue","200000")

    def tearDown(self):
        #this is run after every test
        #it clears the vehicles list everytime
        Car.vehicles=[]

    #check if object was initialized
    def test_init(self):
        self.assertEqual(self.new_car.model,"Nissan")
        self.assertEqual(self.new_car.year,"2007")
        self.assertEqual(self.new_car.color,"blue")
        self.assertEqual(self.new_car.price,"200000")


    #test if objects are saved well
    def test_save_car(self):
        self.new_car.saveCar()#method to save the new car to the vehicles list

        self.assertEqual(len(Car.vehicles),1)

    #test if you can save multiple objects
    def test_save_multiple_cars(self):
        self.new_car.saveCar()
        #create new objects
        test_car=Car("Escalade","2012","black","1000000")
        test_car.saveCar()

        self.assertEqual(len(Car.vehicles),2)

    #test if you can delete an objects
    def test_delete_car(self):
        self.new_car.saveCar()
        #create new objects
        test_car=Car("Escalade","2012","black","1000000")
        test_car.saveCar()

        self.new_car.deleteCar()#delete created object

        self.assertEqual(len(Car.vehicles),1)

    #test if you can find a car by the model
    def test_find_car_by_model(self):
        self.new_car.saveCar()
        #create new objects
        test_car=Car("Escalade","2012","black","1000000")
        test_car.saveCar()

        foundCar=Car.findByModel("Escalade")
        self.assertEqual(foundCar.model,test_car.model)

    #test if a car exists
    def test_car_exists(self):
        self.new_car.saveCar()
        #create new objects
        test_car=Car("Escalade","2012","black","1000000")
        test_car.saveCar()

        carExists=Car.carExist("Escalade")

        self.assertTrue(carExists)

    #test if i can return a list of cars
    def test_car_display_all_cars(self):
        self.assertEqual(Car.displayCars(),Car.vehicles)        











if __name__ == '__main__':
    unittest.main()
