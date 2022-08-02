from turtle import hideturtle
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
    
    print("...") if len(history) > 5 else None
    
    for i in history[-5:]:
        rich.print(i)
        
    rich.print(f"Play a card to {'attack' if turn%2 == 0 else 'defend against'} [red]{bot.getName()}[/red]:")

    while (not (cardPlayed := player.getCard(input(">> ")))):
        pass
    
    botCard = bot.getRandomCard()
    
    if cardPlayed["NAME"] == "Rest" and botCard["NAME"] == "Rest":
        rich.print(f"[green]{player.getName()}[/green] and [red]{bot.getName()}[/red] have agreed to a temporary peace treaty...")
        history.append(f"[green]{player.getName()}[/green] and [red]{bot.getName()}[/red] have agreed to a temporary peace treaty...")
        turn += 1
        time.sleep(4)
        continue
    
    if turn == 1 and cardPlayed["NAME"] == "Rest":
        party = player.getHand()[1:]
        for i in party:
            ut.attack(botCard, i, turn)
        
        rich.print(f"[red]{bot.getName()}[/red] attacks the entire party while [green]{player.getName()}[/green] was resting for [white on red]{botCard['DMG']}[/white on red] damage!")
        history.append(f"[red]{bot.getName()}[/red] attacks the entire party while [green]{player.getName()}[/green] was resting for [white on red]{botCard['DMG']}[/white on red] damage!")
        turn += 1
        time.sleep(4)
        continue

    if turn == 0 and botCard["NAME"] == "Rest":
        party = bot.getHand()[1:]
        for i in party:
            ut.attack(cardPlayed, i, turn)
        
        rich.print(f"[green]{player.getName()}[/green] attacks the entire party while [red]{bot.getName()}[/red] was resting for [white on red]{cardPlayed['DMG']}[/white on red] damage!")
        history.append(f"[green]{player.getName()}[/green] attacks the entire party while [red]{bot.getName()}[/red] was resting for [white on red]{cardPlayed['DMG']}[/white on red] damage!")
        turn += 1
        time.sleep(4)
        continue
    
    currentMessage = ""
    
    if turn % 2 == 0:
        currentMessage = ut.attack(cardPlayed, botCard, turn) if cardPlayed["NAME"] != "Rest" else f"{player.getName()} [green]rested[/green] their weary bones."
        if botCard["HP"] <= 0 and botCard["NAME"] != "Rest":
            print(f"{bot.getName()} lost {botCard['NAME']}")
            history.append(f"{bot.getName()} lost {botCard['NAME']}")
            bot.addToGraveyard(botCard)
    else:
        currentMessage = ut.attack(botCard, cardPlayed, turn) if botCard["NAME"] != "Rest" else f"{bot.getName()} [red]rested[/red] their weary bones."
        if cardPlayed["HP"] <= 0 and cardPlayed["NAME"] != "Rest":
            print(f"{player.getName()} lost {botCard['NAME']}")
            history.append(f"{player.getName()} lost {botCard['NAME']}")
            player.addToGraveyard(cardPlayed)
    
    rich.print(currentMessage)
    time.sleep(4)
    history.append(currentMessage)
    
    turn += 1