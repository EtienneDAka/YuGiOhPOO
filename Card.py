from MonsterType import MonsterType
from MonsterAttribute import MonsterAttribute
from Position import Position

class Card:
    def __init__(self, name, description, position):
        self.name = name
        self.description = description
        self.position = position

    def __str__(self):
        return self.name

    def getPosition(self):
        return self.position.value

    def setPosition(self, position:Position):
        self.position = position

class MonsterCard(Card):
    def __init__(self, name, description, attack, defense, type: MonsterType, attribute: MonsterAttribute):
        super().__init__(name,description, Position.FACE_DOWN)
        self.attack = attack
        self.defense = defense
        self.type = type
        self.attribute = attribute
    
    def getAttack(self):
        return self.attack
    
    def getDefense(self):
        return self.defense
    
    def getMonsterType(self):
        return self.type.value

    def getMonsterAttribute(self):
        return self.attribute.value
    
    def setAttack(self, attack):
        self.attack = attack
    
    def setDefense(self, defense):
        self.defense = defense
    
    # COMPORTAMIENTO DE ATAQUE
    def perform_attack(self, enemy: 'MonsterCard', player_enemigo, player_self):
        # Check for trap card
        for card in player_enemigo.field[1]:
            if isinstance(card, TrapCard):
                if card.activate(self):
                    print(f"{self.name}'s attack is negated!")
                    player_enemigo.remove_magic_card(card)
                    return None  # Attack is stopped

        print(f"{self.name} attacks {enemy.name}!")

        if enemy.getPosition() == Position.FACE_UP_ATAQUE:
            if self.attack > enemy.getAttack():
                print(f"{self.name} destroys {enemy.name}.")
                dmg_real = self.attack - enemy.getAttack()
                player_enemigo.take_damage(dmg_real)
                return True
            elif self.attack == enemy.getAttack():
                print(f"{self.name} and {enemy.name} destroy each other!")
                return None
            else:
                print(f"{enemy.name} withstands the attack and destroys {self.name}.")
                dmg_real = enemy.getAttack - self.attack
                player_self.take_damage(dmg_real)
                return False

        elif enemy.getPosition() == Position.FACE_UP_DEFENSA or enemy.getPosition() == Position.FACE_DOWN:
            if self.getAttack() > enemy.getDefense():
                return True
            elif self.getAttack() == enemy.getDefense():
                return None
            elif self.getAttack() < enemy.getDefense():
                return False
    
    # String representation of Monster in console
    def __str__(self):
        return f"{self.name} ' - ' {self.attribute}\n{self.getMonsterType}\n{self.getMonsterType}\n{self.description}\nATK:/{self.attack} DEF/{self.defense}"
class SpellCard(Card):

    def __init__(self, name, description, affectsMonster: MonsterType, attackBoost, defenseBoost):
        super().__init__(name, description, Position.FACE_DOWN)
        self.affectsMonster = affectsMonster
        self.attackBoost = attackBoost
        self.defenseBoost = defenseBoost
        self.isActive = False

    def activate(self, target:MonsterCard):
        if target.getMonsterType() == self.affectsMonster.value:
            target.attack += self.attackBoost
            target.defense += self.defenseBoost
            return True
        return False
    
    def getEffect(self):
        return self.description
    

        


class TrapCard(Card):
    def __init__(self, name, description, affectsMonster: MonsterAttribute):
        super().__init__(name, description, Position.FACE_DOWN)
        self.isActive = False
        self.affectsMonster = affectsMonster

    def activate(self, attackingMonster:MonsterCard):
        if attackingMonster.attribute.value == self.affectsMonster.value:
            # negate attack from THAT monster
            self.isActive = True
            print(f"La carta trampa '{self.name}' es activada y niega el ataque de '{attackingMonster.name}'!")
            return True
        else:
            print(f"La carta trampa '{self.name}' no puede ser activado contra '{attackingMonster.name}'.")
            return False