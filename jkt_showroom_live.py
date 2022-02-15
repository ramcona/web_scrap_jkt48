from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

list = []

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}


url = "https://www.showroom-live.com/room/search?genre_id=102&keyword=jkt48"
bs = BeautifulSoup(requests.get(url, headers=header).text,  "html.parser")


list_showroom = bs.find_all('li', class_ = "search_res_li genre_id_102")

size_of_list_showroom = len(list_showroom)
position_of_showroom = 0

# svg icon-camera-gray is-active //active showroom

while position_of_showroom < size_of_list_showroom:
    model = {}
    div_all = list_showroom[position_of_showroom]
    card_info_all = div_all.find("div", class_ = "listcardinfo")

    # get image
    card_image = card_info_all.find("div", class_ = "listcardinfo-image")
    image = card_image.find("img", class_ = "img-main")['data-src']
    model['ava'] = image

    #  get menu showroom
    card_info = card_info_all.find("div", class_ = "listcardinfo-info")
    nama_full = card_info.find("h4", class_ = "listcardinfo-main-text").text
    nama = nama_full.split('/')
    model['nama'] = nama[0]

    sub_info_full = card_info.find("p", class_ = "listcardinfo-sub-text").text
    nama_lengkap_mentah = sub_info_full.split('\n')[1]
    nama_lengkap_rplc = nama_lengkap_mentah.replace('"Name: ', '')
    nama_lengkap_splt = nama_lengkap_rplc.split('/')
    model['nama_lengkap'] = nama_lengkap_splt[0] 

    #  get menu showroom
    card_menu = card_info_all.find("div", class_ = "listcardinfo-menu")
    check_active = card_menu.find("span", class_ = "svg icon-camera-gray is-active")

    if check_active == None:
        model['active'] = 0
    else :
        model['active'] = 1

    list.append(model)

    position_of_showroom += 1


print(json.dumps(list))