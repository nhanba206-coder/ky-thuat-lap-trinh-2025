class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dien_tich(self):
        return self.dai * self.rong

h = Hinhchunhat(5, 3)
print("Dài x Rộng =", h.dai, "x", h.rong)
print("Diện tích =", h.dien_tich())  
