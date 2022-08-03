from player import Player
import utilities as ut
import rich
from rich.columns import Columns
from rich.panel import Panel
import time
from rich.prompt import Prompt
from rich.progress import track
import os

dev = True

os.system("cls")

if not dev:
    rich.print(Panel(f"Introduction",subtitle_align="center", title="Twilight", subtitle="A turn-based card game"))
    print()

    rich.print("[cyan]Messenger[/cyan]: ")
    ut.printout("Hello my liege. I am a messenger from an enemy kingdom. Can I know whose land I am residing in?")
    time.sleep(2)
    print()

    rich.print("[green]You[/green]: ")
    ut.printout("Of course, messenger, I am King", nl=False)
    player = Player(Prompt.ask().capitalize())
    time.sleep(2)
    print()

    rich.print(f"[cyan]Court Squire [/cyan]: ")
    ut.printout(f"Oh King {player.getName()}! Our king has great honour and wants to inform you to prepare for war over this very land.")
    time.sleep(2)
    print()

    rich.print("[green]You[/green]: ")
    ut.printout("And which king might that be?")
    time.sleep(2)
    print()

    rich.print("[cyan]Court Squire [/cyan]: ")
    ut.printout("Our king is called", nl=False)
    bot = Player(Prompt.ask().capitalize())
    time.sleep(2)
    print()

    rich.print("[green]You[/green]: ")
    ut.printout(f"Then tell King {bot.getName()} to prepare for war...")

    time.sleep(4)

    for i in track(range(50), description="Preparing for battle..."):
        time.sleep(0.1)
else:
    player = Player("Player")
    bot = Player("Bot")
turn = 0

history = []

while not player.isLost() and not bot.isLost():
    os.system("cls")
    rich.print(Panel(f"Day {int((turn+2)/2)}",subtitle_align="center", title="Twilight", subtitle="A turn-based card game"))
    print()
    
    player.addMana((turn-1)%3 + 1) if turn > 0 else None
    bot.addMana((turn-1)%3 + 1) if turn > 0 else None
    
    columns = Columns([player.getHandTable(), bot.getHandTable()], equal=True, expand=True)
    rich.print(columns)
    
    print("...") if len(history) > 5 else None
    
    for i in history[-5:]:
        rich.print(i)
        
    print()
        
    rich.print(f"Play a card to {'attack' if turn%2 == 0 else 'defend against'} [red]{bot.getName()}[/red]:")

    while (not (cardPlayed := player.getCard(input(">> ")))):
        pass
    
    botCard = bot.getRandomCard()
    
    if cardPlayed["NAME"] == "Rest" and botCard["NAME"] == "Rest":
        rich.print(f"[green]{player.getName()}[/green] and [red]{bot.getName()}[/red] have agreed to a temporary peace treaty, and both parties gain health...")
        party = player.getHand()[1:] + bot.getHand()[1:]
        
        for i in party:
                i["HP"] += 2
        
        history.append(f"[green]{player.getName()}[/green] and [red]{bot.getName()}[/red] have agreed to a temporary peace treaty, and both parties gain health...")
        turn += 1
        time.sleep(4)
        continue
    
    if cardPlayed["NAME"] == "Rest":
        party = player.getHand()[1:]
        if turn%2 == 1:
            
            partyLost = []

            for i in party:
                ut.attack(botCard, i, turn, restAttack=True)
                if i["HP"] <= 0:
                    partyLost.append(i["NAME"])
                    player.addToGraveyard(i)

            rich.print(f"[red]{bot.getName()}[/red] attacks the entire party while [green]{player.getName()}[/green] was resting for [white on red]{botCard['DMG']}[/white on red] damage! And killed {[name for name in partyLost]}!")
            history.append(f"[red]{bot.getName()}[/red] attacks the entire party while [green]{player.getName()}[/green] was resting for [white on red]{botCard['DMG']}[/white on red] damage! And killed {[name for name in partyLost]}!")
            turn += 1
            time.sleep(4)
            continue        
        else:
            for i in party:
                i["HP"] += 2
        
        
    
    if botCard["NAME"] == "Rest":
        party = bot.getHand()[1:]
        if turn%2 == 0:
            partyLost = []
        
            for i in party:
                ut.attack(cardPlayed, i, turn, restAttack=True)
                if i["HP"] <= 0:
                    partyLost.append(i["NAME"])
                    bot.addToGraveyard(i)
                turn += 1
            time.sleep(4)
            continue
        else:
            for i in party:
                i["HP"] += 2
        
    
    currentMessage = ""
    
    if turn % 2 == 0:
        currentMessage = ut.attack(cardPlayed, botCard, turn) if cardPlayed["NAME"] != "Rest" else f"{player.getName()} [green]rested[/green] their weary bones and the party gains health."
        if botCard["HP"] <= 0 and botCard["NAME"] != "Rest":
            print(f"{bot.getName()} lost {botCard['NAME']}")
            history.append(f"{bot.getName()} lost {botCard['NAME']}")
            bot.addToGraveyard(botCard)
    else:
        currentMessage = ut.attack(botCard, cardPlayed, turn) if botCard["NAME"] != "Rest" else f"{bot.getName()} [red]rested[/red] their weary bones and the party gains health."
        if cardPlayed["HP"] <= 0 and cardPlayed["NAME"] != "Rest":
            print(f"{player.getName()} lost {botCard['NAME']}")
            history.append(f"{player.getName()} lost {botCard['NAME']}")
            player.addToGraveyard(cardPlayed)
    
    rich.print(currentMessage)
    time.sleep(4)
    history.append(currentMessage)
    
    turn += 1
    
if player.isLost():
    ut.printout("You have fallen..")
    time.sleep(6)
    ut.printout(f"Your kingdom falls around you as {bot.getName()} takes your crown and proclaims himself the ruler of the land.")
    ut.printout("You fought your best and it was all for naught...")
else:
    ut.printout("You have risen..")
    time.sleep(6)
    ut.printout(f"You take {bot.getName()}'s crown and place it on your head. You have expanded your kingdom, and built it on the land of your enemies.")
    ut.printout("There is no limit to your power...")

"""
To implement:
    A spell stage every 5 days? swap cards, gain new card, etc
    Change colour of HP in hand table, depending if near full health, medium health, low health, and overcharged health.
    Maybe fix balances in cards?
    Make it obvious how much mana the user will be gaining per day
    Improve history section. Maybe a panel in the middle of the screen?
"""