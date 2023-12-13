import math

class Kalkulator:
    def __init__(self, x, y):
       self.A = x
       self.B = y
       print("A = "+str(x) + ",B = "+str(y))

    def tambah(self):
        self.hasil = self.A + self.B
        print("Hasil A + B = " + str(self.hasil))

    def kurang(self):
        self.hasil = self.A - self.B
        print("Hasil A - B = " + str(self.hasil))

    def kali(self):
        self.hasil = self.A * self.B
        print(" Hasil A x B = " + str(self.hasil))

    def bagi(self):
        if self.B == 0:
            print("Hasil Pembagian Dengan Nol")
        else:
            self.hasil = self.A / self.B
            print("Hasil A / B = " + str(self.hasil))

    def pangkat(self):
        self.hasil = self.A ** self.B
        print("Hasil A ^ B = " + str(self.hasil))

    def akar(self):
        if self.A < 0 :
            print ("Nilai A harus positif")
        else:
            self.hasil = math.sqrt(self.A)
            print("Hasil Akar dari A = " + str (self.hasil))
    
    def modulus(self):
        self.hasil = self.A % self.B
        print("Hasil A % B = " + str(self.hasil))

Object1 = Kalkulator(1,2)
Object1.tambah()
Object1.kurang()
Object1.kali()
Object1.bagi()
Object1.akar()
Object1.pangkat()
Object1.modulus()



Object2 = Kalkulator(2,0)
Object2.bagi()