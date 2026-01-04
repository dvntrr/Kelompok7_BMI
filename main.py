from module import tentukan_kategori, hitung_bmi

def user_input() :
    berat = int(input("How much do you weigh? (kg) : "))
    tinggi = int(input("How tall are you? (cm) : "))
    return berat, tinggi

def tampilkan_hasil(bmi, pesan):
    print(f"\nYour BMI :            {bmi:.2f}")
    print(f"{pesan}")

def main() :
    while True :
        print("\nMAIN MENU")
        print("1. Calculate BMI")
        print("2. View BMI History")
        print("3. Health Guidance")
        print("4. Exit")
        pilihan = input("Select an option (1/2/3/4): ")

        if pilihan == '1' :
            berat, tinggi = user_input()
            bmi = hitung_bmi(berat,tinggi)
            kategori, pesan = tentukan_kategori(bmi)
            tampilkan_hasil(bmi,pesan)

        elif pilihan == '4' :
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
