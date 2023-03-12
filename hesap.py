class HesapMakinasi:
    def topla(self,ilk_sayi,ikinci_sayi):
        return ilk_sayi+ikinci_sayi
    def çikar(self,ilk_sayi,ikinci_sayi):
        return ilk_sayi-ikinci_sayi
    def bol(self,ilk_sayi,ikinci_sayi):
        return divmod(ilk_sayi,ikinci_sayi)
    def carp(self,ilk_sayi,ikinci_sayi):
        return ilk_sayi * ikinci_sayi
hesap=HesapMakinasi()
while True:
    try:
        a=int(input("ilk sayıyı giriniz"))
        b=int(input("ikinci sayıyı giriniz"))
        break
    except ValueError:
        print("lütfen gecerrli bir tam sayı giriniz")

islem = input("islem giriniz \ntoplam : +\ncıkarma : -\nbol : /\ncarp : *\n")

if islem == "+":
    print("girdiginiz iki sayının toplamı",hesap.topla(a,b))
elif islem == "-":
    print("girdiginiz iki sayının farkı",hesap.çikar(a,b))
elif islem == "*":
    print("girdiginiz iki sayının carpımı",hesap.carp(a,b))
elif islem == "/":
    print("girdiginiz iki sayının boleni ve kalanı",hesap.bol(a,b))
