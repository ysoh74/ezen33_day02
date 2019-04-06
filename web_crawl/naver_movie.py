from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

ctx = 'C:/Users/Ysoh/PycharmProjects/'
driver = webdriver.Chrome(ctx+"chromedriver")  #대문자 --> 객체 생성하는 문법
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())

all_divs = soup.find_all('div', attrs={'class':'tit3'})
products = [div.a.string for div in all_divs]
for i in products:
    print((i))
driver.close()




