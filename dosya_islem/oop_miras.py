class Ilan(): #sınıf türetirken çoğul kullanılmaz
    aktiflik = True
    def __init__(self, no, bas):
        self.ilanNo = no
        self.baslik = bas
    
    def ilanbiigisi(self):
        print("no: ",self.ilanNo, "baslik :",self.baslik)

class Arac(Ilan):
    def __init__(self, no , bs, fy,tur):
        super().__init__(no,bs)
        self.aracFiyati = fy
        self.aracTuru = tur

class ev (Ilan):
    def __init__(self,no,bas,m2_,konumu_):
        super.__init__(no,bas)
        self.m2 = m2_
        self.konum = konumu_

class kiralikev(ev):
    def __init__(self,no,bas,m2_,konumu_,depozito,kirasi):
        super().__init__(no,bas,m2_,konumu_)
        self.depozito = depozito
        self.kirasi = kirasi

# @abstractmedhod bilgi almada zorunluluk getirmesini istersen. !!!!!!!!!!!!!!!!!!
class satilikev(ev):
    def __init__(self, no, bas, m2_, konumu_, fiyati, ipotek):
        super().__init__(no, bas, m2_, konumu_,depozito,kirasi)
        self.fiyat = fiyati
        self.ipotek = ipotek

ilan234 = satilikev(23652,"sahibinden kelepir 2+1", 120,"demetevler",3000000,"yok")
ilan234.ilanbiigisi()        
# ilan46515215 = Ilan(46515215,"pıtır pıtır şahin")
# ilan64645464 = Ilan(64645464, "aslanlar gibi toros")

# ilan46515215.ilanbiigisi()
# ilan64645464.ilanbiigisi()

arac1 = Arac(46515215,"pıtır pıtır şahin", 500000, "binek")
arac1.ilanbiigisi()
# >>>>>>>>>>>>kalıtım<<<<<<<<<<<<<<<

# class Calisan():
#     odulleri = ""
#     rutbesi = ""
#     def __init__(self,tc = "---", adSoy = "---"):
#         self.TCKN = tc
#         self.adiSoyadi = adSoy
#     def calisanBilgisi(self):
#         print("çalışan bilgileri : adı soyadı:", self.adiSoyadi,"TCKN:",self.TCKN)

# calisan1=Calisan(adSoy="beyza Ünsal",tc ="123456")
# calisan1.calisanBilgisi()        

# class Idareci(Calisan):
#     ekucret = 0
#     def __init__(self, tc="---", adSoy="---",grc="henüz tanımlı değil."):
#         super().__init__(tc, adSoy)
#         self.gorev = grv
#     def calisanBilgisi(self):
#         print("yönetici bilgleri : adı ve soyadı",self.adiSoyadi,"görevi:",grv)    

# calisan2 = Idareci(adSoy="kdjghksj",tc ="98217515")
# calisan2.calisanBilgisi()

# calisan4 = Idareci("mehmet arlı","1232153","müdür")
# calisan4.calisanBilgisi()