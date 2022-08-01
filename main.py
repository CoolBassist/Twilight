from cards import Cards
from player import Player
import utilities as ut

players_hand = []

player = Player("Joe")
bot = Player("Bot")

player.printHand()

print(player.getCard("Dragon"))