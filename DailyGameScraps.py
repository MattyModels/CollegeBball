from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\Program Files (x86)\msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get("https://www.espn.com/mens-college-basketball/scoreboard/_/date/20220204/")
html = driver.page_source
soup = bs(html)
#print(soup)

events = soup.body.select("article.scoreboard a.mobileScoreboardLink")
actual_links = [link['href'] for link in events]
ids = soup.body.select("article.scoreboard")
game_ids = [gids['id']for gids in ids]
home_ids = [hids['data-homeid']for hids in ids]
away_ids = [hids['data-awayid']for hids in ids]

date_log = [actual_links, game_ids, home_ids, away_ids]
date_log
