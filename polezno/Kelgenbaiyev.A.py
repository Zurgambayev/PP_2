class Parent1():
    word1 = ''
    def __init__(self, color1, number1):
        self.color1 = color1
        self.number1 = number1
    def printInfo1(self):
        print(f'{self.color1}    perents1     {self.number1}')
    def setWord1(self, word1):
        self.word1 = word1

    def getWord1(self):
        print(self.word1)

class Parent2():
    word2 = ''
    def __init__(self, color2, number2):
        self.color2 = color2
        self.number2 = number2
    def printInfo2(self):
        print(f'{self.color2}   Parent2     {self.number2}')

    def setWord2(self, word2):
        self.word2 = word2

    def getWord2(self):
        print(self.word2)

class BabyBay(Parent1,Parent2):
    word3 = ''
    def __init__(self,color1,number1,color2,number2):
        Parent1.__init__(self,color1,number1)
        Parent2.__init__(self,color2,number2)
        self.color3 = self.color1 + self.color2
        self.number3 = self.number1 + self.number2
    def printInfo3(self):
        print(f'{self.color3}   BabyBay   {self.number3}')
    def setWord3(self):
        self.word3 = self.word1 + self.word2 
    def getWord3(self):
        print(self.word3)


c1 = input() 
in1 = int(input())
c2 = input()
in2 = int(input())
w1 = input()
w2 = input()



p3 = BabyBay(c1,in1,c2,in2)
p3.setWord1(w1)
p3.setWord2(w2)
p3.setWord3()


p3.printInfo1()
p3.printInfo2()
p3.getWord1()
p3.getWord2()
p3.printInfo3()
p3.getWord3()


