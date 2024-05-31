#lokal değişken sadece bir fonksiyonun içinde tanımlanan ve o fonksiyonun içinde erişilen değişkenlerdir
a=0
def ornek_fonksiyon():
    a=2
    print("fonksiyonun içindeki a:",a)
ornek_fonksiyon()
print("fonksiyonun dişindaki a:",a)
#listeler değiştirilebilir oldukları için fonksiyonun içindeki işlemler global listeyi  de etkiler
numbers=[]
def add_number():
    numbers.append(5)
    return numbers
print(add_number())
#global değişken fonksiyon dışında tanımlanır her yerden erişilebilir fonksiyon içine global anahtar kelimesini kullanarak globaldeki değişkeni kullanabiliriz
name="ahmet"
def update_name():
    global name 
    name+=" yilmaz"
    return name
print(update_name())
print(name)
#eğer globalde tanımlı bir değişkeni bir fonksiyonun içinde global anahtar kelimesi kullanarak değiştirirsek globaldeki değişken bu değişiklikten etkilenir

#lambda fonksiyonları  :
#lambda anahtar kelimesi ile tanımlanır
selam_ver= lambda isim: f"merhaba {isim}"
print(selam_ver("ahmet"))
#lambda koşullu ifadeler

maksimum= lambda x,y : x if x>y else y
print(maksimum(8,5))
kontrol_et= lambda x: "pozitif" if x>0 else("negatif" if x<0 else "sifir")
print(kontrol_et(0))
print(kontrol_et(-1))
print(kontrol_et(25))

#map fonksiyonu iki parametre alır ilk parametre fonksiyon nesnesidir ikinci parametre olarak değişken alır
def kare_al(x):
    return x**2
x=5
sayilar=[1,2,3]
a=list(map(kare_al,sayilar))
print(a)

#filter fonksiyonu belirli bir koşulu sağlayan elemanları yinelenebilirlerden seçmek için kullanılır
#reduce fonksiyonu bir dizi veya bir listenin elemanlarına ardışık olarak bir işlev uygulamak ve tek bir sonuç değeri elde etmek için uygulanır 
