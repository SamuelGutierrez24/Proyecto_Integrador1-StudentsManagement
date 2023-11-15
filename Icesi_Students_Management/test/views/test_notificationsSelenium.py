from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class testNotificationForSend(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testNotificationForSend(self):

    user = self.driver.find_element(by=By.ID,value='mail')
    password = self.driver.find_element(by=By.ID,value='password')
   
    submit = self.driver.find_element(by=By.ID, value='ingresar')

    #populate the form with data
    user.send_keys('filantropia')
    password.send_keys('filantropia')

    #submit form
    submit.click()
     
    notification = self.driver.find_element(by=By.ID,value='noti')
    notification.click()
    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/menu_filantropia/envioAlerta/56/' )


class testNotificationIsSend(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testNotificationIsSend(self):

    user = self.driver.find_element(by=By.ID,value='mail')
    password = self.driver.find_element(by=By.ID,value='password')
   
    submit = self.driver.find_element(by=By.ID, value='ingresar')

    #populate the form with data
    user.send_keys('filantropia')
    password.send_keys('filantropia')

    #submit form
    submit.click()
     
    notification = self.driver.find_element(by=By.ID,value='noti')
    notification.click()

    btnSendNoti = self.driver.find_element(by=By.ID,value='send')
    btnSendNoti.click()
    
    popup =self.driver.find_element(by=By.ID,value='isSend')

    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/menu_filantropia/' )
    assert popup.is_displayed()
    

    

    
    