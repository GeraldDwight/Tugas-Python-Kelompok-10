import math

print("Selamat datang di Aplikasi Memecahkan Rumus Matematika")
print("Pilih salah satu bentuk :")
print("1. Bentuk Bola")
print("2. Bentuk Kubus")
print("3. Bentuk Balok")
print("4. Keluar")

Pilihan = int(input("Masukkan pilihan bentuk (1-4) : "))

while Pilihan != 4:
    if Pilihan == 1:
        print("1. Rumus Keliling")
        print("2. Rumus Luas")
        print("3. Rumus Volume")
        pilihan_rumus = int(input("Masukkan pilihan rumus (1-3) : "))
        if pilihan_rumus == 1:
            def keliling_bola():
                Keliling_Bola = 2 * math.pi * r
                return Keliling_Bola
            r = float(input("Masukkan jari-jari : "))
            print("Rumus Keliling Bola")
            print("2 * 3,14 *", r)
            Keliling = keliling_bola()
            print("Keliling bola adalah : ", Keliling)
        elif pilihan_rumus == 2:
            def luas_bola():
                Luas_Bola = 4 * math.pi * r**2
                return Luas_Bola
            r = float(input("Masukkan Jari - jari : "))
            print("Rumus Luas Bola")
            print("4 * 3,14 *", r)
            Luas = luas_bola()
            print("Luas bola adalah : ", Luas)
        elif pilihan_rumus == 3:
            def volume_bola():
                Volume_Bola = 4/3 * math.pi * r**3
                return Volume_Bola
            r = float(input("Masukkan Jari - jari : "))
            print("Rumus Volume Bola")
            print("4/3 * 3,14 *", r)
            Volume = volume_bola()
            print("Volume bola adalah : ", Volume)
        else:
            print("Pilihan tidak valid, silahkan coba lagi.")
    elif Pilihan == 2:
        print("1. Rumus Keliling")
        print("2. Rumus Luas")
        print("3. Rumus Volume")
        pilihan_rumus = int(input("Masukkan pilihan rumus (1-3) : "))
        if pilihan_rumus == 1:
            def keliling_kubus():
                Keliling_Kubus = 4 * s
                return Keliling_Kubus
            s = float(input("Masukkan sisi kubus : "))
            print("Rumus Keliling Kubus")
            print("4 *", s)
            Keliling = keliling_kubus()
            print("Keliling kubus adalah : ", Keliling)
        elif pilihan_rumus == 2:        
            def luas_kubus():
                Luas_Permukaan_Kubus = 6 * s**2
                return Luas_Permukaan_Kubus
            s = float(input("Masukkan sisi kubus : "))
            print("Rumus Luas Kubus")
            print("6 *", s)
            Luas = luas_kubus()
            print("Luas kubus adalah : ", Luas)
        elif pilihan_rumus == 3:
            def volume_kubus():
                Volume_Kubus = s * s * s
                return Volume_Kubus
            s = float(input("Masukkan sisi kubus : "))
            print("Rumus Volume Kubus")
            print(s, "*", s ,"*" ,s)
            Volume = volume_kubus()
            print("Volume Kubus adalah : ", Volume)
        else:
            print("Pilihan tidak valid, silahkan coba lagi.")
    elif Pilihan == 3:
        print("1. Rumus Keliling")
        print("2. Rumus Luas")
        print("3. Rumus Volume")
        pilihan_rumus = int(input("Masukkan pilihan rumus (1-3) : "))
        if pilihan_rumus == 1:
            def keliling_balok():
                Keliling_Balok = 2 * (p + l + t)
                return Keliling_Balok
            p = float(input("Masukkan Panjang balok : "))
            l = float(input("Masukkan Lebar balok : "))
            t = float(input("Masukkan Tinggi balok : "))
            print("Rumus Keliling Balok")
            print("2 *", p ,"+", l ,"+", t)
            Keliling = keliling_balok()
            print("Keliling balok adalah:", Keliling)
        elif pilihan_rumus == 2:
            def luas_balok():
                Luas_Balok = 2 * (p * l) + (p * t) + (l * t)
                return Luas_Balok
            p = float(input("Masukkan Panjang balok : "))
            l = float(input("Masukkan Lebar balok : "))
            t = float(input("Masukkan Tinggi balok : "))
            print("Rumus Luas Balok")
            print("2 * (", p, "*", l ,") + (", p, "*", t ,") + (", l, "*", t ,")")
            Luas = luas_balok()
            print("Luas balok adalah:", Luas)
        elif pilihan_rumus == 3:
            def volume_balok():
                Volume_Balok = p * l * t
                return Volume_Balok
            p = int(input("Masukkan Panjang balok : "))
            l = int(input("Masukkan Lebar balok : "))
            t = int(input("Masukkan Tinggi balok : "))
            print("Rumus Volume Balok")
            print(p ,"*", l ,"*", t)
            Volume = volume_balok()
            print("Volume Balok adalah = ", Volume)
        else:
            print("Pilihan tidak valid, silahkan coba lagi.")
    ulangi = input("Apakah Anda ingin kembali ke Aplikasi? (iya/tidak): ")
    if ulangi.lower() == 'tidak':
        break
    else:
        print()
        print("Selamat datang di Aplikasi Memecahkan Rumus Matematika")
        print("Pilih salah satu bentuk :")
        print("1. Bentuk Bola")
        print("2. Bentuk Kubus")
        print("3. Bentuk Balok")
        print("4. Keluar")
        Pilihan = int(input("Masukkan pilihan bentuk (1-4) : "))