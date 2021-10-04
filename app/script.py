import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
                     headers = {'User-agent': 'Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")
max_page = int(soup.find_all("a", {"class": "Page"})[-1].text)

base_url = "https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
l = []
for page in range(0, max_page * 10, 10):
    r = requests.get(base_url + str(page) + ".html", 
                     headers = {'User-agent': 'Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "propertyRow"})
    
    for item in all:
        d = {}
        adresses = item.find_all("span", {"class": "propAddressCollapse"})
        try: d["Adress"] = adresses[0].text
        except: d["Adress"] = None
        try:d["Locality"] = adresses[1].text
        except: d["Locality"] = None
        try:d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
        except: d["Price"] = None
        try: d["Beds"] = item.find("span", {"class": "infoBed"}).find("b").text
        except: d["Beds"] = None
        try: d["Area"] = item.find("span", {"class": "infoSqFt"}).find("b").text
        except: d["Area"] = None
        try: d["Baths"] = item.find("span", {"class": "infoValueFullBath"}).find("b").text
        except: d["Baths"] = None
        try: d["Half Baths"] = item.find("span", {"class": "infoValueHalfBath"}).find("b").text
        except: d["Half Baths"] = None
        for column_group in item.find_all("div", {"class": "columnGroup"}):
            if "Lot Size" in column_group.text:
                 d["Lot Size"] = column_group.find("span", {"class": "featureName"}).text
        l.append(d)
df = pandas.DataFrame(l)
df.to_csv("output.csv")
