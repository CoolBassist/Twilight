from cards import Cards
from rich.console import Console
from rich.table import Table
import random

class Player():
    def __init__(self, name: str, isBot: bool = False):
        self.__hand = [Cards.getCards()[6]]
        self.__hand += [Cards.getCards()[random.randint(1, 5)] for _ in range(2)]
        self.__graveyard = []
        self.__name = name
        self.__isBot = isBotd
    
    def getHand(self) -> list:
        return self.__hand

    def printHand(self) -> None:
        table = Table("Name", "HP", "Damage", "Cost", title=f"{self.__name}'s Hand")
        for card in self.__hand:
            table.add_row(card["NAME"], str(card["HP"]), str(card["DMG"]), str(card["COST"]))
        
        console = Console()
        console.print(table)
    
    def getGraveyard(self) -> list:
        return self.__graveyard
    
    def getCard(self, card_name: str = ""):
        for i in self.__hand:
            if i["NAME"] == card_name.casefold():
                return i
        
        return False
