# Twilight
A turn based card game. Requires the Python module `rich` to run.

## General gameplay
You and the bot are given 2 cards randomly from a pool of available cards, and also a rest card. The game ends when a player has only the rest card left.

## Attacking
To attack, simply type the name of the card that you wish to play. <i>Make sure you got enough mana to cover it!</i> The bot will proceed to also pick a card. You will attack the bots card. If the bots card hp drops below 0, they will lose the card and it will leave for the graveyard. And your mana will drop by the cost of the card you played. 

## Defending
To defend, simply type the name of the card that you wish to play. You will need to spend mana to prepare your defences. The bot will also pick a card to play, and your card will lose hp based on the bots card damage.

## Resting
If you choose to rest during an attack cycle, you wont send out an attack, and wont lose any mana. The bot will lose mana due to them over preparing their defences. Your party will gain 2 hp.

If you choose to rest during a defence, due to not having enough mana to play a card, or to prepare to play a powerful card, the bots card will proceed to deal damage to every single member in your party. Devasting blow!

If you <i>and</i> the bot decide to rest, you will agree to a truce for the day.  No one will lose mana, and both parties will gain 2 hp.

## Mana
Mana is the lifeblood of twilight. You need it to attack, and defend. And spending it foolishly is a sure way to lose the battle. Every card has a cost associated with it, and every time you play that card, you will lose that amount of mana.

The daily mana gain is on a three day cycle.
You will gain 1 mana the first day, 2 mana the second day, and 3 mana the third day, and then it resets to 1 mana for the fourth day.
