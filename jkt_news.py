from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

data = {}


url = "https://jkt48.com/news/list?lang=id"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

list_berita_mentah  = bs.find_all("div", class_ = "entry-news__list")
data_list_berita = []
size_of_berita = len(list_berita_mentah)
position_berita = 0

while position_berita < size_of_berita:
    model = {}
    berita_mentah = list_berita_mentah[position_berita]

    #get badge  / kategori
    badge_div = berita_mentah.find("div", class_ = "entry-news__list--label")
    badge_img = badge_div.find('img')
    if badge_img.has_attr('src'):
        #yes you got badge
        # print(badge_img['src'])

        #add badge to model
        model['badge_url'] = badge_img['src']

    #get title and date
    title_div = berita_mentah.find("div", class_ = "entry-news__list--item")
    
    #get waktu
    waktu = title_div.find('time').text
    model['waktu'] = waktu

    #get judul
    judul = title_div.find('h3').text
    model['judul'] = judul

    #get berita id
    #extacing src
    url_berita_full = title_div.find('h3').find('a', href=True)['href']
    url_berita_full_rplc = url_berita_full.replace('?lang=id', '')
    url_berita_full_rplc_2 = url_berita_full_rplc.replace('/news/detail/id/', '')
    # detail_url_event = url_berita_full['href']
    # print(url_berita_full_rplc_2)
    model['berita_id'] = url_berita_full_rplc_2


    data_list_berita.append(model)
    position_berita += 1

data['berita'] = data_list_berita


print(json.dumps(data))