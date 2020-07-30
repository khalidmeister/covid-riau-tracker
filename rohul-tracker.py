import re
import requests
import csv
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup

with open('rohul.csv', 'a+') as csv_files:
    tr_kecamatan = soup.find_all('tr')[2:]
    fieldnames = ['tanggal', 'Kecamatan', '(ODP) Proses Pemantauan', '(ODP) Selesai Pemantauan', '(PDP) Masih Dirawat', 
                  '(PDP) Pulang dan Sehat', '(Positif) Dirawat', '(Positif) Sembuh', '(Positif) Meninggal']
    writer = csv.DictWriter(csv_files, fieldnames=fieldnames)
    # Ekstraksi per kecamatan
    writer.writeheader()
    for tr in tr_kecamatan:
        temp = {}
        temp['tanggal'] = date.today()
        c = 1
        # Ekstraksi per kolom
        for td in tr.find_all('td')[1:]:
            td = td.text
            temp[fieldnames[c]] = td
            c += 1
        writer.writerow(temp)