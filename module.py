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
    
def tampilkan_riwayat() :
    if not data_riwayat :
        print("History Not Found!")
        return
    print("\n=====================================")
    for i,data in enumerate(data_riwayat, start=1) :
        print(f"\nData Ke-{i}")
        print(f"Weight   : {data[0]}")
        print(f"Height   : {data[1]}")
        print(f"BMI      : {data[2]:.2f}")
        print(f"Category : {data[3]}")
        print(f"Time     : {data[4]}")
    print("\n=====================================")
def tampilkan_hasil(bmi, pesan):
    print(f"\nYour BMI :            {bmi:.2f}")
    print(f"{pesan}")

def tampilkan_saran(kategori):
            print(f"Our Recommendations for You : ")
            if kategori == "Underweight" :
                print(f"{data_saran[0]}")
                return
            elif kategori == "Normal" :
                print(f"{data_saran[1]}")
                return
            elif kategori == "Overweight" :
                print(f"{data_saran[2]}")
                return
            elif kategori == "Obese" :
                print(f"{data_saran[3]}")
                return

def buat_data(berat, tinggi, bmi, kategori):
    waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return [berat, tinggi, bmi, kategori, waktu]