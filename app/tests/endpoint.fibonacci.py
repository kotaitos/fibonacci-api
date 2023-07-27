import os
import unittest
import requests


class TestFibonacciEndpoint(unittest.TestCase):
  def setUp(self):
    self.base_url = os.getenv('BASE_URL', 'http://localhost:8000/fib')
    
  
  def test_base_cases(self):
    response1 = requests.get(self.base_url, params={'n': 0})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 0})
    
    response2 = requests.get(self.base_url, params={'n': 1})
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json(), {'result': 1})
    
    response1 = requests.get(self.base_url, params={'n': 2})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 1})
    
  
  def test_small_input(self):
    response2 = requests.get(self.base_url, params={'n': 3})
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json(), {'result': 2})
    
    
  def test_large_input(self):
    response2 = requests.get(self.base_url, params={'n': 30})
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json(), {'result': 832040})
    
  
  def test_negative_input(self):
    response1 = requests.get(self.base_url, params={'n': -1})
    self.assertEqual(response1.status_code, 400)
    self.assertEqual(response1.json(), {'status': 400, 'message': 'Bad Request'})
    
    
  def test_non_integer_input(self):
    response1 = requests.get(self.base_url, params={'n': 3.14})
    self.assertEqual(response1.status_code, 400)
    self.assertEqual(response1.json(), {'status': 400, 'message': 'Bad Request'})
    
    response2 = requests.get(self.base_url, params={'n': 'Hello'})
    self.assertEqual(response2.status_code, 400)
    self.assertEqual(response2.json(), {'status': 400, 'message': 'Bad Request'})
    
    response3 = requests.get(self.base_url, params={'n': True})
    self.assertEqual(response3.status_code, 400)
    self.assertEqual(response3.json(), {'status': 400, 'message': 'Bad Request'})
    
    response4 = requests.get(self.base_url, params={'n': None})
    self.assertEqual(response4.status_code, 400)
    self.assertEqual(response4.json(), {'status': 400, 'message': 'Bad Request'})
    
  
  def test_performance(self):
    response1 = requests.get(self.base_url, params={'n': 1000})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875})
    
  
  def test_random_inputs(self):
    response1 = requests.get(self.base_url, params={'n': 8})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 21})
    
    response2 = requests.get(self.base_url, params={'n': 13})
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json(), {'result': 233})
    
    response3 = requests.get(self.base_url, params={'n': 21})
    self.assertEqual(response3.status_code, 200)
    self.assertEqual(response3.json(), {'result': 10946})
    
    
if __name__ == '__main__':
  print('base_url:', os.getenv('BASE_URL', 'http://localhost:8000/fib'))
  unittest.main()
