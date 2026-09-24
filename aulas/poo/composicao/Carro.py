# COMPOSIÇÃO
class Carro:
    def __init__(self, modelo, motor):
        self.__modelo = modelo # Camaro, Celta, BYD Dolphin
        self.motor = Motor(motor) # TEM UM MOTOR -> instanciando a classe Motor, logo, tenho acesso aos metodos dessa classe sem precisar de herança

    def acelerar(self):
        print(f'O carro {self.__modelo} acelerou')

    def quebrar(self):
        print(f'O carro {self.__modelo} quebrou')
        self.motor.estado_motor = "quebrado"

class Motor:
    def __init__(self, tipo_motor):
        self.__tipo_motor = tipo_motor # V8, V6...
        self.__estado_motor = "funcionando"

    @property
    def tipo_motor(self):
        return self.__tipo_motor

    @property
    def estado_motor(self):
        return self.__estado_motor

    @estado_motor.setter
    def estado_motor(self, value):
        self.__estado_motor = value

    def arrumar_motor(self):
        if self.estado_motor == "quebrado":
            print(f"O motor {self.tipo_motor} foi concertado")
            self.estado_motor = "funcionando"
        else:
            print("Motor concertado")




carro_joao = Carro("Camaro", "V8")
carro_marcelo = Carro("BYD", "Eletrico")
carro_italo =  Carro("Palio", "V6")

carro_joao.quebrar()
carro_marcelo.quebrar()
carro_italo.acelerar()


print(f"Estado atual do carro: {carro_joao.motor.estado_motor}")
print(f"Estado atual do carro: {carro_marcelo.motor.estado_motor}")
print(f"Estado atual do carro: {carro_italo.motor.estado_motor}")
