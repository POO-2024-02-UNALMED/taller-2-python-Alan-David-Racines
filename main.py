class Asiento:
    colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
    
    def __init__(self, color: str, precio: int, registro: int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color: str):
        if color in Asiento.colores:
            self.color = color

class Motor:
    def __init__(self, numerocilindros: int, tipo: str, registro: int):
        self.numerocilindros = numerocilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro: int):
        self.registro = registro
    
    def asignarTipo(self, tipo: str):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo
            
class Auto:
    cantidadcreados = 0

    def __init__(self, modelo: str, precio:int, asientos: list[Asiento], marca:str, motor: Motor, registro: int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadcreados += 1

    def cantidadAsientos(self) -> int:
        contador = 0
        for i in self.asientos:
            if isinstance(i, Asiento):
                contador += 1
        return contador
        
    def verificarIntegridad(self) -> str:
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