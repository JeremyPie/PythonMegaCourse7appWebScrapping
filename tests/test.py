import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonhow.com/example.html",
                headers = {'User-agent': 'Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c, "html.parser")
print(soup.prettify())

all = soup.find_all("div", {"class": "cities"})[0]
all = soup.find_all("h2")
all = soup.find_all("h2")
