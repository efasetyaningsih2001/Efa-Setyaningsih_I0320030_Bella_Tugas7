title = "program Konversi Teks"
title2 = title.upper()
border = ""
sapa = "~SELAMAT MENCOBA~"
print(border.center(68, "="))
print(title2.center(68))
print(border.center(68, "="))
print("     Hallo, program ini dirancang untuk memudahkan kalian dalam mengkonversi tulisan sesuai dengan perintah yang Anda inginkan. Anda bisa mengubah tulisan menjadi huruf kapital di awal kalimat, semua huruf besar dan semua huruf kecil.")
print(sapa.center(68))
#Data masuk
#menampilkan menu
def list_tulisan():
    print("\n--------------MAIN MENU---------------")
    print("1. Membuat huruf pertama menjadi kapital")
    print("2. Membuat huruf menjadi kapital semua")
    print("3. Membuat huruf menjadi kecil semua")
    print("4. Keluar dari program")
    print("--------------------------------------")
    text = int(input("Masukkan nomor : "))
    print("")

    if text == 1:
        one = input("Masukkan kata : ")
        print("Output: ", one.capitalize())
    elif text == 2:
        two = input("Masukkan kata : ")
        print("Output: ", two.upper())
    elif text == 3:
        three = input("Masukkan kata : ")
        print("Output: ", three.lower())
    elif text == 4:
        exit()
    else:
        pass
if __name__ == "__main__":
    while(True):
        list_tulisan()




