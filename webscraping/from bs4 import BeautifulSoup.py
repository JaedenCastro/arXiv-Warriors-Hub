from functions import webscrape_text_per_page
from functions import webscrape_link_per_page
import csv

tracker = 0

def webscrape_abante():
    global tracker
    url = "file:///Users/jaeden/Downloads/News%20_%20Abante%20Tonite.html"
    all_links = webscrape_link_per_page(url)
    news = []
    for i in all_links[:1500]:
        if "https://" in i:
            tracker += 1
            print("webscraping article:  ", tracker)
            a = webscrape_text_per_page(i)
            try:
                news.append(str(a[2]))
            except IndexError:
                if not a:
                    continue
                news.append(str(a))  # In case there's only one element
    return news

def webscrape_bandera(url):
    global tracker
    all_links = webscrape_link_per_page(url)
    news = []
    for i in all_links:
        if "https://bandera" in i:
            tracker += 1
            print("webscraping article:  ", tracker)
            a = webscrape_text_per_page(i)
            if not a:
                break
            try:
                news.append(str(a[2])) # Extend with content only
                print(str(a[2]))
                print(str(a[4]))
            except IndexError:
                news.append(str(a))  # In case there's only one element
                print(str(a))
    return news
def webscrape_all_bandera():
    news = webscrape_bandera("https://bandera.inquirer.net/balita")
    for i in range(2,50):
        news += webscrape_bandera("https://bandera.inquirer.net/balita/page/"+str(i))
    return news

def webscrape_philstar():
    global tracker
    url = "file:///Users/jaeden/Downloads/Pilipino%20Star%20Ngayon%20-%20Bansa%20_%20Philstar.com.html"
    all_links = set(webscrape_link_per_page(url))
    print(all_links)
    news = []
    for i in all_links:
        if i.startswith("https://www.philstar.com/pilipino-star-ngayon/bansa/2024/"):
            tracker += 1
            print("webscraping article:  ", tracker)
            a = webscrape_text_per_page(i)
            try:
                news.append(str(a[2]))
                print(str(a[2]))
            except IndexError:
                news.append(str(a))  # In case there's only one element
                print(str(a))
    return news
# def webscrape_all_philstar():
#     news = webscrape_philstar()
#     for i in range(2,50):
#         news += webscrape_philstar("")

print("on it boss")

with open('news.csv', 'w', newline='') as file:
    writer = csv.writer(file)
#     # news = set(webscrape_abante())
#     # for item in news:
#     #     writer.writerow(("Abante", item))
#     # news = set((webscrape_all_bandera()))
#     # for item in news:
#     #     writer.writerow(("Bandera", item))
    news = set((webscrape_philstar()))
    for item in news:
        writer.writerow(("Philstar", item))
print("done")

