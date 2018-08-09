import random

playerList = []

class Tile:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.tiles = []
        suits = ['Circle', 'Character', 'Bamboo', 'Wind', 'Dragon', 'Flower', 'Season']
        winds = ['North', 'South', 'East', 'West']
        dragons = ['Red', 'Green', 'White']
        for x in range(1,5):
            for suit in suits:
                if suit == 'Circle' or suit == 'Character' or suit == 'Bamboo':
                    for i in range(1, 10):
                        tile = Tile(suit, i)
                        self.tiles.append(tile)
                elif suit == 'Wind':
                    for w in range(1,5):
                        tile = Tile(suit, w)
                        self.tiles.append(tile)
                elif suit == 'Dragon':
                    for d in range(1,4):
                        tile = Tile(suit, d)
                        self.tiles.append(tile)
                else:
                    tile = Tile(suit, 1)
                    self.tiles.append(tile)

class Player:
    def __init__(self, name):
        self.name = 'Player ' + str(name)
        self.hand = []

    def drawTile(self):
        for t in range(0, len(deck.tiles)-1):
            r = random.randint(0,(len(deck.tiles)-1))
            self.hand.append(deck.tiles[r])
            deck.tiles.remove(deck.tiles[r])

deck = Deck()

def dealHands():
    for i in range(1, 5):
        playerName = 'player' + str(i)
        playerName = Player(i)
        for x in range(1,5):
            r = random.randint(0,(len(deck.tiles)-1))
            playerName.hand.append(deck.tiles[r])
            deck.tiles.remove(deck.tiles[r])
        playerList.append(playerName)

dealHands()

def turn(playerName):
    pass

for player in playerList:
    print(player.name)
    for tile in player.hand:
        print(tile.suit + ' ' + str(tile.value))

# for player in playerList:
#     for card in player.hand:
#         print(str(player.name) + ': ' + card.suit + str(card.value))
