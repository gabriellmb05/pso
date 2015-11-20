__author__ = 'gabriel'

from funcoes import *

class Bobina:
    def __init__(self, ordem, candidatas):
        self.ordem_saida = ordem
        self.candidatas = candidatas

    def print_bobina(self):
        print("ordem_saida: ", self.ordem_saida, "\n")
        print("candidatas: ", self.candidatas, "\n")

    def escolhe_candidata(self, patio):

        elemento = sorteia_elem_lista(self.candidatas)
        i , j = patio.busca_placa(elemento)
        if(patio.pilhas[i].sequenciada == False):
            return elemento, i , j

        elif(len(self.candidatas) > 1):
            if(elemento in self.candidatas):
                self.candidatas.remove(elemento)
            return self.escolhe_candidata( patio)
        else:
            self.candidatas.remove(elemento)
            return -1

    def retira_candidata(self, placa_atual):
        if(placa_atual in self.candidatas):
            self.candidatas.remove(placa_atual)


    def inseri_candidatas(self, candidatas):
        self.candidatas = [candidatas]


