class Meci:
    def __init__(self, jucator1, jucator2, cota1, cota2):
        self.jucator1 = jucator1
        self.jucator2 = jucator2
        self.cota1 = cota1
        self.cota2 = cota2
        self.probabilitate = (1 / float(cota1) + 1 / float(cota2)) * 100

    def __str__(self):
        return "Joaca " + self.jucator1 + " cota " + self.cota1 + " vs " + self.jucator2 + " cota " + self.cota2 + " probabilitate totala: " + str(self.probabilitate)