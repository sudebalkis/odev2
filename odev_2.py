def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "+":
        sonuc = sayi1 + sayi2 
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
        else:
            return "Bölme işleminde ikinci sayı 0 olamaz."
    else:
        return "Geçersiz işlem."
    
    return f"Sonuç: {sonuc}"

print(hesap_makinesi(10, 5, "+"))