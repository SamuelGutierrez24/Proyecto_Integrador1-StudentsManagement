from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class testActualice(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testActualice(self):

    user = self.driver.find_element(by=By.ID,value='mail')
    password = self.driver.find_element(by=By.ID,value='password')
   
    submit = self.driver.find_element(by=By.ID, value='ingresar')

    #populate the form with data
    user.send_keys('contabilidad')
    password.send_keys('contabilidad')

    #submit form
    submit.click()
     
    regist = self.driver.find_element(by=By.ID,value='btn1')
    regist.click()

    student = self.driver.find_element(by=By.ID,value='editarbtn')
    student.click()
    gasto = self.driver.find_element(by=By.ID,value='id_gasto')
    date = self.driver.find_element(by=By.ID,value='id_fecha')
    gasto.send_keys('1000000')
    date.send_keys('2023-11-14')
    regist = self.driver.find_element(by=By.ID,value='edit')
    
    regist.send_keys(Keys.RETURN)
    popup =self.driver.find_element(by=By.ID,value='send')

    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/contabilidad/modificar.html/A00231010/' )
    assert popup.is_displayed()