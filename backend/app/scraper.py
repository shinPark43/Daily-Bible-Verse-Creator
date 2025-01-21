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

def save_verses_to_file(verses, filename="bible_verses.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n\n".join(verses))
    print(f"Bible verses saved to {filename}")

url = 'https://sum.su.or.kr:8888/bible/today'
bible_verses = scrape_bible_verses(url)

save_verses_to_file(bible_verses)
