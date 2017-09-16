import Player
import random
class Computer(Player.Player):

    def __init__(self,health,i):

        self.name = 'Computer{}'.format(i)

        super().__init__(health,self.name)
        rand1 = random.randint(0,1000)
        rand2 = random.randint(0,1000)
        rand3 = random.randint(0,1000)


        t = rand1 + rand2 + rand3

        prob1 = rand1/t
        prob2 = rand2/t
        prob3 = rand3/t

        self.rockL = prob1
        self.paperL = prob2 + prob1

        print("{} {}".format(self.rockL,self.paperL))

    def getHand(self):

        hand = []

        for i in range(2):
            x = random.random()

            if x <= self.rockL:
                hand.append('r')

            elif x<= self.paperL:
                hand.append('p')

            else:
                hand.append('s')
        print("\t{}: {}".format(self.name,hand))
        return hand

pass
