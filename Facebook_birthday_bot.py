#Wishing happy birthday on behalf of you

#Using Xpath we can navigate to various elements of the HTML DOCUMENT.. it is used with selenium
#search using XPath ... Syntax of Xpath: '//name_of_element[@name_of_attribute='value_of_attribute']'

from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
#Step 1 -> Login into Facebook


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

time.sleep(20)

#Step 2 -> Check for the number of people having birthday today
xpath = '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'  # * means -> check for all elemets
n = browser.find_element_by_xpath(xpath).get_attribute('textContent') #text content is what text is between the tags

# To get the number of the friends to be wished ..... n is something like '3 others' 
num = int(n[0]) 
print(num) 

message = "Happy Birthday !!"
browser.get('https://www.facebook.com/events/birthdays/')
#time.sleep(3)

events_link_xpath = "//*[@class = 'enter_submit_UTI_.get_using_inspect_elemet']"
bday_list = browser.find_element_by_xpath(events_link_xpath)


count_wishes = 0  #to avoid sending belated wishes

for element  in bday_list:
    element_id = str(element.get_attribute('id'))# to fetch box to which we need to write message
    XPATH = '//*[@id = "' + element_id+  '"]'
    post = browser.find_element_by_xpath(XPATH)
    post.send_keys(message)
    #time.sleep(1)
    post.send_keys(Keys.RETURN) #similar to pressing enter
    count_wishes += 1
    if(count_wishes>num):
        break; 


browser.quit()