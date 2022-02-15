from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

data = {}


url = "https://jkt48.com/theater/schedule/id/2354?lang=id"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

table_body = bs.find_all("tbody")[1]
rows = table_body.find("tr")

size_of_tr = len(rows)

chill_td = rows.find_all('td')[2]

main_other_data = bs.find('div', class_ = "entry-mypage")
harga_tiket = main_other_data.find('p')
print(harga_tiket.text.strip)

#1. find member
list_member_tampil = chill_td.find_all('a',  {"target" : "member"})

#extraxing member tampil
data_member_tampil_final = []
size_of_member_tampil = len(list_member_tampil)
position_member_tampil = 0
while position_member_tampil < size_of_member_tampil:
    member = {}
    member_mentah = list_member_tampil[position_member_tampil]
    
    nama_member = member_mentah.text
    member['nama_member'] = nama_member
    # print('nama member : ' + nama_member)

    #find id member
    id_member_full = member_mentah['href']
    id_member_full_rplc = id_member_full.replace('?lang=id', '')
    id_member_full_rplc_2 = id_member_full_rplc.replace('/member/detail/id/', '')

    member['id_member'] = id_member_full_rplc_2
    # print('id member : ' + id_member_full_rplc_2)

    data_member_tampil_final.append(member)

    position_member_tampil += 1
data['tampil'] = data_member_tampil_final

#2. find birtday
list_member_bday = chill_td.find_all('a',  {"style" : "color:#616D9D"})
#extraxing member tampil
data_member_bday_final = []
size_of_member_bday = len(list_member_bday)
position_member_bday = 0

while position_member_bday < size_of_member_bday:
    member = {}
    member_mentah = list_member_bday[position_member_bday]
    
    nama_member = member_mentah.text
    member['nama_member'] = nama_member
    # print('nama member : ' + nama_member)

    #find id member
    id_member_full = member_mentah['href']
    id_member_full_rplc = id_member_full.replace('?lang=id', '')
    id_member_full_rplc_2 = id_member_full_rplc.replace('/member/detail/id/', '')

    member['id_member'] = id_member_full_rplc_2
    # print('id member : ' + id_member_full_rplc_2)

    data_member_bday_final.append(member)

    position_member_bday += 1

data['bday'] = data_member_bday_final


# print(json.dumps(data))