import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/",
                headers = {'User-agent': 'Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

l = []
for item in soup.find_all("div", {"class": "propertyRow"}):
    d = {}
    adresses = item.find_all("span", {"class": "propAddressCollapse"})
    d["Adress"] = adresses[0].text
    d["Locality"] = adresses[1].text
    d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")

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
