class house():
    """описание дома"""
    def __init__(self,street,number):
        """свойства дома """
        self.street = street
        self.number = number
    def build(self,):
        """будет стройть дом"""
        print("house on the street " + self.street + " under the number " + str(self.number) + " built")
class ProspectHous(house):
    """дома на проспекте"""
    def __init__(self,procpekt, number):
        super().__init__(self,number)
        self.procpekt = self.procpekt


PrHous = ProspectHous("Abaya",7)
print(PrHous.procpekt)
