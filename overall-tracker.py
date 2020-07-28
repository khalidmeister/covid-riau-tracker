import requests
import re
import csv
from datetime import date
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://covid19.riau.go.id/webster')
soup = BeautifulSoup(r.content, 'html.parser')

# Menampilkan Kasus Positif COVID-19 di Riau
print('Rekapitulasi Kasus COVID-19 di Provinsi Riau Per Tanggal:', date.today())
angka = []
for data in soup.find_all('table')[2].find_all('td'):
    data = data.text
    data = int(data)
    angka.append(data)
print("Sedang Dirawat:", angka[0])
print("Sembuh:", angka[1])
print("Meninggal:", angka[2])
print("Total:", angka[0] + angka[1] + angka[2])

# Membuat dan Mengupdate Dataset
with open('overall-dataset.csv', 'a+') as csv_file:
    fieldnames = ['tanggal', '(ODP) Total', '(ODP) Selesai Pemantauan', '(PDP) Total', '(PDP) Sembuh', '(PDP) Meninggal', '(Positif) Dirawat', '(Positif) Sembuh', '(Positif) Meninggal']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    c = 1
    temp = {}
    # writer.writeheader()
    for tabel in soup.find_all('table'):
        temp['tanggal'] = date.today()
        for data in tabel.find_all('td'):
            data = data.text
            data = re.sub("\.", "", data)
            temp[fieldnames[c]] = data
            c += 1
    writer.writerow(temp)