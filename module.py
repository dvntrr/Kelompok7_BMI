import datetime
from data import *

def hitung_bmi(berat,tinggi) :
    tinggi_m = tinggi/100
    bmi = berat/(tinggi_m**2)
    return bmi

def tentukan_kategori(bmi) :
    if bmi < 18.5 :
        return data_kategori[0], data_pesan[0]
    if bmi < 25 :
        return data_kategori[1], data_pesan[1]
    if bmi < 30 :
        return data_kategori[2], data_pesan[2]
    else :
        return data_kategori[3], data_pesan[3]
    
    
def buat_data(berat, tinggi, bmi, kategori):
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
    return [berat, tinggi, bmi, kategori, waktu]