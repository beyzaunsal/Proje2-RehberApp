# def topla(a):
#     print(a)
#     toplam=0
#     for x in a:
#         toplam+d=x
#     print("Toplam: ",toplam)    


# topla([3,4,2,5,6])    #diziyi de alabilir.dizinin içine istediğin kadar eleman ekleyebilirsin.

# def topla(*a):
#     print(a)
#     toplam = 0
#     for x in a:                      #  * ->alttaki köşeli parantezi kullanmamıza gerek kalmadı.
#         toplam+=x
#     print("Toplam: ",toplam)    

# topla(3,4,2,5,6)  

#<<<<args>>>>
# def yaz (**xx):
#     print(type(xx))
#     print("gelen veri: ",xx)
#     print("Soyadı:"+ xx["soyad"])   # ** -> dictionary şeklinde aldı veriyi

# yaz (ad="Beyza",soyad ="Ünsal")

# def fonksiyon(a,b,c, *dd,*ff, **ee): aynı fonksiyonda iki tane arg eklenmez.
# def fonksiyon(a,b,c, *dd,**ee):      #sıralama önemli
#     print(a)
#     print(b)

#     print(c)
#     print(dd)
#     print(ee)

# fonksiyon(4,2,4,1,3,5,1, key1="ankara",key2 ="izmir")    

#<<<<<<map>>>>>>>>>

# sayilar =[11,22,3]
# def carp(xx):                #herbirini kendi içinde 2 ile çarptı
#     return xx*2               #diziyi map fonksiyonuna verirsen yeni dizi oluşturur (güncellenmiş halini)
                          
# yeniDizi =list(map(carp,sayilar))

# print (yeniDizi)

# ürünFiyatları =[100,200,300]
# def yariyaindir(xx):                
#     return xx//2                     
                          
# yeniDizi =list(map(yariyaindir,ürünFiyatları))

# print (yeniDizi)


#   map kullanılmasaydı 


# ürünFiyatları =[100,200,300]
# def yariyaindir(xx):                
#     return xx//2                     
                          
# #yeniDizi =list(map(yariyaindir,ürünFiyatları))
# yeniDizi=[]
# for a in range(len(ürünFiyatları)):
#     yeniDizi.append(yariyaindir(ürünFiyatları[a]))


# print (yeniDizi)

#<<<<<<<<<<<<<lambda>>>>>>>>> satır içi basit fonksiyon
# print((lambda x:x**2)(5))

# karesi =lambda n:n**2
# print(karesi(4))

# sayilar =[11,22,3]
# def carp(xx):
#     return xx*2               #uzun hali
# yeniDizi=[]
# for a in sayilar:
#     yeniDizi.append(carp(a))

# print(yeniDizi)


#<<<<<<<<<<filter>>>>>>>>>>>

# sayilar =[11,22,3]
# def carp(xx):
#     return xx*2               
# for a in sayilar:
#     yeniDizi.append(carp(a))
# print(yeniDizi)   
# yeniDizi= list(filter (lambda x:x%2==0,sayilar))

# sayilar= [11,22,3,6,7,5,8]
# def ciftmi(x):
#     return x%2==0
# yeniDizi=list(filter(ciftmi,sayilar))

# ogrenciNotlari=[[60,90,80],[20,60],[90,90,80]]
# def gectimi(x):
#     # toplam =0
#     # for a in x: toplam +=a
#     # return toplam
#     if len (x)>2 : durum = True
#     else: durum =False
#     return durum
    
# yeniDizi =list(filter(gectimi,ogrenciNotlari))
# print(yeniDizi)


#>>>>>>>>>>>>>>>>özyinelemeli fonksiyonlar<<<<<<<<<

# def sayac():
#     i=0;
#     while True:    
#         yield i;
#         i += 2

# say=sayac()        
# for a in range(5):
#     print(next(say))         