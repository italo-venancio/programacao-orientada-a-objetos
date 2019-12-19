class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self):
        self.tamanho_lado + 1
    def retornar_valor_lado(self):
        return self.tamanho_lado
    def calcular_area(self):
        return (tamanho_lado**2)