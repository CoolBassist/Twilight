from cards import Cards
import rich
from rich.table import Table
import random

class Player():
    def __init__(self, name: str, isBot: bool = False):
        self.__hand = [Cards.getCards()[1]]
        self.__graveyard = []
        self.addRandomCard()
        self.addRandomCard()
        self.__name = name
        self.__mana = 5
    
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
            hpColour = None
            maxHP = None
            for tcard in Cards.getCards().values():
                if card["NAME"] == tcard["NAME"]:
                    maxHP = tcard["HP"]

            if maxHP < card["HP"]:
                hpColour = "cyan"
            elif maxHP*0.66 < card["HP"] <= maxHP:
                hpColour = "green"
            elif maxHP*0.33 < card["HP"] <= maxHP*0.6:
                hpColour = "orange3"
            else:
                hpColour = "red"
                
            table.add_row(card["NAME"], f"[{hpColour}]{card['HP']}[/{hpColour}]", str(card["DMG"]), str(card["COST"]))
        
        return table
    
    def getGraveyard(self) -> list:
        return self.__graveyard
    
    def getName(self) -> str:
        return self.__name
    
    def addRandomCard(self):
        randCard = None
        while (randCard := Cards.getCards()[random.randint(2, len(Cards.getCards()))]) in self.__hand or (randCard in self.__graveyard):
            pass
        self.__hand.append(randCard)
    
    def getCard(self, card_name: str):        
        for i in self.__hand:
            if i["NAME"].casefold() == card_name.casefold() and i["COST"] <= self.__mana:
                self.__mana -= i["COST"]
                return i
        
        return False
    
    def getRandomCard(self) -> dict:
        randCard = None
        while (randCard := random.choice(self.__hand))["COST"] > self.__mana:
            pass
        
        self.__mana -= randCard["COST"]
        rich.print(f"{self.__name} played {randCard['NAME']}")

        return randCard
