dosyaadi="rehber.txt"
aktifMenü=1

def menu():
    global aktifMenü
    print("╔"+"════════════════════════════════"+"╗")
    print("║           REHBER APP           ║")
    print("║  >> 1- İsim Ekle  <<           ║" if aktifMenü==1 else "║ 1- İsim Ekle                   ║") 
    print("║  >> 2- Kayıtları Listele  <<   ║" if aktifMenü==2 else "║ 2- Kayıtları listele           ║" )
    print("║  >> 3- Kayıt Düzelt  <<        ║" if aktifMenü==3 else "║ 3- Kayııt Düzelt               ║" )
    print("║  >> 4- Kayıt sil  <<           ║" if aktifMenü==4 else "║ 4- Kayıt sil                   ║")
    print("║                                ║")
    print("║        Seçiminiz nedir?        ║")
    print("╚"+"════════════════════════════════"+"╝")

    tus=input(f"{aktifMenü} A=aşağı/ Y=Yukarı/ S=SEÇ").upper()
    if tus == "A":aktifMenü +=1
    if tus == "Y": aktifMenü -=1
    if tus== "S": 
        if aktifMenü==1: kisiEkle()
        if aktifMenü==2: listele()
        if aktifMenü==3: degistir()



    if aktifMenü>4 : aktifMenü=1
    if aktifMenü<1 :aktifMenü=4
    menu()
def kisiEkle():
    d= open(dosyaadi, "a", encoding="utf-8") 
    ad=input("\nKişi Adı ve Soyadı:")
    no=input("\nNumarayı giriniz:")
    d.write(str({"Adı:":ad, "Numarası:":no})+",")
    d.close()
    
f listele():
    ddd de= open(dosyaadi,encoding="utf-8") 
    print("\n\n KİŞİLER LİSTESİ:\n===============")
    ddd.read()
    okunan = ddd.readlines()
    okunan.split(",")
    for b in okunan:
        print(b)
listele()        
   
  
menu()   

# import os 
# def kayitlarListele():
#     kayitlist =os.listdir()   
#     for dosya in kayitlist:
#         if dosya.endswith("rehber.txt"):
#     print(dosya)
# menu()        