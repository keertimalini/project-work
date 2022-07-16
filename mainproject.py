from selenium import webdriver
from selenium . webdriver.common.by import By
import requests
import time


#class zen guvi
class zenguvi :
    url = "https://www.zenclass.in/login"
    driver = webdriver.firefox()
    data = requests.get(url)
    driver.maximize_winiows()

#login page
def login (self):
  username = "keertimalini0109@gmail.com"
  password = "keerti012345"
  self.driver.get(sel1f.url)
  time.sleep(6)

#username
  username1_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
  username1 = self.driver.find_element(by=By.xpath,value=username1_xpath)
  username1 .send_keys(username1)
  username1.sleep(6)

#password
  password1_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
  password1 = self.driver.find_element(by=By.xpath,value=password1_xpath)
  password1.send_keys(password1)
  time.sleep(6)

#login button
  loginbutton1_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'
  loginbutton1 = self.driver.find_element(by=By.xpath,value=loginbutton1_xpath)
  login.click()
  time.sleep(6)

#creating Query
  def Query(self):
  Heading = "Guvi python AT 1 & 2 Automation project"
  body = " This is a project test code running for the python Automation - 1 & 2 project given by mentor mr. SUMAN GANGOPADHAYAY"

/  Querybutton1_xpath = '//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div/div[2]'
  Querybutton1 = self.driver.find_element(by=By.xpath,value=Querybutton1_xpath)
  Querybutton1.click()
  time.sleep(6)

#create button
  createbutton1_xpath = '//*[@id="root"]/div[2]/div/div[1]/div[1]/button'
  createbutton1 = self.driver.find_element(by=By.xpath,value=createbutton1_xpath)
  createbutton1.click()
  time.sleep(6)

#cancel button
  cancelbutton1_xpath = '//*[@id="WelcomeModal"]/div/div/section[3]/div[2]/button[1]'
  cancelbutton1 = self.driver.find_element(by=By.xpath,value=cancelbutton1_xpath)
  cancelbutton1.click()
  time.sleep(6)

#category
  category1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
  category1 = self.driver.find_element(by=By.xpath,value=category1_xpath)
  category1.click()
  time.sleep(6)

#category option
  categoryoption1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
  categoryoption1 = self.driver.find_element(by=By.xpath,value=categoryoption1_xpath)
  categoryoption1.click()
  time.sleep(6)

#subcategory
  subcategory1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
  subcategory1 = self.driver.find_element(by=By.xpath,value=subcategory1_xpath)
  subcategory1.click()
  time.sleep(6)


#subcategory option
  subcategoryoption1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/label[2]'
  subcategoryoption1 = self.driver.find_element(by=By.xpath,value=subcategoryoption1_xpath)
  subcategoryoption1.click()
  time.sleep(6)


#language
  language1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select'
  language1 = self.driver.find_element(by=By.xpath,value=language1_xpath)
  language1.click()
  time.sleep(6)


#language option
  languageoption1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form'
  languageoption1 = self.driver.find_element(by=By.xpath,value=languageoption1_xpath)
  languageoption1.click()
  time.sleep(6)


#Query tittle
  querytittle1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input'
  querytittle1 = self.driver.find_element(by=By.xpath,value=querytittle1_xpath)
  querytittle1.send_keys(Heading)
  time.sleep(6)


#Query description
  querydescription1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
  querydescription1 = self.driver.find_element(by=By.xpath,value=querydescription1_xpath)
  querydescription1.send_keys(body)
  time.sleep(6)


#Created query button
createdbutton1_xpath = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button'
createdbutton1.click()
time.sleep(6)








