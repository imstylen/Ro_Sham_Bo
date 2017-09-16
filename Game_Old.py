import Computer

import os

def getScore(player1Hand,player2Hand):

    battleStr = ['rr','rp','rs','pr','pp','ps','sr','sp','ss']
    battlePt = [0,-1,1,1,0,-1,-1,1,0];

    score = 0
    for charP in player1Hand:

        for charC in player2Hand:

            bt = charP + charC

            # print(bt)

            for i, pr in enumerate(battleStr):
                if pr == bt:
                    # print(battlePt[i])
                    score += battlePt[i]
                    break
    return score
#=====================
#   game
#=====================
player1 = Computer.Player.Player(5)
player2 = Computer.Computer(5)

roundNumber = 1;

while player1.health > 0 and player2.health > 0:

    print("Round Number: {}".format(roundNumber))
    roundNumber += 1

    player1Hand = player1.getHand()
    print(player1Hand)
    player2Hand = player2.getHand()
    print(player2Hand)

    score  = getScore(player1Hand,player2Hand)

    player1.attack(score,player2)

    print("Player 1: {}".format(player1.health))
    print("Player 2: {}".format(player2.health))
    print("Score:{}".format(score))

    print("\n")
