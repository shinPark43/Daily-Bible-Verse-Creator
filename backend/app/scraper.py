import requests
from bs4 import BeautifulSoup

def scrape_bible_verses(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    verses = []
    
    bible_info = soup.select_one('.bibleinfo_box').text.strip()
    verses.append(bible_info)

    for item in soup.select('ul.body_list > li'):
        number = item.select_one('.num').text.strip()
        content = item.select_one('.info').text.strip()
        verses.append(f"{number}) {content}")
    return verses

url = 'https://sum.su.or.kr:8888/bible/today'
bible_verses = scrape_bible_verses(url)
print("\n".join(bible_verses))
