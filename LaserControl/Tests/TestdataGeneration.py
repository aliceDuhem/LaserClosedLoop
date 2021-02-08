#Test of the dataGeneration functions
import unittest
from dataGenerationScript import openReadCsv
from dataGenerationScript import dataGeneration

class TestDataGenerationMethods(unittest.TestCase):

#Tests if the function gets the correct values from the fake data csv file
    def testOpenReadCsv(self):
        #Try the openReadCsv funciton
        fileName = "fake_intensity_data_test.csv"
        intensities = openReadCsv(fileName)
        self.assertEqual(intensities[0],8.32, "Actual data not the expected 0.012345")
        self.assertEqual(intensities[2],8.25, "Actual data not the expected 0.267891")

#Tests all the different cases for the datageneration
    def testDataGeneration(self):
        #Defines the primary values, they will be changed after for other tests
        argument =1
        laser_intensity = 8.32
        increment = 0
        fileName=""
        fileArray=[]


        """start the Tests with the case with argument 1 (use random)"""
        laser_intensity_generated = dataGeneration(argument,laser_intensity, increment, fileArray)
        #Tests that the function added a random number to the laser intensity to 10^-5
        self.assertAlmostEqual(laser_intensity_generated,laser_intensity,1)
        self.assertNotAlmostEqual(laser_intensity_generated,laser_intensity,3)

        """start the Tests with the case with argument 2 (reads data from file)"""
        argument = 2
        laser_intensity = 0
        fileName = "fake_intensity_data_test.csv"
        fileArray = openReadCsv(fileName)

        for increment in range(0,2):
            laser_intensity_generated = dataGeneration(argument,laser_intensity, increment, fileArray)
            self.assertEqual(laser_intensity_generated,fileArray[increment])

        #Test with another method to make sure
        increment = 1
        laser_intensity_generated = dataGeneration(argument,laser_intensity, increment, fileArray)
        self.assertEqual(laser_intensity_generated,8.28)



if __name__ == "__main__":
    unittest.main()
