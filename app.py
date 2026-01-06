from module import *
from data import *

def main() :
    while True :
        menu()
        pilihan = input("\nSelect an option (1/2/3/4/5): ")

        if pilihan == '1' :
            berat, tinggi = user_input()
            bmi = hitung_bmi(berat,tinggi)
            kategori, pesan, saran_terpilih = tentukan_kategori(bmi)
            
            tampilkan_hasil(bmi,pesan)
            tampilkan_saran(saran_terpilih)

            riwayat = buat_data(berat, tinggi, bmi, kategori, saran_terpilih)
            
            data_riwayat.append(riwayat)
            kembali_ke_menu()

        elif pilihan == '2' :
            tampilkan_riwayat()
            kembali_ke_menu()

        elif pilihan == '3' :
            hapus_riwayat(data_riwayat)
            kembali_ke_menu()

        elif pilihan == '4' :
            pilih_panduan(saran_terpilih)
            kembali_ke_menu()

        elif pilihan == '5' :
            print("Goodbye!")
            break

        else :
            print("Invalid input. Please choose a number between 1-5")

if __name__ == "__main__":
    main()
