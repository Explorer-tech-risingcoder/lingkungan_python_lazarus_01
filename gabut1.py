
def user():
    print("ketik nama anda")
    pengguna = input("> ")
    

#gw mau buat kalo pengguna ngetik simbol aneh aneh nanti ada sesuatu kondisi

    if pengguna.strip() == "": # strip itu cuma buat menghapus spasi kosong e
        print("\n")
        print("[!] input kosong, silahkan coba lagi")
    
    elif pengguna.isalpha() : #
        print(pengguna)
        print(f"{pengguna.isalpha()}")
    else:
        print(f"{pengguna.isalpha()}")
user()

#testing kode
#pengguna = "furqon".isalpha()
#print(f"{pengguna}")
