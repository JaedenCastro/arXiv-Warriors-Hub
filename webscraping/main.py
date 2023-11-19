from bs4 import BeautifulSoup
import requests

url = "https://bandera.inquirer.net/chika"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
paragraphs = doc.find_all("a",)[:]

for a in paragraphs[::2]:
    if "https://bandera.inquirer.net/" in a['href']:
        print(a['href'])