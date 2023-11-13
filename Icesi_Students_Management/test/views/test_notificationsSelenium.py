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

    user = self.driver.find_element(by=By.ID,value='form2Example11')
    password = self.driver.find_element(by=By.ID,value='form2Example22')
   
    submit = self.driver.find_element(by=By.ID, value='submit-button')

    #populate the form with data
    user.send_keys('filantropia')
    password.send_keys('filantropia')

    #submit form
    submit.click()
     
    notification = self.driver.find_element(by=By.ID,value='noti')
    notification.click()
    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/menu_filantropia/envioAlerta/1/' )


class testNotificationIsSend(LiveServerTestCase):

  def setUp(self):

      self.driver = webdriver.Chrome()

      self.driver = webdriver.Chrome()

      self.driver.get('http://127.0.0.1:8000/signin/')

  def testNotificationIsSend(self):

    user = self.driver.find_element(by=By.ID,value='form2Example11')
    password = self.driver.find_element(by=By.ID,value='form2Example22')
   
    submit = self.driver.find_element(by=By.ID, value='submit-button')

    #populate the form with data
    user.send_keys('filantropia')
    password.send_keys('filantropia')

    #submit form
    submit.click()
     
    notification = self.driver.find_element(by=By.ID,value='noti')
    notification.click()

    btnSendNoti = self.driver.find_element(by=By.ID,value='sendNoti')
    btnSendNoti.click()
    
    #popup =self.driver.find_element(by=By.ID,value='alertC')

    self.assertEqual(self.driver.current_url,'http://127.0.0.1:8000/menu_filantropia/' )
    #assert popup.is_displayed()
    

    

    
    