#Membuat program dengan fungsi numerik
print("Suatu ketika, ada sebuah geng yang terdiri dari 5 orang sahabat yang ingin mengadakan.")
print("Mereka ingin berkumpul di rumah salah satu anggota setelah pulang sekolah.")
print("Program ini diciptakan untuk membantu mereka menemukan tempat yang pas untuk berkumpul.")
Data = []
banyak = 5
print("\n")
for data in range(0, banyak):
    print("Masukkan jarak rumah-sekolah tiap anggota dalam satuan meter")
    Jarak = int(input("Jarak rumah-sekolah anggota ke-%d : " % (data + 1)))
    Data.append(Jarak)
    print(" ")
import math
#Rata-rata jarak rumah-sekolah seluruh anggota
jumlah = sum(Data)
Ratarata = float(jumlah/banyak)
print("Jarak rata rata rumah anggota geng tersebut adalah", round(Ratarata, 2), "meter")
print("\n", "="*50)

#Data anggota dengan jarak rumah terdekat dengan sekolah
print("Jarak terdekat diraih oleh anggota dengan jarak rumah %d" % min(Data), "meter")
print("\n", "="*50)

#Data anggota dengan jarak rumah terjauh dengan sekolah
print("Jarak terjauh diraih oleh anggota dengan jarak  %d" % max(Data), "meter")
print("\n", "="*50)

#menghitung waktu menuju rumah yang terdekat
print("Diketahui kecepatan rata-rata kendaraan mereka adalah 10 m/s")
V = 10
waktu = min(Data)/V
print("Maka waktu yang dibutuhkan untuk mencapai rumah terdekat adalah", round(waktu, 2), "sekon")
