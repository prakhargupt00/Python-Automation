# compares price on amazon and flipkart for the same product and tells the cheaper one 

from selenium import webdriver

#open web browser
path_to_chromedriver_exe_file = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path_to_chromedriver_exe_file)

print("Checking the price on amazon.......")
browser.get('https://www.amazon.in/Test-Exclusive-750/dp/B078BN55WZ/ref=sr_1_1?crid=3OEL6DKYVV850&dchild=1&keywords=one%2Bpluse8%2Bpro%2Bmobile&qid=1597315955&sprefix=one%2Caps%2C290&sr=8-1&th=1')
price = browser.find_element_by_id('priceblock_ourprice')
amazon_price = price.get_attribute('textContent')
amazon_price = amazon_price[2:]
#still conatains comma 
p = amazon_price.split(',')
amazon_price = "" 

for val in p:
    amazon_price += val

amazon_price = float(amazon_price)


print("Checking on Flipkart...........")

# give the product link on flipkart
browser.get('https://www.flipkart.com/oneplus-8-pro-onyx-black-256-gb/p/itm4dcbd336cdd4f?pid=MOBFU897DEZ4SZ9X&lid=LSTMOBFU897DEZ4SZ9X3XJTWH&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=b0ba3921-ac6d-468a-8282-a92473384b97.MOBFU897DEZ4SZ9X.SEARCH&ppt=sp&ppn=sp&ssid=scq9tf7ek00000001597226823165&qH=5894ab4766000b8e')
price=browser.find_element_by_xpath('//div[@class="_1vC4OE _3qQ9m1"]')
price=price.get_attribute('textContent')
flipkart_price=price[1:]
p=flipkart_price.split(',')

flipkart_price=''
for i in p:
	flipkart_price += i 

flipkart_price = float(flipkart_price)

if (flipkart_price < amazon_price):
    print("Flipkart has lower price currently  ")
elif (amazon_price < flipkart_price):
    print("Amazon has lower price currently  ")
else:
    print("Both have same price currently ")





