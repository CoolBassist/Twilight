from turtle import hideturtle
from cards import Cards
from player import Player
import utilities as ut
import rich
from rich.columns import Columns
from rich.panel import Panel
import time
from rich.prompt import Prompt
from rich.progress import track
import os

os.system("cls")
rich.print(Panel("Twilight",subtitle_align="center" ,subtitle="A turn-based card game"))
print()

rich.print("[cyan]Court Squire [/cyan]: Welcome! You must be the new king of this land. Can I trouble you for your name? ")
player = Player(Prompt.ask("[green]You[/green]: Hello squire. Of course, my name is King").capitalize())
rich.print(f"[cyan]Court Squire [/cyan]: Ah yes {player.getName()}! There is trouble brewing in the far off land that is ruled over by your enemy. I can't remember their name...")
bot = Player(Prompt.ask("[green]You[/green]: Ah yes, I know them, they are called King").capitalize())
rich.print(f"[cyan]Court Squire [/cyan]: Yes! King {bot.getName()}! That was it! You must go now my liege... ")

time.sleep(4)

for i in track(range(50), description="Preparing for battle..."):
    time.sleep(0.1)  # Simulate work being done



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
    
    if turn%2 == 1 and cardPlayed["NAME"] == "Rest":
        party = player.getHand()[1:]
        for i in party:
            ut.attack(botCard, i, turn)
            if i["HP"] <= 0:
                player.addToGraveyard(i)
        
        rich.print(f"[red]{bot.getName()}[/red] attacks the entire party while [green]{player.getName()}[/green] was resting for [white on red]{botCard['DMG']}[/white on red] damage!")
        history.append(f"[red]{bot.getName()}[/red] attacks the entire party while [green]{player.getName()}[/green] was resting for [white on red]{botCard['DMG']}[/white on red] damage!")
        turn += 1
        time.sleep(4)
        continue

    if turn%2 == 0 and botCard["NAME"] == "Rest":
        party = bot.getHand()[1:]
        for i in party:
            ut.attack(cardPlayed, i, turn)
            if i["HP"] <= 0:
                bot.addToGraveyard(i)
        
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
    
if player.isLost():
    rich.print("You have fallen..")
    time.sleep(6)
    rich.print(f"Your kingdom falls around you as {bot.getName()} takes your crown and proclaims himself the ruler of the land.")
    rich.print("You fought your best and it was all for naught...")
else:
    rich.print("You have risen..")
    time.sleep(6)
    rich.print(f"You take {bot.getName()}'s crown and place it on your head. You have expanded your kingdom, and built it on the land of your enemies.")
    rich.print("There is no limit to your power...")
