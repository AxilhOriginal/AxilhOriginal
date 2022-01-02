turgirin = str(input("Lütfen işlem türünüzü seçin. "))

def toplama():
    return print(sayibir + sayiiki)
def carpma():
    return print(sayibir * sayiiki)
def cikartma():
    return print(sayibir - sayiiki)
def bolme():
    if sayiiki == 0:
        print("0'a bölünemez.")
    else:
        return print(sayibir / sayiiki)

sayibir = float(input("1. Sayıyı girin. "))
sayiiki = float(input("2. Sayıyı girin. "))

match turgirin:
    case turgirin if turgirin == "Toplama" or "toplama":
        toplama()
    case turgirin if turgirin == "Çıkartma" or "çıkartma" or "cikartma":
        cikartma()
    case turgirin if turgirin == "Çarpma" or "çarpma" or "carpma":
        carpma()
    case turgirin if turgirin == "Bölme" or "bölme" or "bolme":
        bolme()
