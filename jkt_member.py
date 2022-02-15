from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

data = {}

url = "https://jkt48.com/member/list?lang=id"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

div_main  = bs.find("div", class_ = "col-lg-9 order-1 order-lg-2 entry-contents__main-area")

#find kategori
kategori_mentah = div_main.find_all('h2')
size_of_kategori = len(kategori_mentah)
position_of_kategori = 0
list_of_kategori = []

list_member = []

while position_of_kategori < size_of_kategori:
    kategori = kategori_mentah[position_of_kategori].text
    list_of_kategori.append(kategori)
    position_of_kategori += 1

#find kategori
root_member_all_mentah = div_main.find_all('div', class_ ="row row-all-10")
size_of_div_member = len(root_member_all_mentah)
position_of_div_member = 0
while position_of_div_member < size_of_kategori:

    list_div_member = root_member_all_mentah[position_of_div_member].find_all('div', class_ = "entry-member")
    size_of_member = len(list_div_member)
    position_of_member = 0

    #find member
    while position_of_member < size_of_member:
        model = {}
        member = list_div_member[position_of_member] 

        #get name member
        nama_member_mentah = member.find('p').find('a').text
        nama_member = re.sub(r"(\w)([A-Z])", r"\1 \2", nama_member_mentah)
        model['nama_member'] = nama_member

        #get id member
        url_member_full = member.find('a', href=True)['href']
        url_member_full_rplc = url_member_full.replace('?lang=id', '')
        url_member_full_rplc_2 = url_member_full_rplc.replace('/member/detail/id/', '')
        model['id_member'] = nama_member

        #get nama member
        ava_member_mentah = member.find('a').find('img')
        if ava_member_mentah.has_attr('src'):
        #yes you got ava member
            ava_member = ava_member_mentah['src']
            model['ava_member'] = ava_member

        model['kategori'] = list_of_kategori[position_of_div_member]
        list_member.append(model)
        position_of_member += 1

            

    position_of_div_member += 1


data['member'] = list_member


print(json.dumps(data))