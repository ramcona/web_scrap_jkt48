from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json
import re

lists = []

url = "https://jkt48.com/calendar/list?lang=id"
bs = BeautifulSoup(requests.get(url).text,  "html.parser")

table_body = bs.find("tbody")
rows = table_body.find_all("tr")

#date id
bulan_tahun = bs.find("div", class_ = "entry-schedule__header--center").text.strip()
print("bulan_tahun: " + bulan_tahun)

size = len(rows)
x= 0
    
while x<size:
    model = {}
    model['bulan_tahun'] = bulan_tahun
    # print(rows[x])
    list_td = rows[x].find_all('td')

    #find tanggal & dari
    tanggal_mentah = list_td[0].find('h3').text

    #extra tanggal & hari
    tanggal_rplc = tanggal_mentah.replace(')', '')
    tanggal_spl = tanggal_rplc.split('(')
    
    #get tanggal
    if len(tanggal_spl) > 0:
        tanggal = tanggal_spl[0]
        print('tanggal ' + tanggal)
        
        #add tanggal to model
        model['tanggal'] = tanggal

    #get hari
    if len(tanggal_spl) >= 1:
        hari = tanggal_spl[1]
        print('hari ' + hari)

        #add hari to model
        model['hari'] = tanggal

    
    #find event
    list_event = list_td[1].find_all('div')
    size_of_event = len(list_event)
    position_event = 0

    #still find event
    while position_event < size_of_event:

        #get event / extraxing event
        event = list_event[position_event]

        #find badge
        badge_span = event.find('span')
        badge_img = badge_span.find('img')
        if badge_img.has_attr('src'):
            #yes you got badge
            print(badge_img['src'])

            #add badge to model
            model['badge_url'] = badge_img['src']

        #find event name
        event_name_full = event.find('p').text.strip()
        event_name = event_name_full[6:]
        print('event name :' + event_name)

        #add event_name to model
        model['event_name'] = event_name

        event_jam = event_name_full[0:5]
        print('waktu event : ' + event_jam)

        #add event_time to model
        model['event_time'] = event_jam

        #find id event
        url_event_full = event.find('a', href=True)['href']
        url_event_full_rplc = url_event_full.replace('?lang=id', '')
        url_event_full_rplc_2 = url_event_full_rplc.replace('/theater/schedule/id/', '')
        # detail_url_event = url_event_full['href']
        print(url_event_full_rplc_2)

        #add event_id to model
        model['event_id'] = url_event_full_rplc_2
        model['have_event'] = True

        #append model to list
        lists.append(model)

        position_event += 1
        #end of finding event

    #check if not have envet & add default value
    if size_of_event == 0:
        model['have_event'] = False

        #append model to list
        lists.append(model)
        

    x += 1