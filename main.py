class Asiento:
    def __init__(self, color:str, precio: int, registro: int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarcolor(self, color: str):
        if color == "rojo" or "verde" or "amarillo" or "negro" or "blanco":
            self.color = color


class Motor:
    def __init__(self, numerocilindros: int, tipo: str, registro: int):
        self.numerocilindros = numerocilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarregistro(self, registro: int):
        self.registro = registro
    
    def asignartipo(self, tipo: int):
        if tipo == "electrico" or "gasolina":
            self.tipo = tipo

class auto:
    cantidadcreados = 0

    def __init__(self, modelo: str, precio:int, asientos: list[Asiento], marca:str, motor: Motor, registro: int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = Asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro
        auto.cantidadcreados += 1

    def cantidadasientos(self) -> int:
        contador = 0
        for i in self.asientos:
            if isinstance(i, Asiento):
                contador += 1
            return contador
        
    def verificarintegridad(self) -> str:
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if asiento.registro != self.motor.registro:
                    return "Las piezas no son originales"
                elif asiento.registro != self.registro:
                    return "las piezas no son originales"
                elif self.registro != self.motor.registro:
                    return "las piezas no son origales"
                else:
                    return "Auto original"