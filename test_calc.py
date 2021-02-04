import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
 
  def setUp(self):
    self.calculator = Calculator()
 
  def test_add(self):
    self.assertEqual(self.calculator.add(4,7), 11)
    self.assertEqual(self.calculator.add(-1,1), 0)
    self.assertEqual(self.calculator.add(0,11), 11)
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)
    self.assertEqual(self.calculator.subtract(-5,5), -10)
    self.assertEqual(self.calculator.subtract(10,0), 10)
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)
    self.assertEqual(self.calculator.multiply(-3,7), -21)
    self.assertEqual(self.calculator.multiply(3,0), 0)
  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,2), 5)
    self.assertEqual(self.calculator.divide(-50,10), -5)
    self.assertRaises(ValueError,self.calculator.divide,10,0)

if __name__ == "__main__":
  unittest.main()
