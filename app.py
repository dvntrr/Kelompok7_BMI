from module import *
from data import *

def user_input() :
    berat = int(input("\nHow much do you weigh? (kg) : "))
    tinggi = int(input("How tall are you? (cm) : "))
    return berat, tinggi

def main() :
    while True :
        menu()
        pilihan = input("\nSelect an option (1/2/3/4): ")

        if pilihan == '1' :
            berat, tinggi = user_input()
            bmi = hitung_bmi(berat,tinggi)
            kategori, pesan = tentukan_kategori(bmi)
            
            tampilkan_hasil(bmi,pesan)
            tampilkan_saran(kategori)
            kembali_ke_menu()

            riwayat = buat_data(berat, tinggi, bmi, kategori)
            
            data_riwayat.append(riwayat)

        elif pilihan == '2' :
            tampilkan_riwayat()
            kembali_ke_menu()

        elif pilihan == '4' :
            print("Goodbye!")
            break

        else :
            print("Wrong Input! Please select a number 1-4")

if __name__ == "__main__":
    main()
