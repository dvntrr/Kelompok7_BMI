import datetime
from data import *

def menu() :
    print("\n-+-+-+-MAIN MENU-+-+-+-")
    print("1. Calculate BMI")
    print("2. View BMI History")
    print("3. Remove BMI History")
    print("4. Health Guidance")
    print("5. Exit")
    
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
        return data_kategori[0], data_pesan[0], data_saran[0]
    elif bmi < 25 :
        return data_kategori[1], data_pesan[1],data_saran[1]
    elif bmi < 30 :
        return data_kategori[2], data_pesan[2],data_saran[2]
    else :
        return data_kategori[3], data_pesan[3],data_saran[2]

def tampilkan_hasil(bmi, pesan):
    print(f"\nYour BMI Score :      {bmi:.2f}")
    print(f"{pesan}")

def tampilkan_saran(saran_terpilih):
    print(f"\nOur Recommendations for You : {saran_terpilih}")

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

def tampilkan_rencana(saran_terpilih) :
    print("\n-+-+-+-WEEKLY PLAN-+-+-+")
    if saran_terpilih not in rencana_mingguan:
        print("No weekly plan available.")
        return

    for plan in rencana_mingguan[saran_terpilih]:
        print(plan)
        
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

def pilih_panduan(saran_terpilih) :
    print("\n-+-+-+-HEALTH GUIDANCE-+-+-+-")
    print("1. Select Goal")
    print("2. Check Weekly Plans")
    pilihan = input("\nChoose what you want to do (1/2) : ")
    if pilihan == '1' :
        pilih_saran()
    elif pilihan == '2' :
        tampilkan_rencana(saran_terpilih)
    else :
        print("Invalid input. Please enter 1 or 2")
    return

def pilih_saran() :
    while True :
        print("\n-+-+-+-SELECT YOUR GOAL-+-+-+-")
        print("1. Gain Weight")
        print("2. Maintain Weight")
        print("3. Lose Weight")
        print("4. Build Muscle")
        pilihan = input("Choose a new goal (1-4) : ")

        if pilihan == '1':
            saran_terpilih = data_saran[0]
            tips = data_tips[0]
            print(f"Goal has changed to {data_saran[0]}")
        elif pilihan == '2':
            saran_terpilih = data_saran[1]
            tips = data_tips[1]
            print(f"Goal has changed to {data_saran[1]}")
        elif pilihan == '3':
            saran_terpilih = data_saran[2]
            tips = data_tips[2]
            print(f"Goal has changed to {data_saran[2]}")
        elif pilihan == '4':
            saran_terpilih = data_saran[3]
            tips = data_tips[3]
            print(f"Goal has changed to {data_saran[3]}")
        else:
            print("Invalid input. Please choose a number between 1-4")
            continue
    
        print("\nOur Suggestions : ")
        for tip in tips :
            print(f"- {tip}")
    
        konfirmasi_rencana(saran_terpilih)
        return saran_terpilih

def konfirmasi_rencana(saran_terpilih) :
    pilihan = input(f"\nDo you want to check your weekly plan? (Y/N)").upper()
    if pilihan == 'Y' : 
        tampilkan_rencana(saran_terpilih)
    elif pilihan == 'N' :
        print("Don't worry, You can always check them later")


def kembali_ke_menu() :
    input("\nPress ENTER to go back to menu")
    return

def buat_data(berat, tinggi, bmi, kategori, saran_terpilih):
    waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return [berat, tinggi, bmi, kategori, waktu, saran_terpilih]