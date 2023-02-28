import os
while True:
    
    print("Hoşgeldiniz")
    x = input("Kişinin İsmi: ")
    y = input("Kişinin Soy İsmi: ")
    z = input("Kişinin Yaşı: ")
    f = input("Kişinin Tc Kimlik Numarası: ")
    h = input("Kişinin Telefon Numarası: ")
    s = " "
    veri = ("\n\nKişinin İsmi: " + x + "\nKişinin Soy İsmi: " + y + "\nKişinin Yaşı: " + z + "\nKişinin Tc Kimlik Numarası: " + f + "\nKişinin Telefon Numarası: " + h)
    print(x + " " + y + " " +"Başarıyla Kaydedildi")
    dosya = open("Database.txt","a")
    dosya.write(veri)
    dosya.close
    os.system('cls')
    
