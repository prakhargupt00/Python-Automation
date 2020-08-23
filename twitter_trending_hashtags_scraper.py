from selenium import webdriver
import time 

#open web browser
path_to_chromedriver_exe_file = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path_to_chromedriver_exe_file)

#open website
browser.get('https://twitter.com/explore/tabs/trending')

#beacuse it takes time to load website so add a sleep
time.sleep(15)

#go to explore section and check trending

sp = browser.find_element_by_tag_name('span')

#check only those among trending that has hash tags

fl = []
for i in sp:
    a=i.get_attribute('textContent')
    if (a.startswith('#')):
		if a not in fl:
			fl.append(a)

urls=[]
for i in fl:
	i=i[1:]
	url='https://twitter.com/search?q=%23'+i+'&src=trend_click'
	urls.append(url)

dic={'HashTag':fl,'URL':urls}

df=pd.DataFrame(dic)
df.to_csv("C:\\Users\\acer\\Twitter_HT.csv",index=False)
print("The data is stored at C:\\Users\\acer\\Twitter_HT.csv")