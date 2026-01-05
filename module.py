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
    
def menu() :
    print("MAIN MENU")
    print("1. Calculate BMI")
    print("2. View BMI History")
    print("3. Health Guidance")
    print("4. Exit")
    
def tampilkan_riwayat() :
    if not data_riwayat :
        print("History Not Found!")
        return
    
    for i,data in enumerate(data_riwayat, start=1) :
        print(f"\nData Ke-{i}")
        print(f"Weight   : {data[0]}")
        print(f"Height   : {data[1]}")
        print(f"BMI      : {data[2]:.2f}")
        print(f"Category : {data[3]}")
        print(f"Time     : {data[4]}")

def tampilkan_hasil(bmi, pesan):
    print(f"\nYour BMI Score :      {bmi:.2f}")
    print(f"{pesan}")

def tampilkan_saran(kategori):
            print(f"\nOur Recommendations for You : ")
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

def kembali_ke_menu() :
    input("\nPress ENTER to go back to menu")
    return

def input_saran() :
     data_saran

def buat_data(berat, tinggi, bmi, kategori):
    waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return [berat, tinggi, bmi, kategori, waktu]