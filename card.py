# Create YUGIOH Card object
from enum import Enum
from cardtype import CardType
from atributotype import AttributeType
from position import Position
from player import Player
from ubicacion import Ubicacion
import random as rd

class Card:
    def __init__(this, name, description, cardtype, attribute, atk, defense):
        this.name = name
        this.description = description
        this.cardtype = cardtype
        this.attribute = attribute
        this.atk = atk
        this.defense = defense

    def __str__(this):
        return f"Name: {this.name}\nDescription: {this.description}\nCard Type: {this.cardtype.name}\nAttribute: {this.attribute.name}\nATK: {this.atk}\nDEF: {this.defense}"

    # VERIFY SETTERS AND CREATE GETTERS TOO
    # def setATK(this, atk):
    #     this.atk = atk

    # VERIFICAR QUE AL TENER ATK -1 se ENVÍA AL CEMENTERIO ESA CARTA
    # HAY QUE VERIFICAR SI LA CARTA ENEMIGA SE ENCUENTRA EN MODO DE DEFENSA O EN MODO DE ATAQUE
    def combat(this, enemigo):
        if this.atk < enemigo.atk:
            this.atk = -1
            return False
        elif this.atk == enemigo.atk:
            this.atk = -1
            enemigo.atk = -1
            return True
        else:
            enemigo.atk = -1
            return True




# INSTANCIAS
# object instance
c1 = Card("Sky Striker ACE - Raye", "Random desc", CardType.MONSTER, AttributeType.DARK, 1500, 1500)
print(c1)
c2 = Card("Mago Oscuro", "x", CardType.MONSTER, AttributeType.DARK, 2500, 1500)

# player instance
p1 = Player("Etienne") #<----input("ingrese su nombre: ")
print(p1)

x = c1.combat(c2)

print(f"\n{x}")
print(f"Ataque de {c1.name} es de: {c1.atk}")
print(f"Ataque de {c2.name} es de: {c2.atk}")
