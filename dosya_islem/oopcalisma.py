# class Ogrenci():
#     ad= "beyza"
#     soyad="ünsal"
#     numara="2030075"
#     notOrt ="3.07"
#     disiplinCezasi = 0

# print(Ogrenci.ad)
# print(Ogrenci.disiplinCezasi)
# print(Ogrenci.numara)

# print("sınıftaki ad değeri:",Ogrenci.ad)
# ogrenci1 = Ogrenci
# ogrenci2 = Ogrenci

# ogrenci1.ad = "ali"
# ogrenci2.ad = "veli"

# print("ogrenci1 nesnesinin ad değeri:", ogrenci1.ad)
# print("ogrenci2 nesnesinin ad değeri:", ogrenci2.ad)

# print("sınıftaki ad değeri:",Ogrenci.ad)

#sınıfa method ekleme

# class ogrenci:
#     ad="beyza"
#     soyad="ünsal"
#     numara="2030075"
#     notOrt ="3.07"
#     disiplinCezasi = 0

#     def Bilgi(self):
#         print("method ile = Adı:",self.ad, "Soyadı:",self.soyad)
#         # print("sınıftaki ad değeri:",ogrenci.ad)

# ogrenci1 = ogrenci()
# ogrenci1.Bilgi()
# print(ogrenci1.__dict__)
# print(ogrenci.__dict__)

# class Ogrenci:
#     Tc="00000000000"
#     ad= "beyza"
#     no="20370075"
#     puan="100"
#     def __init__(self,xx="ad yok",yy=111,zz=20):
#         self.ad=xx
#         self.no=yy
#         self.puan= zz
#     def bilgiVer(self):
#             print("method ile bilgi veriliyor ==> Adı:",self.ad,"Numarası:",self.no)
#     def belgeDurumu(self):
#          if self.puan <80: durum = "Teşekkür"
#          else: durum = "taktir"  
#          return durum
# ogrenci1= Ogrenci("MURAT",787624,80)
# ogrenci2= Ogrenci("Dila",642655,75)
# ogrenci1.bilgiVer()
# ogrenci2.bilgiVer()
# print("ogrenci.puan:",Ogrenci.puan)
# print("ogrenci puan:",ogrenci1.puan)
# print("ogrenci puan:",ogrenci2.puan)    

# print("ogrenci1.belgeDurumu:",ogrenci1.belgeDurumu())
# print("ogrenci2.belge durumu:",ogrenci2.belgeDurumu())

# class Ogrenci:
#     adSoyad="---"
#     notOrt="---"
#     DisiplinCezasi=0

#     def __init__(self):
#         self.adSoyad ="tanmsız"
#         self.Numara = 0

#     def Bilgi(self):
#         print("Adı ve soyadı =>",self.adSoyad,"Numarası =>",self.Numara)
# print("sınıftaki adSoyad değeri:",Ogrenci.adSoyad)
# ogrenci1=Ogrenci()
# ogrenci1.Bilgi()



#__init__

# class Ogrenci:
#     adSoyad="Tanımsız"
#     notOrt=""
#     DisiplinCezasi=0

#     def __init__(self,ad,no):
#         self.adSoyad =ad
#         self.Numara = no

#     def Bilgi(self):
#         print("Adı ve soyadı =>",self.adSoyad,"Numarası =>",self.Numara)
#         print("sınıftaki adSoyad değeri:",Ogrenci.adSoyad)
# ogrenci1=Ogrenci("beyza ünsal", 78645)
# ogrenci1.Bilgi()


# class Ogrenci():
#     AdSoyad ="tanımsız"
#     notOrt=""
#     disiplinCezasi=0

#     def __init__(self,ad,no):
#         self.AdSoyad=ad
#         self.Numara= no

#     def Bilgi(self):
#         print("Metod ile: Adı Soyadı:",self.AdSoyad, "Numarası:",self.Numara)   
#         print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)

