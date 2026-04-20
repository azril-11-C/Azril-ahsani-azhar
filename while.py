# kondisi
# aksi

nama_anda = "azriel"
input_nama = input("Masukkan nama anda: ")

if input_nama == nama_anda:

    print("Jika benar akan lanjut ke program selanjutnya")

    try:
        angka = int(input("masukkan angka"))

        for i in range(1, 20):
            print(f"{angka} x {i} = {angka* i}")

    except ValueError:
        pass 
    print("program selesai")
else:
    print("silahkan coba lagi")


