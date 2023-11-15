from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class testAddStudentForm(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testAddStudentForm(self):

    user = self.driver.find_element(by=By.ID,value='mail')
    password = self.driver.find_element(by=By.ID,value='password')
   
    submit = self.driver.find_element(by=By.ID, value='ingresar')

    #populate the form with data
    user.send_keys('filantropia')
    password.send_keys('filantropia')

    #submit form
    submit.click()
     
    btnAdd = self.driver.find_element(by=By.ID,value='add_student')
    btnAdd.click()


    studentName = self.driver.find_element(by=By.ID,value='id_Nombre')
    studentLastName = self.driver.find_element(by=By.ID,value='id_Apellido')
    email = self.driver.find_element(by=By.ID,value='id_Email')
    Code = self.driver.find_element(by=By.ID,value='id_Codigo')
    semester = self.driver.find_element(by=By.ID,value='id_semester')
    career = self.driver.find_element(by=By.ID,value='id_career')
    select1 = Select(semester)
    select2 = Select(career)
    
    
    studentName.send_keys('Julian')
    studentLastName.send_keys('Agudelo')
    email.send_keys('juli24@gmail.com')
    Code.send_keys('A00381045')
    select1.select_by_visible_text("Quinto Semestre")
    select2.select_by_visible_text("Ingenieria de Sistemas")



    registStudent = self.driver.find_element(by=By.ID,value='boton')
    registStudent.click()
    #registActivity.send_keys(Keys.RETURN)
    popup =self.driver.find_element(by=By.ID,value='isSend')

    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/menu_filantropia/' )
    assert popup.is_displayed()