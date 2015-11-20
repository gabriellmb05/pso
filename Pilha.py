__author__ = 'Gabriel'

TAM_MAX = 5
from geraParticula import *

class Pilha():
    def __init__(self):
        self.sequenciada=False
        self.placas=[]

    def add_placa(self,placa):
        self.placas.append(placa)

    def imprime(self):
        for i in range(len(self.placas)):
            print(self.placas[i], end=" ")

    def desempilha(self):
        if(len(self.placas) == 0):
            print("Pilha sem placas para desempilhar")
        else:

            placa = self.placas[-1]
            self.placas = self.placas[0:-1]
            return placa

    def empilha(self, placa):

        if(len(self.placas) == TAM_MAX):
            print("Pilha cheia")
        else:
            self.placas.append(placa)

    #def sequencia_pilha2(self, patio, j, vel, movimento_bobina):


    def qtd_placas_acima(self, j):

        qtd_placas = len(self.placas) - 1
        qtd_placas_tirar = qtd_placas - j

        return qtd_placas_tirar

