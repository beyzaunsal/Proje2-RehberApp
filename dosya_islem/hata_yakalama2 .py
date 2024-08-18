#hata yakalama 
try:
    f=open("dosya3.py","r")
    print(f.read())
except:
    print("İşlem başarısız")


#çok dosya oluşturma
for a in range(100):                #100 tane birden dosya oluşturur.
    dosya=open(f"deneme{a}.txt","w")


#dosya listeleme
import os
print(os.listdir())      # mevcut konumdaki dosya/dizinlerin dizi olarak listesi.


#maddeler halinde listeleme
import os
xyz=os.listdir()           # mevcut konumdaki dosya/dizinlerin dizi olarak listesi.
for a in xyz:
    print(a)

# 1 - ['.git', 'dosya islem', 'Proje2', 'rehber.txt'] ----->>> dizi şeklinde (örnek)
# import os 
# dosyaDizinListesi = os.listdir()      # mevcut konumdaki dosya ve dizinlerin dizi olarak listesi.
# for x in range(len(dosyaDizinListesi)):
#     print(x+1,"-",dosyaDizinListesi)


# import os 
# kayitlist =os.listdir()   # python kod dosyasının bulunduğu klasöründeki dosyaların listesi
# for dosya in kayitlist:
#     if dosya.endswith(".txt"): #------>>>>>> # sonu .txt olan dosyaların liste    #if dosya.endswith(""): # tüm dosyaların listesi 
#      print(dosya)

# import os
# dosyadizinListesi = os.listdir()
# print("çalışma dizini :",os.getcwd())   #klasörde mi dosyada mı? yerini belirtti
# for a in dosyadizinListesi:
#     print("Dosya\t" if os.path.isfile(a) == True else "Klasör\t", end="")
#     print(a)

# walk()-->>> dizin ve dosyalar arasında gezinir

# import os
# from os.path import join, getsize
# for root, dirs, file in os.walk('D:\\'):
#     print(root,"consumes",end="")                   #yetişmedi. tüm dosyalar arasında gezinir!!!!!!
#     print(sum(getsize(join(root,name))))
#     for name in files),end="")




# import os,time
# while True:
#     os.mkdir("deneme")
#     time.sleep(.5)
#     os.rename("deneme","DENEME")    #deneme adını DENEME olarak çevirdi ve ardından arka arka ekleyip sildi.     
#     time.sleep(.5)
#     os.rmdir("DENEME")
#     time.sleep(.5)


# #>>>>>>>>>>>>>>dosya silme<<<<<<<<<<<<<<

# import os,time

# while True:
#     open("deneme","w")
#     time.sleep(.5)
#     os.rename("deneme","DENEME")   #deneme adını değiştirdi.
#     time.sleep(.5)
#     os.rmdir("DENEME")
#     time.sleep(.5)

# #path.split()
# import os
# print(os.path.split("\\"))
# print(os.getcwd())
# print(os.getcwd().split("\\")) #-------->>> bilgi ayırştırmak için kullanılır ().split)