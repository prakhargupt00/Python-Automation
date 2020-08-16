#downloads the profile pic of given instagram handle


from selenium import webdriver
import urllib.request

#open web browser
path_to_chromedriver_exe_file = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path_to_chromedriver_exe_file)

profile_handle = input("Enter the profile handle: ")  #like veg.food

#Get the link 
url = 'https://www.instagram.com/'
url_profile = url+ profile_handle


#open the profile 
browser.get(url_profile)

#for handling  both private and public profiles
try:
    image = browser.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
    image = browser.find_element_by_xpath('//img[@class="be6sR"]')

image_link = image.get_attribute('src')

destination_path = "E:\\" + profile_handle + ".jpg"
urllib.request.urlretrieve(image_link,destination_path) 

print("Download completed !! View at path : "+ destination_path)

