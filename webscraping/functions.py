import bs4 as bs
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  # cloudflare is blocking my ass

def webscrape_link_per_page(link):
    global tracker
    req = urllib.request.Request(url=link, headers=headers)
    source = urllib.request.urlopen(req).read()
    articles = []
    soup = bs.BeautifulSoup(source, 'lxml')
    for paragraph in soup.find_all('a', href=True):
        articles.append(paragraph['href'])
    return articles

def webscrape_text_per_page(link):
    text = []
    req = urllib.request.Request(url=link, headers=headers)
    try:
        source = urllib.request.urlopen(req).read()
    except Exception as e:
        return text
    soup = bs.BeautifulSoup(source, 'lxml')
    for paragraph in soup.find_all("p"):
        text.append(str(paragraph.text))
    return text
arr = webscrape_link_per_page("https://digiskillet.com/")
print(arr)
for i in arr:
    print(webscrape_text_per_page("https://digiskillet.com/"+i))
             
                                                                                          