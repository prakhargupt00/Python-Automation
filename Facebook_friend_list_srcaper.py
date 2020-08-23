#scraps names of your facebook friends

from selenium import webdriver
from bs4 import BeautifulSoup


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

#find profile icon and click it
profile=browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
profile.click()

time.sleep(4)
#find friends
friends=browser.find_element_by_xpath('//ul[@class="_6_7 clearfix"]/li[3]/a')
friends.click()

#keep scolling till you get all the friends
while True:
    #now scroll down so as to get all friends 
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    browser.execute_script('window.scrollTo(0,0);')
    try:
        exit_control = browser.find_elements_by_xpath("//*[contains(text(), 'More about you')]")
        break
    except:
        continue

page_source = browser.page_source
soup = BeautifulSoup(page_source,'html.parser')

friends_list = soup.find('div',{'class': '_3i9'})

friends = []
for i in friends_list.findAll('a'):
    friends.append(i.text)   

names_list=[]

#cleaning required as i.text is dirty containing terms like '123 mutual friends'
for name in friends:
    if(name=='FriendFriends'):
        continue
    if('friends' in name):
        continue
    if(name==''):
        continue
    else:
        names_list.append(name)

print(names_list)



