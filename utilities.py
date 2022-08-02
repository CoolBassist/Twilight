import rich
import random
import time

def attack(card1: dict, card2: dict, turn: int, restAttack: bool = False):
    dialogue = {
        "Rest": "You shouldnt see this",
        "Brute": "punches",
        "Wizard": "curses",
        "Goblin": "nibbles",    #TODO change this
        "Knight": "stabs",
        "Dragon": "attacks",    #TODO change this
        "Mage": "casts",
        "Peasant": "hits",
        "Paladin": "swears",     #TODO change this 
        "Archer": "shoots"    
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

def printout(s: str, nl: bool = True):
    for c in s:
        rich.print(c, end="", flush=True)
        time.sleep(0.05)
    print() if nl else None
        

