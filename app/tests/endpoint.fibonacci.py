import unittest
import requests


class TestFibonacciEndpoint(unittest.TestCase):
  def setUp(self):
    self.base_url = 'http://localhost:8000/fib'
    
  
  def test_base_cases(self):
    response1 = requests.get(self.base_url, params={'n': 0})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 0})
    
    response2 = requests.get(self.base_url, params={'n': 1})
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json(), {'result': 1})
    
  
  def test_small_input(self):
    response1 = requests.get(self.base_url, params={'n': 2})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 1})
    
    response2 = requests.get(self.base_url, params={'n': 3})
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json(), {'result': 2})
    
    response3 = requests.get(self.base_url, params={'n': 4})
    self.assertEqual(response3.status_code, 200)
    self.assertEqual(response3.json(), {'result': 3})
    
    
  def test_large_input(self):
    response1 = requests.get(self.base_url, params={'n': 100})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 354224848179261915075})
    
    response2 = requests.get(self.base_url, params={'n': 200})
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json(), {'result': 280571172992510140037611932413038677189525})
    
  
  def test_negative_input(self):
    response1 = requests.get(self.base_url, params={'n': -1})
    self.assertEqual(response1.status_code, 400)
    self.assertEqual(response1.json(), {'status': 400, 'message': 'Bad Request'})
    
    response2 = requests.get(self.base_url, params={'n': -10})
    self.assertEqual(response2.status_code, 400)
    self.assertEqual(response2.json(), {'status': 400, 'message': 'Bad Request'})
    
    response3 = requests.get(self.base_url, params={'n': -100})
    self.assertEqual(response3.status_code, 400)
    self.assertEqual(response3.json(), {'status': 400, 'message': 'Bad Request'})
    
    
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
    response1 = requests.get(self.base_url, params={'n': 500})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125})
    
  
  def test_too_large_input(self):
    response1 = requests.get(self.base_url, params={'n': 1000})
    self.assertEqual(response1.status_code, 400)
    self.assertEqual(response1.json(), {'status': 400, 'message': 'Requested number is too large'})
    
  
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
  unittest.main()
