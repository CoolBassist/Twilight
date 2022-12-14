import rich
from rich.panel import Panel
import random
import time

def attack(card1: dict, card2: dict, turn: int, restAttack: bool = False):
    dialogue = {
        "Rest": "You shouldnt see this",
        "Brute": "punches",
        "Wizard": "curses",
        "Goblin": "nibbles",
        "Knight": "stabs",
        "Dragon": "incinerates",
        "Mage": "casts",
        "Peasant": "hits",
        "Paladin": "charges",
        "Archer": "shoots",
        "Bowman": "pierces",
        "Assassin": "backstabs",
        "Bear": "swipes"  
    }
    
    if restAttack:
        card2["HP"] -= card1["DMG"]
        return
    
    primaryColour, secondaryColour = ("green", "red") if turn % 2 == 0 else ("red", "green")
    damage = random.choice(list(range(card1["DMG"]-1, card1["DMG"]+2)))
    
    typeOfHit = random.choice(["miss"] + ["normal"]*3 + ["critical"])
    message = None
    
    match typeOfHit:
        case "miss":
            message = f"[{primaryColour}]{card1['NAME']}[/{primaryColour}] missed the [{secondaryColour}]{card2['NAME']}[/{secondaryColour}]!"
        case "normal":
            message = f"The [{primaryColour} italic] {card1['NAME']} [/{primaryColour} italic] {dialogue[card1['NAME']]} the [{secondaryColour} italic] {card2['NAME']}[/{secondaryColour} italic] for [white on red]{damage}[/white on red] damage!"
            card2["HP"] -= damage        
        case "critical":
            damage = int(damage*1.5)
            message = f"The [{primaryColour} italic] {card1['NAME']} [/{primaryColour} italic] {dialogue[card1['NAME']]} the [{secondaryColour} italic] {card2['NAME']}[/{secondaryColour} italic] for [white on red][underline]CRTITICAL[/underline] {damage}[/white on red] damage!"
            card2["HP"] -= damage  
       
    return message

def printHistory(history: list) -> None:
    title = "..." if len(history) > 5 else None
    message = ""
    
    for i in history[-5:]:
        message += i + "\n"
        
    for i in range(len(history), 5):
        message += "\n"
    
    rich.print(Panel(f"{message[:-1]}",subtitle_align="center", title=title, subtitle="History"))
    print()

def printout(s: str, nl: bool = True):
    for c in s:
        rich.print(c, end="", flush=True)
        time.sleep(0.05)
    print() if nl else None
        

