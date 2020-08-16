#selenium is an open source web automation tool.
#webdriver is an open tool used by selenium which makes connection between your program and any website
from selenium import webdriver

#open web browser
path_to_chromedriver_exe_file = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path_to_chromedriver_exe_file)

#open website
browser.get('https://www.facebook.com/')

#get the credentials
email = input("Enter the email address for facebook ")
password = input("enter the password ")

#access email and password fields from the facebook page
email_element = browser.find_element_by_id('email')
password_element = browser.find_element_by_id('pass')

#pass values to the email and password boxes on fb website
email_element.send_keys(email)
password_element.send_keys(password)

#click login 
login = browser.find_element_by_id('u_0_b')
login.click()

#close the browser
browser.quit()

