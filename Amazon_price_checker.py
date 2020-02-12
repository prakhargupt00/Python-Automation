#=======================================================================================
# The problem
# So many times we want to keep checking price of particular product on a certain website
# like amazon so as to get the cheapest price possible but are busy to continuosly do so 
# This script is exactly going to automate that and send a mail when price falls below a
# certain threshold setup by us
#====================================================================================

import requests
from bs4 import BeautifulSoup
import smtplib  #simple mail transfer protocol library 
import time

#Product URL
URL = 'https://www.amazon.in/gp/product/B07DJHXTLJ?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=1098H1YPRF91EP0Z5169'

#Search my user agent on chrome 
headers = {
	"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
}

threshold_price = 30000

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_dealprice").get_text()
	converted_price = price[2:8]
	converted_price = converted_price.replace("," , "")
	converted_price = float(converted_price)
	if(converted_price <= threshold_price): 
		send_mail()

	print(title.strip())
	print(converted_price)

#Enable google 2 step verification (google it)
#Google app password setup
def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587) #587 port i guess
	server.ehlo()
	server.starttls()
	server.ehlo()  #way to say hello to another mail server while conecting via a mail server  

	password = "########" #setup using google app password or use your actual mail password
	server.login('abc@gmail.com', password)

	subject = 'Price fell Down!'
	body = 'Check the link : https://www.amazon.in/gp/product/B07DJHXTLJ?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=1098H1YPRF91EP0Z5169'

	msg = f"subject: {subject}\n\n{body}"

	server.sendmail(
		'abc@gmail.com',
		'abc@gmail.com',
		msg
	)


	print('HEY MAIL HAS BEEN SENT!!')
	server.quit()

while(True):
	check_price()
	time.sleep(3600)
