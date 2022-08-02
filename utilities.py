import rich
import time

def attack(card1: dict, card2: dict):
    dialogue = {
        "Wolf": "swipes",
        "Brute": "punches",
        "Wizard": "curses",
        "Goblin": "nibbles",    #TODO change this
        "Knight": "stabs",
        "Dragon": "attacks",    #TODO change this
        "Mage": "casts",
        "Peasant": "hits",
        "Paladin": "swears"     #TODO change this     
        }
    
    rich.print(f"The [green italic] {card1['NAME']} [/green italic] {dialogue[card1['NAME']]} the [red italic] {card2['NAME']}[/red italic].")

def printout(s: str, colour: str = "black"):
    sl = f"[{colour}]hey"
    rich.print(sl)
    for c in s:
        rich.print(c, end="", flush=True)
        time.sleep(0.8/len(s))
        

