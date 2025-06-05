class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0
        self.__litros = 0
    def set_destino(self,v):
            if v < (): raise ValueError("Você precisa informar algo")
            self.__destino = v
    def set_distancia(self,v):
         if v < 0: raise ValueError("A distância não pode ser negativa")
         self.__distancia = v
    def set_litros(self,v):
         if v < 1: raise ValueError("O litro não pode ser negativo")
         self.__litros = v
    def get_destino(self):
         return self.__destino
    def get_distancia(self):
         return self.__distancia
    def get_litros(self):
         return self.__litros
    def  consumo(self):
         return self.__distancia / self.__litros
class ViagemUI:
     @staticmethod
     def menu():
         op = int(input("Informe uma opção: 1-Calcular, 2-Fim"))
         return op
     @staticmethod
     def main():
          op = 0
          while op != 2:
           op = ViagemUI.menu()
           if op == 1: ViagemUI.menu()
     @staticmethod
     def viagem():
          x = Viagem()
          
                     
           