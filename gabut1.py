

def user():
    

    #gw mau buat kalo pengguna ngetik simbol aneh aneh nanti ada sesuatu kondisi
    while True:
        print("ketik nama anda")
        pengguna = input("> ") 
        if pengguna.strip() == "" : # strip itu cuma buat menghapus spasi kosong 
            print("\n")
            print("[!] input kosong, silahkan coba lagi")
        
        elif not pengguna.isalpha() : # misal not False dia bakal kesini kalo not true di bakal ke else programnya 
            print(f"variabel ini aslinya : {pengguna.isalpha()}") 
            print("ea")

        else:
            print(f"variabel ini aslinya : {pengguna.isalpha()}") 
            #break
            print("eaaaa")
user()
#
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
