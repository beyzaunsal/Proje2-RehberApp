#fonksiyonlar

# def selamla():               Normal (basit) fonksiyonlar. Değer almaz, değer döndürmez
#     print("merhaba")
#     print("nasılsın")
# selamla()   

# def soyle(xxx="değer gönderilmedi"):    # Değer alan fonksiyonlar
#     print(xxx)
# soyle()
# soyle("napıyon")    


# Değer döndüren fonksiyon

# def topla(a,b):
#     return a+b

# print(topla,(8,topla(3,5)))


    # Değer alan fonksiyonlarda default parametre değeri

# def topla(s1=4,s2=5):
#     print(s1+s2)

# topla(3,4)
# topla()    

# def bol(s1,s2):
#     print(s1/s2)
# bol(8,2)
# bol(6,3)
# bol(s2=6,s1=3)   


# def topla(s1=int(input("1.Sayıyı giriniz: ")),s2=int(input("2.sayıyı giriniz: "))):
#     print(s1+s2)
# topla()    

# def soyle(x="değer gönderilmedi"):
#     print(x)

# soyle()
# soyle("merhaba")    


# def topla(a,b,c=0):
#     return sum((a,b,c))

# print(topla(10,20))
# print(topla(10,20,30))


# İsimli parametre kullanımı

# kayitNo=1

# def kayitolustur(ad,soyad,no):
#     global kayitNo
#     print(f"\n{kayitNo}.kayıt oluşturuldu.")
#     print(f"Soyad:{soyad} Ad:{ad} numara:{no}\n")
#     kayitNo+=1
 
# kayitolustur("erhan","gün","41")

# kayitolustur("23","erdinç","dönmez") # sıra olmadığından karışır


# Global ve yerel değişkenler
# degisken =11
# def fonksiyon1 ():
#     print (degisken)

# fonksiyon1()    

# degisken=11
# def fonksiyon1():
#     degisken=22
#     print("yereldeki: ",degisken)

# fonksiyon1()
# print("globaldaki: ",degisken)

# degisken=11
# def fonksiyon1():
#     print("yereldeki2:",degisken)

# fonksiyon1()
# print("globaldaki: ",degisken)

# degisken=11
# def fonksiyon1():
#     global degisken
#     degisken =22
#     print("yereldeki:",degisken)

# fonksiyon1()
# print("globaldaki:",degisken)    

# Hangisi global ?
# (global bir üstteki mi, en baştaki mi?)

# degisken = 11
# def fonksiyon1():
#   degisken = 22
# print("Yereldeki:",degisken)
# def ictekiFonksiyon():
#   degisken = 33
# print("İçteki fonksiyon:",degisken)
# ictekiFonksiyon()
# fonksiyon1() 

# print("Globaldeki:",degisken)

# degisken =11
# def fonksiyon1():
#  global degisken
#  degisken = 22
#  print("Yereldeki:",degisken)
# def ictekiFonksiyon():
#  degisken = 33
#  print("İçteki fonksiyon:",degisken)
# ictekiFonksiyon()
# fonksiyon1()
# print("Globaldeki:",degisken)

# İç içe fonksiyonlar/Nested Functions

# def selam():
#     print("merhaba")
# def sabah():
#         print("güno")

# selam()

# Arbitrary Arguments   *args / *params

# def topla(*sayilar):
#     print("gelenler: ",sayilar)
#     print("sayilar[1]:",sayilar[1])

# topla(10,20,30)    

# def listele (*gelen):
#     print(gelen)
#     print(3,"eleman ",gelen[3-1])
# listele ("doruk", 5, "helin")    

# def topla(*parametreler):
#     print("gönderilen veri/dizi: ",parametreler)
#     print("gönderilen parametre sayısı:",len(parametreler))
#     toplam =0
#     for n in parametreler: toplam += n;
#     return toplam
# print(topla(10,20,50))
# print("toplam: ",topla(10,20,30,50))


# def topla(*parametreler):
#     return sum(parametreler)
# print(topla(10,20))
# print(topla(10,20,30,50))

yy=[22,2,41,62]
def topla(*xx):
    print("xx : ",xx)
    topla=0
    for a in xx :topla += a; print(a)
    print(topla)
    print("xx[3] : ",xx[3])
topla(55,2,41,62)    