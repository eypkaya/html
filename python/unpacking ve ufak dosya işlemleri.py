#sep bu parametre değerler arasındaki  ayırıcıyı belirler varsayılan değeri " " tur
#end çıktının sonunda kullanılacak karakteri belirler defaultu "\n" dir
#file çıktının yazılacağı dosyayı belirler
dosya=open("deneme.txt","w")
print("dosyaya yazilan metin",file=dosya)
dosya.close
#flush True olarak ayarlandığında çıktının tamponlamadan hemen diske yazılmasını sağlar defalut değeri false dur
print("hemen yazdir",flush=True)
f= open("yeni_dosya.txt","w")
print("ubuntu",file=f)
print("python",file=f)
f.close

demet=(1,2,3)
print(*demet)
dizi="abc"
print(*dizi)
print(*enumerate("python"))
#complex fonksiyonu karmaşık sayı oluşturmamızı sağlar
sayi=complex(1,5)
print(sayi)
print(sayi.real)
print(sayi.imag)