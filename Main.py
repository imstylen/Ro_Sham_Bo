import Game

# # player1 = Game.Computer.Player.Player(10,"Mike")
# player1 = Game.Computer.Computer(10,1)
# player2 = Game.Computer.Computer(10,2)
# player3 = Game.Computer.Computer(10,3)
# player4 = Game.Computer.Computer(10,4)
rock = 0
paper = 0
n = 100
for i in range(n):
    players = []

    nPlayers = 100
    for i in range(nPlayers):
        players.append(Game.Computer.Computer(1000,i+1))

    game = Game.Game(players)

    playersLeft = True

    rnd = 1
    while playersLeft:
        cleanout = []
        for player in game.players:
            if player.health <= 0 :
                cleanout.append(player)
        for item in cleanout:
            second = item
            game.players.remove(item)
        if len(game.players) <= 1:
            print(game.players[0].getLimits())
            rock += game.players[0].getLimits()[0]
            paper += game.players[0].getLimits()[1]
            print(second.getLimits())

            break
        print("ROUND NUMBER: {}".format(rnd))
        rnd +=1
        game.playRound()
        print("")
print("\nlimits")
print(rock/n)
print(paper/n)
