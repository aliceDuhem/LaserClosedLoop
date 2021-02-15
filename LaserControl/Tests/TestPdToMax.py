import unittest
from Motor_calibration import motor_calibration_array

class TestMotorCalibration(unittest.TestCase):

    def testMotorCal(self):
        random_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 11.3, 10.5]
        self.assertEqual(motor_calibration_array(random_array),12)

#What the code does is in comment below
        """ 1
        0.01
        2
        0.01
        3
        0.01
        4
        0.01
        5
        0.01
        6
        0.01
        7
        0.01
        8
        0.01
        9
        0.01
        11
        0.01
        12
        0.01
        -0.01
        The initialisation is finished"""

if __name__ == "__main__":
    unittest.main()
