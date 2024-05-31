matris2=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
for satir in matris2:
    for eleman in satir:
        print(eleman,end=" ")
    print()
matris=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matris)
kareler_matrisi=[[eleman**2 for eleman in satir] for satir in matris]
for satir in kareler_matrisi:
    print(satir)

ogrenciler=[["ahmet",[90,85,80]],
            ["merve",[88,92,94]],
            ["cem",[65,70,72]]
]
for ogrenci in ogrenciler:
    ad,notlar=ogrenci
    ortalama=sum(notlar)/len(notlar)
    print(f"{ad}->ortalama not: {ortalama:.2f}")

#list comprehension örnekleri
a=[x*2 for x in range(10) if x%2==0]
print(a)
cift_sayilar=[c for c in range(10) if c%2==0]
print(cift_sayilar)
ascii_sozluk={chr(i):i for i in range(65,91)}
print(ascii_sozluk)