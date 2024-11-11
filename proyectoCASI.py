import random

class Carta:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class CartaMonstruo(Carta):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo, atributo):
        super().__init__(nombre, descripcion)
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo
        self.atributo = atributo
        self.en_defensa = False
        self.boca_abajo = False
    def cambiar_posicion(self):
        if not self.boca_abajo:
            self.en_defensa = not self.en_defensa

class CartaMagica(Carta):
    def __init__(self, nombre, descripcion, incremento, tipo_objetivo):
        super().__init__(nombre, descripcion)
        self.incremento = incremento
        self.tipo_objetivo = tipo_objetivo

class CartaTrampa(Carta):
    def __init__(self, nombre, descripcion, atributo_efectivo):
        super().__init__(nombre, descripcion)
        self.atributo_efectivo = atributo_efectivo

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos_vida = 4000
        self.mazo = []
        self.mano = []
        self.tablero = {"monstruos": [None] * 3,"magicas_trampas": [None] * 3}

    def robar(self):
        if self.mazo:
            carta = self.mazo.pop()
            self.mano.append(carta)

    def jugar_carta(self, carta, en_defensa=False):
        if isinstance(carta, CartaMonstruo):
            if None in self.tablero["monstruos"]:
                indice = self.tablero["monstruos"].index(None)
                self.tablero["monstruos"][indice] = carta
                carta.en_defensa = en_defensa
                carta.boca_abajo = en_defensa
        elif isinstance(carta, (CartaMagica, CartaTrampa)):
            if None in self.tablero["magicas_trampas"]:
                indice = self.tablero["magicas_trampas"].index(None)
                self.tablero["magicas_trampas"][indice] = carta

    def recibir_dano(self, cantidad):
        self.puntos_vida = max(self.puntos_vida - cantidad, 0)

class Juego:
    def __init__(self, jugador):
        self.jugador = jugador
        self.maquina = Jugador("Máquina")
        self.turno_jugador = random.choice([self.jugador, self.maquina])
        self.turno_numero = 1
        self.inicializar_mazos()

    def inicializar_mazos(self):
        pass

    def fase_tomar_carta(self):
        self.turno_jugador.robar()

    def fase_principal(self):
        if self.turno_jugador == self.jugador:
            pass
        else:
            self.logica_maquina()

    def logica_maquina(self):
        for carta in self.maquina.mano:
            if isinstance(carta, CartaMonstruo) and None in self.maquina.tablero["monstruos"]:
                self.maquina.jugar_carta(carta)
            elif isinstance(carta, (CartaMagica, CartaTrampa)) and None in self.maquina.tablero["magicas_trampas"]:
                self.maquina.jugar_carta(carta)

    def fase_batalla(self):
        if self.turno_numero > 1:
            if self.turno_jugador == self.maquina:
                self.logica_batalla_maquina()

    def logica_batalla_maquina(self):
        for atacante in self.maquina.tablero["monstruos"]:
            if atacante and not atacante.en_defensa:
                if any(self.jugador.tablero["monstruos"]):
                    defensor = random.choice([m for m in self.jugador.tablero["monstruos"] if m])
                    self.resolver_batalla(atacante, defensor)
                else:
                    self.jugador.recibir_dano(atacante.ataque)

    def resolver_batalla(self, atacante, defensor):
        pass

    def cambiar_turno(self):
        self.turno_jugador = self.jugador if self.turno_jugador == self.maquina else self.maquina
        self.turno_numero += 1

    def jugar_turno(self):
        self.fase_tomar_carta()
        self.fase_principal()
        self.fase_batalla()
        self.cambiar_turno()
