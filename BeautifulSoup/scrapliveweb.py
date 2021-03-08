import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

yc_soup = BeautifulSoup(yc_web_page, 'html.parser')
article_tag = yc_soup.find(name='a', class_='storylink')
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = yc_soup.find(name='span', class_='score').getText()

print(article_upvote)

