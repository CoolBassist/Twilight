from cards import Cards
from player import Player
import utilities as ut
import rich
from rich.columns import Columns
from rich.panel import Panel
import time
import os

players_hand = []

player = Player("Joe")
bot = Player("Bot")

turn = 0

history = []



while not player.isLost() and not bot.isLost():
    os.system("cls")
    rich.print(Panel("Twilight",subtitle_align="center" ,subtitle="A turn-based card game"))
    print()
    player.addMana(turn%3 + 1)
    bot.addMana(turn%3 + 1)
    
    columns = Columns([player.getHandTable(), bot.getHandTable()], equal=True, expand=True)
    rich.print(columns)
    
    for i in history:
        rich.print(i)
        
    rich.print(f"Play a card to {'attack' if turn%2 == 0 else 'defend against'} [red]{bot.getName()}[/red]:")

    while not (cardPlayed := player.getCard(input(">> "))):
        pass
    
    botCard = bot.getRandomCard()
    
    currentMessage = ""
    
    if turn % 2 == 0:
        currentMessage = ut.attack(cardPlayed, botCard, turn)
        if botCard["HP"] <= 0:
            if botCard["NAME"] == "Wolf":
                bot.addPerm()
            print(f"bot lost {botCard['NAME']}")
            bot.addToGraveyard(botCard)
    else:
        currentMessage = ut.attack(botCard, cardPlayed, turn)
        if cardPlayed["HP"] <= 0:
            if cardPlayed["NAME"] == "Wolf":
                player.addPerm()
            print(f"{player.getName()} lost {botCard['NAME']}")
            player.addToGraveyard(cardPlayed)
    
    rich.print(currentMessage)
    time.sleep(4)
    history.append(currentMessage)
    
    turn += 1