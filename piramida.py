jumlahBalok = int(input("Jumlah Balok:"))

balokSekarang = 0
tinggi = 0

while(1):
    balokSekarang = balokSekarang + 1
    if(jumlahBalok<balokSekarang):
        break
    jumlahBalok = jumlahBalok - balokSekarang
    tinggi = tinggi + 1





print("Tinggi Piramida:",tinggi)

