import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

yc_soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = yc_soup.find_all(name='a', class_='storylink')
articles_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_upvotes = [score.getText().split(' ')[0] for score in yc_soup.find_all(name='span', class_='score')]

print(article_upvotes)
