import Computer

class Game:

    def __init__(self,players):
        self.players = players

    def selectHands(self):

        self.hands = []
        for player in self.players:

            hand = player.getHand()

            self.hands.append((player,hand))

    def getScores(self):

        battleStr = ['rr','rp','rs','pr','pp','ps','sr','sp','ss']
        battlePt = [0,-1,1,1,0,-1,-1,1,0]

        scores = []
        for hand in self.hands:
            sc = 0
            for opponenthand in self.hands:
                if hand == opponenthand:
                    continue
                for attack in hand[1]:
                    for defend in opponenthand[1]:
                        bt = attack + defend
                        for i, pr in enumerate(battleStr):
                            if pr == bt:
                                # print(battlePt[i])
                                sc += battlePt[i]
                                break
            scores.append((hand[0],hand[1], sc))
        return scores

    def playRound(self):
        self.selectHands()
        scores = self.getScores()
        for score in scores:
            score[0].attack(score[2])
        for player in self.players:
            print("{}: {}".format(player.name,player.health))


# if __name__ == "__main__":
#     player1 = Computer.Player.Player(5)
#     player2 = Computer.Player.Player(5)
#     player3 = Computer.Player.Player(5)
#
#     game = Game([player1,player2,player3])
#     game.playRound()
