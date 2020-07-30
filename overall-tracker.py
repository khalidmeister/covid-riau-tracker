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
print("Isolasi / Sedang Dirawat:", angka[0] + angka[1])
print("Sembuh:", angka[2])
print("Meninggal:", angka[3])
print("Total:", angka[0] + angka[1] + angka[2] + angka[3])

# Membuat dan Mengupdate Dataset
with open('riau-dataset.csv', 'a+') as csv_file:
    fieldnames = ['tanggal', '(Spesimen) Total Yang Diperiksa', '(Spesimen) Jumlah Orang Yang Diperiksa', '(Suspek) Isolasi Mandiri', '(Suspek) Isolasi di RS', '(Suspek) Sembuh', '(Suspek) Meninggal', '(Positif) Isolasi Mandiri', '(Positif) Isolasi di RS', '(Positif) Sembuh', '(Positif) Meninggal']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    c = 1
    temp = {}
    writer.writeheader()
    for tabel in soup.find_all('table'):
        temp['tanggal'] = date.today()
        for data in tabel.find_all('td'):
            data = data.text
            data = re.sub("\.", "", data)
            temp[fieldnames[c]] = data
            c += 1
    writer.writerow(temp)