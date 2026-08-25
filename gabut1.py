

def user():
    

    #gw mau buat kalo pengguna ngetik simbol aneh aneh nanti ada sesuatu kondisi
    while True:
        print("ketik nama anda")
        pengguna = input("> ") 
        if pengguna.strip() == "" : # strip itu cuma buat menghapus spasi kosong 
            print("\n")
            print("[!] input kosong, silahkan coba lagi")
        
        elif pengguna.isalpha() : #
            print(f"halo, {pengguna}")
            print(f"kondisi {pengguna.isalpha()}")
        else:
            print(f"{pengguna.isalpha()}")
            #break
user()

#testing kode
#pengguna = "furqon".isalpha()
#print(f"{pengguna}")

# penggunaan cara kerja strip() bukan stript() yaa,

# >>> "muhammad furqon".strip()
# 'muhammad furqon'
# >>> " muham mmad fu rqon".strip()
# 'muham mmad fu rqon'
# >>> "     muhammad furqon  ".strip()
# 'muhammad furqon'
# >>> 
#


#simbol ini == artinya perbandingan misal 'p' == 'p' output True kalo p nya sebelah berbeda maka False 
# >>> "p" == "p"
# True
# >>> "p" == "P"
# False
# >>> 
