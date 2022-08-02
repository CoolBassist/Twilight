import rich
import time

def attack(card1: dict, card2: dict, turn: int):
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
    
    card2["HP"] -= card1["DMG"]
    
    primaryColour, secondaryColour = ("green", "red") if turn % 2 == 0 else ("red", "green")
    
    return f"The [{primaryColour} italic] {card1['NAME']} [/{primaryColour} italic] {dialogue[card1['NAME']]} the [{secondaryColour} italic] {card2['NAME']}[/{secondaryColour} italic] for [white on red]{card1['DMG']}[/white on red] damage!"
    
def printout(s: str, colour: str = "black"):
    sl = f"[{colour}]hey"
    rich.print(sl)
    for c in s:
        rich.print(c, end="", flush=True)
        time.sleep(0.8/len(s))
        

