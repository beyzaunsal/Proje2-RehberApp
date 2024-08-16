#hata yakalama 
try:
    f=open("dosya3.py","r")
    print(f.read())
except:
    print("İşlem başarısız")


#çok dosya oluşturma
for a in range(100):                #100 tane birden dosya oluşturur.
    dosya=open(f"deneme{a}.txt","w")


