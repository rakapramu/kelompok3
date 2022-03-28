from pickle import TRUE


angka_1 = (input("Masukkan nilai : "))
angka_2 = input("Masukka nilai : ")
pilih = input("pilih +, /, -, * : ")

while TRUE:
    if pilih == '+' :
        jumlah = int(angka_1) + int(angka_2)
        print("hasilnya adalah ", jumlah)
    elif pilih == '-' :
        jumlah = int(angka_1) - int(angka_2)
        print("hasilnya adalah ", jumlah)
    elif pilih == '/' :
        jumlah = int(angka_1) / int(angka_2)
        print("hasilnya adalah ", jumlah)
    elif pilih == '*' :
        jumlah = int(angka_1) * int(angka_2)
        print("hasilnya adalah ", jumlah)

    isLanjut = input("Lanjut ? (y/n) : ")

    if isLanjut == 'n' :
        break
    else :
        continue
print('Program Selesai')