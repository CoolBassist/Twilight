class Cards():

    @staticmethod
    def getCards() -> dict:
        card_map = {
            1: {"NAME": "Rest",     "DMG": 0,   "HP": 0,    "COST": 0},
            2: {"NAME": "Brute",    "DMG": 3,   "HP": 20,   "COST": 6},
            3: {"NAME": "Wizard",   "DMG": 7,   "HP": 10,   "COST": 4},
            4: {"NAME": "Goblin",   "DMG": 4,   "HP": 5,    "COST": 1},
            5: {"NAME": "Knight",   "DMG": 4,   "HP": 10,   "COST": 3},
            6: {"NAME": "Dragon",   "DMG": 6,   "HP": 15,   "COST": 5},
            7: {"NAME": "Mage",     "DMG": 4,   "HP": 15,   "COST": 3},
            8: {"NAME": "Peasant",  "DMG": 2,   "HP": 4,    "COST": 2},
            9: {"NAME": "Paladin",  "DMG": 5,   "HP": 15,   "COST": 5},
            10:{"NAME": "Archer",   "DMG": 5,   "HP": 4,    "COST": 2},
            11:{"NAME": "Bowman",   "DMG": 7,   "HP": 6,    "COST": 4},
            12:{"NAME": "Assassin", "DMG": 7,   "HP": 4,    "COST": 3},
            13:{"NAME": "Bear",     "DMG": 4,   "HP": 6,    "COST": 3}
        }

        return card_map
    
#{"NAME": "", "DMG": 0, "HP": 0, "COST": 0}