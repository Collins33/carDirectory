import unittest #unittest module
from car import Car #import the car class


class TestCar(unittest.TestCase):

    def setUp(self):
        #this will be run before each Test
        #It will be creating a new object
        self.new_car = Car("Nissan","2007","blue","200000")

    #check if object was initialized
    def test_init(self):
        self.assertEqual(self.new_car.model,"Nissan")
        self.assertEqual(self.new_car.year,"2007")
        self.assertEqual(self.new_car.color,"blue")
        self.assertEqual(self.new_car.price,"200000")






if __name__ == '__main__':
    unittest.main()
