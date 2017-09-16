import Game

# # player1 = Game.Computer.Player.Player(10,"Mike")
# player1 = Game.Computer.Computer(10,1)
# player2 = Game.Computer.Computer(10,2)
# player3 = Game.Computer.Computer(10,3)
# player4 = Game.Computer.Computer(10,4)

players = []

nPlayers = 100
for i in range(nPlayers):
    players.append(Game.Computer.Computer(10,i+1))

game = Game.Game(players)

playersLeft = True

rnd = 1
while playersLeft:
    cleanout = []
    for player in game.players:
        if player.health <= 0 :
            cleanout.append(player)
    for item in cleanout:
        game.players.remove(item)
    if len(game.players) <= 1:
        break
    print("ROUND NUMBER: {}".format(rnd))
    rnd +=1
    game.playRound()
    print("")
