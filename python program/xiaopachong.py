import requests
import re
from  bs4 import BeautifulSoup
from selenium import webdriver
import os

if not os.path.exists('OOXX'):
    os.mkdir('OOXX')
os.chdir('OOXX')
url='http://jandan.net/ooxx/page-99'
driver = webdriver.PhantomJS(executable_path="D:\python3\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
driver.get(url)
soup=BeautifulSoup(driver.page_source,'html.parser')
pics=soup.find_all('li',{'id':re.compile('comment-[0-9]+')})
#print(soup)
for pic in pics:
   # print(pic)
    print(pic.find("img",{'src':re.compile('.*\.jpg')})['src'])
    n = pic.find("img",{'src':re.compile('.*\.jpg')})['src']
    name = n[44:64]
    with open(name,'wb') as f:
        reponse = requests.get(n).content
        f.write(reponse)
