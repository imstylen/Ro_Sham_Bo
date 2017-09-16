class Player:

    def __init__(self,health,name):
        self.health = health
        self.name = name

    def getHand(self):
        prs = ['r','p','s']

        playerHand = []
        i = 0
        while i < 2:
            pIn = input("Choose your {}th hand mofo: ".format(i+1))
            if pIn.lower() not in prs:
                print('Its ro sham bo.. Not ro sham {}... XD'.format(pIn.lower()))
                continue
            playerHand.append(pIn.lower())
            i+=1
        print("\t{}: {}".format(self.name,playerHand))
        return playerHand

    def attack(self,d): #target
        if d < 0:
            self.health += d
        # else:
        #     target.attack(-1*d,target)
