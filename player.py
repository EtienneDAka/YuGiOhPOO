# CREATE PLAYER AS OBJECT
class Player:
    life = 8000
    def __init__(this, name):
        this.name = name

    def __str__(this):
        return f"{this.name}\nTOTAL LP: {this.life}"