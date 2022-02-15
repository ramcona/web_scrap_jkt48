from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

list = []

url = "https://jkt48.com/theater/song-list/id/1?lang=id"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

div_main  = bs.find("div", class_ = "col-lg-9 order-1 order-lg-2 entry-contents__main-area")

#find kategori biodata
list_div_setlist = div_main.find_all('div', class_ = "entry-news__list")
size_of_list_setlist= len(list_div_setlist)
position_of_setlist = 0

while position_of_setlist < size_of_list_setlist:
    model = {}
    setlist = list_div_setlist[position_of_setlist]

    name = setlist.find('a').text
    model['nama'] = name

    url_setlist_full = setlist.find('a', href=True)['href']
    url_setlist_full_rplc = url_setlist_full.replace('?lang=id', '')
    url_setlist_full_rplc_2 = url_setlist_full_rplc.replace('/theater/song/id/', '')
    model['id'] = url_setlist_full_rplc_2

    list.append(model)
    position_of_setlist += 1



print(json.dumps(list))