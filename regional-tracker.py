import csv
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

r = requests.get('https://covid19.riau.go.id/pantauan_data_kasus')
soup = BeautifulSoup(r.content, 'html.parser')

# Menampilkan Status Tiap Kota/Kabupaten
print("Kasus COVID-19 di Provinsi Riau Per Tanggal", date.today())
for kota in soup.tbody.find_all('tr'):
    data = kota.find_all('td')
    print(data[0].text)
    print("Isolasi Mandiri", data[-4].text)
    print("Isolasi di RS", data[-3].text)
    print("Sembuh", data[-2].text)
    print("Meninggal", data[-1].text)
    print()

# Menyimpan ke dalam format .csv
with open('regional-dataset.csv', 'a+') as csv_file:
    fieldnames = ['tanggal', 'wilayah', '(Spesimen) Total Yang Diperiksa', '(Spesimen) Jumlah Orang Yang Diperiksa', '(Spesimen) Positif', '(Suspek) Isolasi Mandiri', '(Suspek) Isolasi di RS', '(Suspek) Sembuh', '(Suspek) Meninggal', '(Positif) Isolasi Mandiri', '(Positif) Isolasi di RS', '(Positif) Sembuh', '(Positif) Meninggal']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    for kota in soup.tbody.find_all('tr'):
        temp = {}
        c = 1
        temp['tanggal'] = date.today()
        for data in kota.find_all('td'):
            data = data.text
            data = re.sub("\.", "", data)
            temp[fieldnames[c]] = data
            c += 1
        writer.writerow(temp)
