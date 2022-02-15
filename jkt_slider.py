from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

data = {}

url = "https://jkt48.com/"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

div_main  = bs.find("section")
list_sliders_mentah = div_main.find_all('a')

size_of_slider = len(list_sliders_mentah)
position_of_slider = 0

list_slider = []
while position_of_slider < size_of_slider:
    model = {}
    slider_mentah = list_sliders_mentah[position_of_slider]

    model['value'] = slider_mentah['href']

    img = slider_mentah.find('img')
    if img.has_attr('src'):
        model['img_url'] = img['src']

    list_slider.append(model)
    position_of_slider += 1

# print(list_sliders_mentah)

# div_lirik = div_main.find('div', class_ = "entry-news__detail").find('div').text
# data['lirik'] = div_lirik
# print(div_lirik)

print(json.dumps(list_slider))