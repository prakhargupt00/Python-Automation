#scraps news from hacker news website 

#beutiful removes requirement for making browser object like in seleniuum
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

pages = int(input("Enter the number of pages(integer format)"))

titles=[]
links=[]

for i in  range(pages):
    url = 'https://news.ycombinator.com/news?p='+str(i+1)
    requested_url = urllib.request.urlopen(url)
    page_source = requested_url.read()
    soup = BeautifulSoup(page_source,'html.parser')
    data = soup.find('table', {'class':'itemlist'}).find_all('a',{ 'class':'storylink'})

    for j in data:
        title = j.text 
        link  = j.get('href')
        titles.append(title)
        links.append(link)

dic = {'new_title':titles, 'URLs':links}

df = pd.DataFrame(dic)

df.to_csv("C:\\Users\\acer\\news.csv",index=False)
print("Done")