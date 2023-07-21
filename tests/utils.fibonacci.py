import sys
sys.path.append('../')

import unittest
from app.utils import fibonacci

class TestFibonacci(unittest.TestCase):
  def test_base_cases(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
  
  
  def test_small_input(self):
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(3), 2)
    self.assertEqual(fibonacci(4), 3)
  
  
  def test_large_input(self):
    self.assertEqual(fibonacci(10), 55)
    self.assertEqual(fibonacci(20), 6765)
    
  
  def test_negative_input(self):
    with self.assertRaises(ValueError):
      fibonacci(-1)
    with self.assertRaises(ValueError):
      fibonacci(-10)
    with self.assertRaises(ValueError):
      fibonacci(-100)
      
  
  def test_non_integer_input(self):
    with self.assertRaises(ValueError):
      fibonacci(3.14)
    
    with self.assertRaises(ValueError):
      fibonacci([1, 2, 3])
    
    with self.assertRaises(ValueError):
      fibonacci("Hello")
      
    with self.assertRaises(ValueError):
      fibonacci(True)
      
    with self.assertRaises(ValueError):
      fibonacci(None)
      
  
  def test_performance(self):
    self.assertEqual(fibonacci(40), 102334155)
    
  
  def test_random_inputs(self):
    self.assertEqual(fibonacci(8), 21)
    self.assertEqual(fibonacci(12), 144)
    self.assertEqual(fibonacci(15), 610)


if __name__ == "__main__":
  unittest.main()
  