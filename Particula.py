__author__ = 'gabriel'

import math
import random


class Particula:
    def __init__(self, movimentacoes, custo, ordem_saida, velocidade, placas_saida):
        self.movimentacoes=movimentacoes
        self.melhor_movimentacoes = movimentacoes
        self.melhor_custo=custo
        self.custo = custo
        self.ordem_saida = ordem_saida
        self.velocidade = velocidade
        self.placas_saida = placas_saida

    def print_particula(self):
        print("movimentações: ", self.movimentacoes, "\n")
        print("custo: ", self.custo, "\n")
        print("melhor_movimentações: ", self.melhor_movimentacoes, "\n")
        print("melhor_custo: ", self.melhor_custo, "\n")
        print("ordem_saida: ", self.ordem_saida, "\n")
        print("velocidade: ", self.velocidade, "\n")
        print("placas_saida : ", self.placas_saida, "\n")

    def calcula_custo(self):
        custo = 0
        for mov_bobina in self.movimentacoes:
            for movimento in mov_bobina:
                custo+= math.fabs(movimento[0] - movimento[1])
        self.custo = custo

    def atualiza_custo(self):

        if(self.custo < self.melhor_custo):
            self.melhor_custo = self.custo
            self.melhor_movimentacoes = self.movimentacoes

    def nova_velocidade(self, mparticula, c1, c2, w):

        nova_vel = []
        for i in range(len(self.velocidade)):
            vel = round(w*self.velocidade[i] + c1*random()*(self.melhor_custo - self.custo) + c2*random()*(mparticula.custo - self.custo))
            nova_vel.append(vel)
        self.velocidade = nova_vel

    def movimenta_particula_vel(self, patio):

        lst_movimentacoes = []

        for i in range(len(self.movimentacoes)):
            j, k = patio.busca_placa(self.placas_saida[i])
            lst_movimentacoes_pilha = patio.movimenta_placas_entre_pilhas_vel( j, k, self.velocidade[i], self.movimentacoes[i])
            if(lst_movimentacoes_pilha != -1):
                lst_movimentacoes.append(lst_movimentacoes_pilha)
            else:
                break
        if(lst_movimentacoes_pilha != -1):
            self.movimentacoes = lst_movimentacoes
