'''class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0
        self.__litros = 0
    def set_destino(self,v):
            if v < "": raise ValueError("Você precisa informar algo")
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
         op = int(input("Informe uma opção: 1-Calcular, 2-Fim: "))
         return op
     @staticmethod
     def main():
          op = 0
          while op != 2:
           op = ViagemUI.menu()
           if op == 1: ViagemUI.viagem()
     @staticmethod
     def viagem():
          x = Viagem()

          x.set_destino(input("Informe o destino da viagem:"))

          x.set_distancia(int(input("Informe a distância percorrida:")))

          x.set_litros(int(input("Informe a quantidade de litros de gasolina gasto:")))

          print(f"O consumo médio de combustível do automovel:{x.consumo():.2f} km/l")    

ViagemUI.main()
'''





class Pais:
    def __init__(self):
        self.__nome = ""
        self.__populacao = 0
        self.__area = 0.00
    def set_nome(self,v):
        if v == "": raise ValueError("Você precisa informar algum nome")
        self.__nome = v
    def set_populacao(self,v):
        if v < 0: raise ValueError(" A população não pode ser negativa")
        self.__populacao = v
    def set_area(self,v):
        if v <= 0: raise ValueError("A área deve ser maior que 0")
        self.__area = v
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__populacao / self.__area
class ParcialUI:
        @staticmethod
        def menu():
            op = int(input("informe uma opção: 1-Calcular, 2-Fim: "))
            return op
        def main():
            op = 0
            while op != 2:
                op = ParcialUI.menu()
                if op == 1 : 
        

        

