#dosya oluşturma
abc=open("rehber1.txt","w")  #abc=open("d:\\rehber1.txt","a")  ----->>> istenilen sürücüde çalışır
abc.write("Dosyaya kaydedilen veri.\nİkinci satir!!\n")
abc.write("Üçüncü satır\n")
abc.write("Dördüncü satır.\n")
abc.write("w ile her çalıştığında içindeki silinir.")
abc.close() #oluşturulan her dosya kapatılmalıdır.

#dosyaya ekleme yapma
f=open("demofile2.txt","a")           # f=open("demofile2.txt","a",encoding="utf-8")  ----->>>> hata verirse encoding çözecektir.           
f.write("Dosyaya ekleme yapma!\n")
f.write("Her çalıştığında içindekiler silinmez!")
f.close()

#ekleme sonrası dosya içeriğine bakma 
f=open("rehber.txt","r")          # r modu ile içindekileri okuyabilirsin.
print(f.read())


dosyalar=["dosya1.py","dosya2.py"]

for a in dosyalar:
    f=open (dosya1.py,"r",encoding="utf-8")     #bütün dosyaları aktarır
    print(f.read()) 


# dosya kapatma 
f=open("demofile2.txt","r")
print(f.readline())                  
f.close()

#otomatik kapatma
with open("test.txt","w") as dosya:
    dosya.write("merhaba")


#Dosya oluşturma
abc=open("program1.py","w")
abc.write("#Bu program python tarafından otomatik oluşturulmuştur.")
abc.write("\na = input('Bir kelime gir: ')")
abc.write("\nprint(a*20)")
abc.write("\ninput()")
abc.close()

#dosya yeri
# f=open("demofile2.txt","r")     #Açmak istediğimiz dosya kod dosyamız ile aynı klasörde ise
# print(f.read())
      
# f=open("D:/newfolder/deneme.txt","r")
# print(f.read())      


