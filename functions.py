# 1-) gönderilen bir kelimeyi belirtildiği kadar ekranda yazdıran fonksiyon.
def yazdir(kelime, adet):
    print(kelime * adet)
yazdir('merhaba\n' , 10)


# 2-) kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonsiyon.
def listeyeCevir(*args):
    liste = []
    for arg in args:
        liste.append(arg)
    return liste
result = listeyeCevir(10, 20, 30, 40, 'merhaba')
print(result)


# 3-) gönderilen 2 sayı arasındaki tüm asal sayıları bulun
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi >1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
sayi1 = int(input('sayi 1: '))
sayi2 = int(input('sayi 2: '))
asalSayilariBul(sayi1, sayi2)


# 4-)kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün
def tamBolenleriBul(sayi):
    tamBolenler= []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler
print(tamBolenleriBul(20))



