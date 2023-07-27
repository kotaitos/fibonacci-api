import sys
sys.path.append('../')

import unittest
from utils import fibonacci

class TestFibonacci(unittest.TestCase):
  def test_base_cases(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)
    
  
  def test_small_input(self):
    self.assertEqual(fibonacci(3), 2)
  
  
  def test_large_input(self):
    self.assertEqual(fibonacci(500), 280571172992510140037611932413038677189525)
      
  
  def test_random_inputs(self):
    self.assertEqual(fibonacci(8), 21)
    self.assertEqual(fibonacci(12), 144)
    self.assertEqual(fibonacci(15), 610)


if __name__ == "__main__":
  unittest.main()
  