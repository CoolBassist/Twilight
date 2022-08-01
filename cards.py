class Cards():

    @staticmethod
    def getCards() -> dict:
        card_map = {
            1: {"NAME": "Tank",     "DMG": 3,   "HP": 20,   "COST": 6},
            2: {"NAME": "Wizard",   "DMG": 7,   "HP": 10,   "COST": 4},
            3: {"NAME": "Goblin",   "DMG": 4,   "HP": 5,    "COST": 1},
            4: {"NAME": "Knight",   "DMG": 4,   "HP": 10,   "COST": 3},
            5: {"NAME": "Dragon",   "DMG": 6,   "HP": 15,   "COST": 5},
            6: {"NAME": "Wolf",     "DMG": 1,   "HP": 4,    "COST": 0}
        }

        return card_map