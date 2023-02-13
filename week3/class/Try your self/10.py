class house():
    """описание дома"""
    def __init__(self,street,number):
        """свойства дома """
        self.street = street
        self.number = number
    def build(self,):
        """будет стройть дом"""
        print("house on the street " + self.street + " under the number " + str(self.number) + " built")
House1 = house("Tole Bi",20)
House2 = house("Tole Bi",21)

House1.build()
