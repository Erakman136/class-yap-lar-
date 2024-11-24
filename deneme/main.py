class Computer:
    colour = "blue" #
    brand = "Hp"
    sistem = "windows"#
    surum = "11" #
    ekran_kartı = "NVIDIA GEFORCE RTX" #

    def surum_bilgisi(self):
        print(f"Sürüm: {self.surum}")

    def renk_bilgisi(self):
        print(f"renk: {self.colour}")

    def ekran_karti_bilgisi(self):
        print(f"Ekran Kartı: {self.ekran_kartı}")
    
    def sistem_bilgisi(self):
        print(f"Sistem: {self.sistem}")
        
    def marka(self):
        print(f"Marka: {self.brand}")

# Nesne oluştur
bilgisayar = Computer()

# Ekran kartı bilgisini al
bilgisayar.ekran_karti_bilgisi()

# Sürüm bilgisini al
bilgisayar.surum_bilgisi()

bilgisayar.sistem_bilgisi()

bilgisayar.renk_bilgisi()

bilgisayar.marka()


