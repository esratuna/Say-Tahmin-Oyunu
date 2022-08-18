import random

x = int    #Oyunun belirlediği sayı
y = int    #Bizim tahminimiz

x = random.randrange(1,10)          #Oyunun 1-10 arasında rastgele bir sayı seçmesini sağlayan kod
y = input("Sayıyı tahmin edin = ") 

print(x)

if x == y:
    print("Tebrikler oyunu kazandınız")

else :
    print("İyi denemeydi belki bir daha ki sefere")
