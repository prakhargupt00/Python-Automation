# Web scraping through Python is fancy way of  gathering useful information from the web .

from selenium import webdriver
import time 
import pandas as pd
import os

#open web browser
path_to_chromedriver_exe_file = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path_to_chromedriver_exe_file)

browser.get('https://www.worldometers.info/coronavirus/') 
rows = browser.find_element_by_xpath("//table[@id='main_table_countries_today']/tbody/tr")

df = pd.DataFrame(columns=['Rank','Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths','Recovered', 'Active Cases', 'Critical'])

for row in rows:
    td_list = row.find_elements_by_tagname('td')
    data = []
    for td in td_list:
        data.append(td.text)
    df_data ={}
    for i in range(len(df.columns)):
        df_data[df.columns[i]] = data[i]
    df.append(df_data,ignore_index=True)

df = df.iloc[1:]

path=os.path.join(base_path,'Covid_Dataset_.csv')
#os.mkdir(path)
df.to_csv(path, index = False)
print("The dataset has been saved at the loction: "+path)
browser.quit()






