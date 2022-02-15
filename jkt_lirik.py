from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

data = {}

url = "https://jkt48.com/theater/song/id/70?lang=id"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

div_main  = bs.find("div", class_ = "col-lg-9 order-1 order-lg-2 entry-contents__main-area")


div_lirik = div_main.find('div', class_ = "entry-news__detail").find('div').text
data['lirik'] = div_lirik
# print(div_lirik)

print(json.dumps(data))