from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# Create your tests here.
class testSinginForm(LiveServerTestCase):
  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testLoginForm(self):

    user = self.driver.find_element(by=By.ID,value='form2Example11')
    password = self.driver.find_element(by=By.ID,value='form2Example22')
   
    submit = self.driver.find_element(by=By.ID, value='submit-button')

    #populate the form with data
    user.send_keys('samu')
    password.send_keys('1234567')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/bienestarUniversitario/' )

  
class testSingUpForm(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signup/')

  def testSingUpForm(self):
     
    name = self.driver.find_element(by=By.ID,value='name')
    lastName = self.driver.find_element(by=By.ID,value='lastName')
    username = self.driver.find_element(by=By.ID,value='username')
    email = self.driver.find_element(by=By.ID,value='email')
    phone = self.driver.find_element(by=By.ID,value='phoneNumber')
    password1 = self.driver.find_element(by=By.ID,value='password1')
    password2 = self.driver.find_element(by=By.ID,value='password2')
    regist = self.driver.find_element(by=By.ID,value='registerBtn')

    name.send_keys('Juan')
    lastName.send_keys('Gonzales')
    username.send_keys('Juancito')
    email.send_keys('juanGonza@gmail.com')
    phone.send_keys('3145567894')
    password1.send_keys('ElDomiEschevehere')
    password2.send_keys('ElDomiEschevehere')

    regist.send_keys(Keys.RETURN)
    popup =self.driver.find_element(by=By.ID,value='alert')


    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/signin/' )
    assert popup.is_displayed()


     
  


