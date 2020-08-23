#scraps contact info , name , current position of all your lindedin connections  

from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import pandas as pd

#open web browser
path_to_chromedriver_exe_file = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path_to_chromedriver_exe_file)

browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')

#find sign in link 
sign_in = browser.find_element_by_xpath('//a[@class =="main__sign-in-link"]')
sign_in.click()
time.sleep(20)

#take email input
email = input("Enter your email here: ")
passw = input("Enter your password here: ")

#find and fill credentials field

email_field=browser.find_element_by_xpath('//input[@id="username"]')
email_field.send_keys(email)
passw_field=browser.find_element_by_xpath('//input[@id="password"]')
passw_field.send_keys(passw)

#click login button
btn=browser.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]')
btn.click()

#Gather all the connections 
page_source = browser.page_source
soup = BeautifulSoup(page_source,'html.parser')
details = soup.findAll('div',{'class':"mn-connection-card__details"})


connections = []

for i in details:
    anchor_element = i.find('a')
    href = anchor_element.get('href')
    connections.append(href)

connection_name = []
connection_position = []
connection_contact = []

for connection in connections:
    connection_url="https://www.linkedin.com/" + connection
    browser.get(connection_url)
    time.sleep(1)
    
    name_element=browser.find_element_by_xpath('//div[@class="flex-1 mr5"]/ul[1]/li[1]')
    name=name_element.text
    connection_name.append(name)

    position_element=browser.find_element_by_xpath('//div[@class="flex-1 mr5"]/h2[1]')
    cpos=position_element.text
    connection_position.append(cpos)

    contact_info=connection_url + 'detail/contact-info/'
    connection_contact.append(contact_info) 


dic={'Name': connection_name ,'Current Position':connection_position , 'Contact Info': connection_contact}
df=pd.DataFrame(dic)
df.to_csv("C:\\Users\\acer\\LinkedIn connection.csv",index=False)

print("DONE")







