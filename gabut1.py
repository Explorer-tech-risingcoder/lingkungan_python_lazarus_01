
def user():
    print("ketik nama anda")
    pengguna = input("> ")
    

#gw mau buat kalo pengguna ngetik simbol aneh aneh nanti ada sesuatu kondisi

    if pengguna == "":
        print("\n")
        print("[!] input kosong, silahkan coba lagi")
    else:
        print(f"halo, {pengguna}")
user()
