class Matematik:
    def __init__(self):
        self.numaralar = []

    def ekle(self, numara):
        self.numaralar.append(numara)

    def top(self):
        return sum(self.numaralar)

    def cık(self):
        sonuc = self.numaralar[0]
        for numara in self.numaralar[1:]:
            sonuc -= numara
        return sonuc

    def carp(self):
        sonuc = 1
        for numara in self.numaralar:
            sonuc *= numara
        return sonuc

    def bol(self):
        sonuc = self.numaralar[0]
        for numara in self.numaralar[1:]:
            if numara == 0:
                print("bolme hatası")
            sonuc /= numara
        return sonuc
    def yazdır(self,sonuc):
        self.sonuc = sonuc
        return sonuc
        

def islemler():
    hesap = Matematik()

    while True:
        numara = input("Sayı giriniz (sonuç için = girin) = ")
        if numara == "=":
            break
        else:
            hesap.ekle(float(numara))

        islem = input("İşlem seçiniz (+, -, *, /) = ")

        if islem == "+":
            print("Sonuç:", hesap.top())
        elif islem == "-":
            print("Sonuç:", hesap.cık())
        elif islem == "*":
            print("Sonuç:", hesap.carp())
        elif islem == "/":
            print("Sonuç:", hesap.bol())

islemler()

