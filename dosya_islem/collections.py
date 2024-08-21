# a=[2,4,1,6]
# b=[3,2,5,1]
# c=a              # dizi adresini başka bir dizi adresi içine atıyoruz
# d=c[:]           #dizi değerlerini başka bir adrese kopya oluşturma


# print("a: ",a)
# print("b: ",b)
# print("c: ",c)
# print("d: ",d)

# print(a[1])
# a[1]=5
# print(a[1])

# c[1]="h"
# print('\nc[1] = "h" sonrası')

# print(a[1])
# print("a: ",a)
# print("d: ",d)

#eklnebilir, silinebilir,sıralanabilir

# eleman ekleme: append, insert
# değer katma: +=

meyve1=["elma","armut"]
meyve2=["muz","kiraz"]
meyve3=[]
meyve3 +=meyve1
print(meyve3)
meyve3.append(meyve2)
print(meyve3)