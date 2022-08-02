from cards import Cards
from player import Player
import utilities as ut
import rich
from rich.columns import Columns

players_hand = []

player = Player("Joe")
bot = Player("Bot")

turn = 0

while not player.isLost() and not bot.isLost():
    player.addMana(turn)
    bot.addMana(turn)
    playerTable = player.printHand()
    botTable = bot.printHand()
    
    columns = Columns([player.printHand(), bot.printHand()], equal=True, expand=True)
    rich.print(columns)
    print("Play a card to attack:")

    while not (cardPlayed := player.getCard(input(">> "))):
        pass
    
    botCard = bot.getRandomCard()
    print(f"{bot.getName()} played {botCard['NAME']}")
    ut.attack(cardPlayed, botCard)
    
    botCard["HP"] -= cardPlayed["DMG"]
    if botCard["HP"] <= 0:
        if botCard["NAME"] == "Wolf":
            bot.addPerm()
        print(f"bot lost {botCard['NAME']}")
        bot.addToGraveyard(botCard)
    
    turn += 1