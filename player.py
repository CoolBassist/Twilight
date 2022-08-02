from cards import Cards
import rich
from rich.table import Table
import random

class Player():
    def __init__(self, name: str, isBot: bool = False):
        self.__hand = [Cards.getCards()[1]]
        self.__hand += [Cards.getCards()[random.randint(2, len(Cards.getCards()))] for _ in range(2)]
        self.__graveyard = []
        self.__name = name
        self.__mana = 4
        self.__isBot = isBot
    
    def getHand(self) -> list:
        return self.__hand
    
    def getMana(self) -> int:
        return self.__mana
    
    def removeMana(self, amount: int) -> None:
        self.__mana -= amount
    
    def addMana(self, amount: int) -> None:
        self.__mana += amount
    
    def isLost(self) -> bool:
        return len(self.__hand) <= 1
        
    def addToGraveyard(self, card:dict) -> None:
        self.__graveyard.append(card)
        self.__hand.remove(card)

    def getHandTable(self) -> None:
        table = Table("Name", "HP", "Damage", "Cost", title=f"[underline]{self.__name}'s[/underline] Hand ([blue]{self.__mana}[/blue] mana)")
        for card in self.__hand:
            table.add_row(card["NAME"], str(card["HP"]), str(card["DMG"]), str(card["COST"]))
        
        return table
    
    def getGraveyard(self) -> list:
        return self.__graveyard
    
    def getName(self) -> str:
        return self.__name
    
    def getCard(self, card_name: str):        
        for i in self.__hand:
            if i["NAME"].casefold() == card_name.casefold() and i["COST"] <= self.__mana:
                self.__mana -= i["COST"]
                return i
        
        return False
    
    def addPerm(self):
        self.__hand = [Cards.getCards()[1]] + self.__hand
    
    def getRandomCard(self) -> dict:
        randCard = random.choice(self.__hand)
        while randCard["COST"] > self.__mana:
            randCard = random.choice(self.__hand)
        
        self.__mana -= randCard["COST"]
        rich.print(f"{self.__name} played {randCard['NAME']}")

        return randCard
