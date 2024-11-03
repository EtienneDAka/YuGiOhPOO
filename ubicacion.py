# STATUS LOGIC - UBICACION EN EL JUEGO
from enum import Enum

class Ubicacion(Enum):
    HAND_ZONE = 0
    DECK_ZONE = 1
    EXTRA_DECK_ZONE = 2
    MAIN_MONSTER_ZONE = 3
    EXTRA_MONSTER_ZONE = 4
    SPELL_TRAP_ZONE = 5
    FIELD_ZONE = 6
    GRAVEYARD_ZONE = 7
    BANISHED_ZONE = 8
    