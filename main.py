isim1 =input("İsminiz : ")
isim2 = input("Sevgilinizin ismi : ")

ask = len(isim1) + len(isim2)

if len(isim1) > len(isim2):
    ask -=5
else:
    ask +=3

ask *=42
ask = ask / (100 + len(isim2))

ask = 10 if ask > 10 else round(ask,0)

print(f"{isim1} ve {isim2} skoru 10 üzerinden {ask} !")

