import datetime
from data import *

def user_input():
    while True:
        try:
            berat = float(input("\nHow much do you weigh? (kg): "))
            tinggi = float(input("How tall are you? (cm): "))

            if berat <= 0 or tinggi <= 0:
                print("Weight and height must be greater than 0.")
                continue

            return berat, tinggi

        except ValueError:
            print("Invalid input. Please enter numbers only.")

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
    print("\n-+-+-+-MAIN MENU-+-+-+-")
    print("1. Calculate BMI")
    print("2. View BMI History")
    print("3. Remove BMI History")
    print("4. Health Guidance")
    print("5. Exit")

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
        print(f"{data_saran[2]}")
        return

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
        
def hapus_riwayat(data_riwayat) :
    hapus = input("Are You sure You want to remove last data? (Y/N)").upper()
    if hapus == 'Y' :
        if not data_riwayat :
            print("History is empty")
        data_riwayat.pop()
        print("Your last data has been removed")
    elif hapus == 'N':
        print("Remove history canceled")
    else:
        print("Invalid input. Please enter Y or N")
    kembali_ke_menu()

def pilih_panduan() :
    print("\n-+-+-+-HEALTH GUIDANCE-+-+-+-")
    print("1. Select Goal")
    print("2. Check Weekly Plans")
    pilihan = input("Choose what you want to do (1/2) : ")
    if pilihan == '1' :
        pilih_goal()
    elif pilihan == '2' :
        print("Not supported yet")
    else :
        print("Invalid input. Please enter 1 or 2")
    return


def pilih_goal() :
    print("\n-+-+-+-SELECT YOUR GOAL-+-+-+-")
    print("1. Gain Weight")
    print("2. Maintain Weight")
    print("3. Lose Weight")
    print("4. Build Muscle")
    pilihan = input("Choose a goal (1-4) : ")

    if pilihan == '1':
        print("\nOur Suggestions : ")
        for tip in data_tips[0]:
            print("-", tip)
        kembali_ke_menu()
        return data_saran[0]
    elif pilihan == '2':
        print("\nOur Suggestions : ")
        for tip in data_tips[1]:
            print("-", tip)
        kembali_ke_menu()
        return data_saran[1]
    elif pilihan == '3':
        print("\nOur Suggestions : ")
        for tip in data_tips[2]:
            print("-", tip)
        kembali_ke_menu()
        return data_saran[2]
    elif pilihan == '4':
        print("\nOur Suggestions : ")
        for tip in data_tips[2]:
            print("-", tip)
        kembali_ke_menu()
        return data_saran[2]
    else:
        print("Invalid input. Please choose a number between 1-4")
    kembali_ke_menu()

def kembali_ke_menu() :
    input("\nPress ENTER to go back to menu")
    return

def buat_data(berat, tinggi, bmi, kategori):
    waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return [berat, tinggi, bmi, kategori, waktu]