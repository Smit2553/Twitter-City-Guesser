import requests
from bs4 import BeautifulSoup


def get_city():
    url = "https://randomcity.net/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs={'class': 'text-center text-2xl font-bold text-purple-900'})
    citylist = []
    for row in table:
        citylist.append(str(row.text).strip().replace(",", ""))
    citylist.pop(0)
    return citylist
