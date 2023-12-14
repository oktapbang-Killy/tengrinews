import requests
from bs4 import BeautifulSoup

url = "https://tengrinews.kz/news/"

response = requests.get(url)
html_code = response.text
soup = BeautifulSoup(html_code, 'html.parser')
news_headlines = soup.find_all('span', class_='tn-article-title')
for index, headline in enumerate(news_headlines, start=1):
    print(f"{index}. {headline.text.strip()}")