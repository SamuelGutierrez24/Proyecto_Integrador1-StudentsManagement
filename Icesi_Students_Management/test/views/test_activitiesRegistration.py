from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class testActivityBUForm(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testActivityBUForm(self):

    user = self.driver.find_element(by=By.ID,value='mail')
    password = self.driver.find_element(by=By.ID,value='password')
   
    submit = self.driver.find_element(by=By.ID, value='ingresar')

    #populate the form with data
    user.send_keys('samu')
    password.send_keys('1234567')

    #submit form
    submit.click()
     
    regist = self.driver.find_element(by=By.ID,value='BtnRegistAct')
    regist.click()

    student = self.driver.find_element(by=By.ID,value='id_student')
    search = self.driver.find_element(by=By.ID,value='search')
    student.send_keys('A00381035')
    search.click()

    activity = self.driver.find_element(by=By.ID,value='id_activity')
    select = Select(activity)

    registActivity = self.driver.find_element(by=By.ID,value='BtnRegist')
    select.select_by_visible_text("Atletismo")
    
    registActivity.send_keys(Keys.RETURN)
    popup =self.driver.find_element(by=By.ID,value='alertBU')

    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/bienestarUniversitario/registroActividades' )
    assert popup.is_displayed()

class testActivityCreForm(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testActivityCreaForm(self):

    user = self.driver.find_element(by=By.ID,value='mail')
    password = self.driver.find_element(by=By.ID,value='password')
   
    submit = self.driver.find_element(by=By.ID, value='ingresar')

    #populate the form with data
    user.send_keys('crea')
    password.send_keys('crea')

    #submit form
    submit.click()
     
    regist = self.driver.find_element(by=By.ID,value='BtnRegistC')
    regist.click()


    student = self.driver.find_element(by=By.ID,value='id_student')
    search = self.driver.find_element(by=By.ID,value='search')
    student.send_keys('A00381035')
    search.click()

    activity = self.driver.find_element(by=By.ID,value='id_activity')
    select = Select(activity)
    registActivity = self.driver.find_element(by=By.ID,value='Btnregist')
    reason = self.driver.find_element(by=By.ID,value='id_reason')

    reason.send_keys('No se nada de matematicas')

    select.select_by_visible_text("Cambas")
    registActivity.send_keys(Keys.RETURN)
    popup =self.driver.find_element(by=By.ID,value='alertC')

    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/Crea/register' )
    assert popup.is_displayed()