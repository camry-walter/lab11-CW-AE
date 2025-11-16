# https://github.com/camry-walter/lab11-CW-AE.git
# Partner 1: Camryn Walter
# Partner 2: Adrian Espinoza

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.multiply(9, 3), 27)
        self.assertEqual(calculator.multiply(-4, 2), -8)
        self.assertEqual(calculator.multiply(6, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.divide(3,  9), 3)
        self.assertAlmostEqual(calculator.divide(7, 16), 2.28571, places = 3)
        self.assertRaises(ZeroDivisionError, calculator.divide, 0, 6)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises(ValueError, calculator.logarithm, 0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(4, 6), 7.211102550927978, places = 3)

    def test_sqrt(self): # 3 assertions
        self.assertRaises(ValueError, calculator.square_root, -1)
        self.assertAlmostEqual(calculator.square_root(4), 2.0, places = 3)
        self.assertAlmostEqual(calculator.square_root(9), 3.0, places = 3)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()