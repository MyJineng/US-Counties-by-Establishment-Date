from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.pornhub.com/pornstars?gender=female&performerType=pornstar"
site = requests.get(url)
soup = BeautifulSoup(site.text, 'html.parser')

views = [i.text for i in soup.findAll('span', {"class": "viewsNumber performerCount"})]
names = [i.text for i in soup.findAll('span', {"class": "pornStarName performerCardName"})]
ranks = [i.text for i in soup.findAll('span', {"class": "rank_number"})] #PH Rank is based on all performers ie. "amateur" models
videos = [i.text for i in soup.findAll('span', {"class": "videosNumber performerCount"})]
sviews = [s.strip() for s in views]
snames = [s.strip() for s in names]
sranks = [s.strip() for s in ranks]
svideos = [s.strip() for s in videos]

stats = pd.DataFrame({'Name': pd.Series(snames), 'Views': pd.Series(sviews), 'Videos': pd.Series(svideos), 'PH Rank': pd.Series(sranks)})
print(stats)

stats.to_csv('PH.csv', encoding='utf-8', index=False)