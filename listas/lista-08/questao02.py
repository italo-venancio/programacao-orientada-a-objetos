class Computador:
    def __init__(self, marca, modelo, componentes, anos_uso, cor):
        self.marca = marca
        self.modelo = modelo
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor

    def mostrarMarca(self):
        print(self.marca)

    def adicionarComponentes(self):
        self.componentes.append(novo_comp)

    def mostrarComponentes(self):
        print(self.componentes)

    def mostrar_anos_uso(self):
        if self.anos_uso < 6:
            print(self.anos_uso)
        elif self.anos_uso >= 6:
            print("Seu computador esta tao velho que te problemas de junta... junta tudo e joga fora...")
    
    def envelhecer(self):
        self.anos_uso + 1

comp1 = Computador("Acme", "Premium", "monitor", 3, "cinza")
