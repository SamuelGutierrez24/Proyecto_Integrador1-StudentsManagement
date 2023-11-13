from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class testAddMaterias(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testAdMaterias(self):

    user = self.driver.find_element(by=By.ID,value='form2Example11')
    password = self.driver.find_element(by=By.ID,value='form2Example22')
   
    submit = self.driver.find_element(by=By.ID, value='submit-button')

    #populate the form with data
    user.send_keys('director')
    password.send_keys('director')

    #submit form
    submit.click()
     
    regist = self.driver.find_element(by=By.ID,value='botonCuerpo')
    regist.click()

    student = self.driver.find_element(by=By.ID,value='inputBuscarEstud')
    student.send_keys('A00381035')
    search = self.driver.find_element(by=By.ID,value='botonBuscarEstud')
    search.click()

    addM = self.driver.find_element(by=By.ID,value='añadirM')
    addM.click()
    codM = self.driver.find_element(by=By.ID,value='codMateria2')
    nameM = self.driver.find_element(by=By.ID,value='nombreMateria2')
    creditsM = self.driver.find_element(by=By.ID,value='creditosMateria2')
    status = self.driver.find_element(by=By.ID,value='estatusMateria2')
    eva= self.driver.find_element(by=By.ID,value='Nota2')
    btn = self.driver.find_element(by=By.ID,value='SubirNotas')

    select = Select(status)

    codM.send_keys('1035')
    nameM.send_keys('Ingenieria de Software I')
    creditsM.send_keys('4')
    select.select_by_visible_text('Materia en Curso')
    eva.send_keys('0')
    btn.click()
    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/BalanceAcademico/' )
  