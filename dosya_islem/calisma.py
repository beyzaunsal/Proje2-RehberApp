# import os               #klasörün konumu belirleme
# print(os.getcwd())

# import os 
# yer= os.getcwd()           #klasör konumunu değiştirme
# yer+="/deneme "
# os.chdir(yer)
# print(os.getcwd())

# import os 
# yer=os.getcwd()
# print("konum:",yer)
# for a in os.listdir(): print(a)         #klasör konumunu değiştirme
# yer += "/deneme"
# os.chdir(yer)
# print("konum: ",yer)
# for b in os.listdir(): print(b)

# os.mkdir("yeni klasör")     #yeni klasör oluşturma
# os.rmdir("sil")             # klasör silme
# os.rename("aa","yeni klasör")   #dosya/klasör adı değiştirme

# olusacak = input("Oluşturacağınız klasör adı:")
# os.mkdir(olusacak)

# import os
# silinecek = input("sileceğiniz klasör adı:")
# os.rmdir(silinecek) 


# import os 
# eskiad= input("adı değişecek klasör veya dosya:")
# yeniad=input("yeni ad nedir:")
# os.rename(eskiad,yeniad)

# import os 
# liste = os.listdir()
# durum = "yok "
# aranan="doysalar2"
# for a in liste:
#     if a == aranan: durum = "var"
    
# print(durum)
# if (durum) == "yok":
#     os.mkdir(aranan)
 
# import os
# path.exists()                                 ????????
# print(os.path.exists('E:\\deneme.txt'))
 

# okunan= open("rehber.txt","r")
# print(okunan.read())           #read() ile tümü okunur
# okunan.close()

# try:
#     okunan = open ("rehber.txt","r")
#     print(okunan.read())
#     okunan.close()
# except:
#     print("bir hata oluştu")

# okunan = open ("rehber.txt","r")
# print(okunan.readline())          #satır okunur
# okunan.close()


# okunan = open("rehber.txt")
# for a in okunan:
#     print(a)
# okunan.close()   

# import os
# os.remove("demofile2.txt")
 

# import os 
# if os.path.exists("demofile2.txt"):
#     os.remove("demofile2.txt")
# else: 
#     print("silmek istediğiniz dosya yok")


# import os
# silinecek= input("sileceğin dosya adı:")
# os.rmdir(silinecek)


# import os 
# os.remove("demofile2.txt")
# if os.path.exists("demofile2.txt"):
#     os.remove("demofile.txt")
# else:
#     print("silmek istediğiniz dosya yok")

# yer= os.getcwd()
# print("konum: ", yer)    

# import os 
# os.remove("demofile2.txt")
# if os.path.exists("demofile2.txt"):
#     os.remove("demofile.txt")
# else:
#     print("silmek istediğiniz dosya yok")

a=[2,4,1,6]
b=[3,2,5,1]
c=a
d=c[:]