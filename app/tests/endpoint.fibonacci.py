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
    
    response1 = requests.get(self.base_url, params={'n': 10000})
    self.assertEqual(response1.status_code, 200)
    self.assertEqual(response1.json(), {'result': 33644764876431783266621612005107543310302148460680063906564769974680081442166662368155595513633734025582065332680836159373734790483865268263040892463056431887354544369559827491606602099884183933864652731300088830269235673613135117579297437854413752130520504347701602264758318906527890855154366159582987279682987510631200575428783453215515103870818298969791613127856265033195487140214287532698187962046936097879900350962302291026368131493195275630227837628441540360584402572114334961180023091208287046088923962328835461505776583271252546093591128203925285393434620904245248929403901706233888991085841065183173360437470737908552631764325733993712871937587746897479926305837065742830161637408969178426378624212835258112820516370298089332099905707920064367426202389783111470054074998459250360633560933883831923386783056136435351892133279732908133732642652633989763922723407882928177953580570993691049175470808931841056146322338217465637321248226383092103297701648054726243842374862411453093812206564914032751086643394517512161526545361333111314042436854805106765843493523836959653428071768775328348234345557366719731392746273629108210679280784718035329131176778924659089938635459327894523777674406192240337638674004021330343297496902028328145933418826817683893072003634795623117103101291953169794607632737589253530772552375943788434504067715555779056450443016640119462580972216729758615026968443146952034614932291105970676243268515992834709891284706740862008587135016260312071903172086094081298321581077282076353186624611278245537208532365305775956430072517744315051539600905168603220349163222640885248852433158051534849622434848299380905070483482449327453732624567755879089187190803662058009594743150052402532709746995318770724376825907419939632265984147498193609285223945039707165443156421328157688908058783183404917434556270520223564846495196112460268313970975069382648706613264507665074611512677522748621598642530711298441182622661057163515069260029861704945425047491378115154139941550671256271197133252763631939606902895650288268608362241082050562430701794976171121233066073310059947366875})
    
  
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