# ogrenci1=Ogrenci("BEYZA ÜNSAL",70)
# ogrenci2=Ogrenci("ZEYNEP AZRA",46)
# ogrenci1.Bilgi()
# ogrenci2.Bilgi()


# class araclar():
#     tur="binek"
#     uretici="mersedes"

# print("araçlar sınıfı için")
# print("araç türü:",araclar.tur)
# print("araç üreticisi:",araclar.uretici)

# arac1=araclar
# arac2=araclar
# arac2.tur="araba"
# arac2.uretici="volvo"
# print( "aracın türü=",arac2.tur)
# print( "aracın üreticisi: ",arac2.uretici)


# class Musteri():
#     adSoyad=""
#     bilet=""

#     def __init__(self,ad,bilet):
#         self.adSoyad =  ad
#         self.bilet= bilet

#     def bilgi(self):
#         print("Müşterinin adı ve soyadı: ",self.adSoyad,"Konser Bileti: ",self.bilet)
        


# musteri1 = Musteri("Mehmet Sarığolu", "Sagopa")

# musteri1.bilgi() 

####kalıtım###

# class Calisan():
#     Odulleri =""
#     Rutbesi=""
#     def __init__(self, adSoy,tc):
#         self.TCKN=tc
#         self.adSoyad=adSoy
#     def CalisanBilgi(self):
#         print("Çalışan Bilgileri ===>> Adı ve Soyadı :",self.adSoyad,"TCKN :",self.TCKN)

# calisan1=Calisan("Beyza ÜNSAL",123456)
# calisan1.CalisanBilgi()

# class Idareci(Calisan):
#     ekUcret=0
#     def __init__(self, adSoy, tc, grv ):
#         self.adSoyad=adSoy
#         self.TCKN=tc
#         self.görev=grv
    
#     def CalisanBilgi(self):
#         print("Yönetici Blgileri: adı ve soyadı:",self.adSoyad,"tckn:",self.TCKN,"görev:",self.görev)
        

# calisan2=Calisan("Nedim Ünsal",000000)
# calisan2.CalisanBilgi()


# calisan4 = Idareci("sude erenoğlu",6541635136,"tasarimci")
# calisan4.CalisanBilgi()


#####super().__init__  

# class Calisan():
#     Odulleri=""
#     Rutbesi=""

#     def __init__(self,adSoy,tc):
#         self.adSoy= adSoy
#         self.TCKN= tc

#     def CalisanBilgi(self):
#         print("Çalisan bilgileri-> Adı ve Soyad :",self.adSoy,"TCKN :",self.TCKN)


# class Idareci(Calisan):
#     ekUcret=0
#     def __init__(self,adSoy,tc,grv):
#         super().__init__(adSoy,tc)
#         self.gorev=grv
#     def CalisanBilgi(self):
#         print("yönetici bilgi >> Adı Soyad: ",self.adSoy,"Tckn :",self.TCKN,"Görev: ",self.gorev)


# calisan1=Calisan("erdinç dönmez",1234566)
# calisan1.CalisanBilgi()
# calisan2 = Idareci("beyza Ünsal","123546546","Müdür")
# calisan2.CalisanBilgi()

#####kapsülleme#####

# class Ogrenci:
#     def __init__(self,xx,yy,zz="normal"):
#         self.ad=xx
#         self.no=yy
#         self.__sd=zz

#     def sağlikDurumu(self):
#         return self.__sd

# ogrenci1= Ogrenci("murat",685425)
# ogrenci2=Ogrenci("dila",54633541,"astımı var")

# print(ogrenci1.sağlikDurumu())
# print(ogrenci2.sağlikDurumu())

# class urun:
#     def __init__(self):
#         self.__fiyat=1000
    
#     def fiyatYaz(self):
#         print("Ürün FİYATI :",self.__fiyat)
#     def setFiyat(self,fiyat):
#         self.__fiyat = fiyat
# u= urun()
# u.fiyatYaz()



