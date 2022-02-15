from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

data = {}

url = "https://jkt48.com/member/detail/id/237?lang=id"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

div_main  = bs.find("div", class_ = "entry-mypage")

#find kategori biodata
list_div_biodata = div_main.find_all('div', class_ = "entry-mypage__item")
size_of_div_biodata = len(list_div_biodata)
position_of_div_biodata = 0

while position_of_div_biodata < size_of_div_biodata:
    div_biodata = list_div_biodata[position_of_div_biodata]

    subject = div_biodata.find('div', class_ = "entry-mypage__item--subject").text.strip()
    value = div_biodata.find('div', class_ = "entry-mypage__item--content").text.strip()

    if subject == "Nama":
        data['nama'] = value
    if subject == "Tanggal Lahir":
        data['tgl_lahir'] = value
    if subject == "Golongan Darah":
        data['gol_darah'] = value
    if subject == "Horoskop":
        data['horoskop'] = value
    if subject == "Tinggi Badan":
        data['tinggi'] = value
    if subject == "Nama Panggilan":
        data['nama_panggilan'] = value
    position_of_div_biodata += 1




print(json.dumps(data))