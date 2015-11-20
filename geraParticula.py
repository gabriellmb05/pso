__author__ = 'gabriel'

from Particula import *
from funcoes import *

TAM_MAX = 5

def geraParticula(patio, demanda):



    lstmovimentos, lstordem_saida, lstplacas_saida = gera_movimentacoes(patio, demanda)
    if(lstmovimentos != None):
        valor = custo(lstmovimentos)
        lstordem_saida.reverse()
        velocidade = velocidade_inicial(patio, demanda)
        p1 = Particula(lstmovimentos, valor, lstordem_saida, velocidade, lstplacas_saida)
        return p1
    else:
        print("Bobina ", demanda[lstordem_saida].ordem_saida," sem opções de placa no patio")
        return None


def gera_movimentacoes(patio, demanda):

    lstmovimentos = []
    lstordem_saida = []
    lstplacas_saida = []
    for i in range(len(demanda) -1, -1 , -1):
        placa_atual, k, j = demanda[i].escolhe_candidata(patio)
        if(placa_atual == -1):
            return None, i, None
        lstplacas_saida.append(placa_atual)
        retira_candidatas(demanda, placa_atual, i)
        lstordem_saida.append(k)
        lst_movimentos_pilha = patio.movimenta_placas_entre_pilhas(k, j)
        if(lst_movimentos_pilha != -1):
            lstmovimentos.append(lst_movimentos_pilha)
        else:
            return None
    return lstmovimentos, lstordem_saida, lstplacas_saida

def print_particulas(particulas):

        cont = 0
        for particula in particulas:
            print("------------------------------------")
            print("Particula ", cont, ":\n")
            particula.print_particula()
            cont+=1
        print("------------------------------------")

def velocidade_inicial(patio, lst):

    pilhas = len(patio.pilhas) -1
    lstvelocidade = []

    for i in lst:

        lstvelocidade.append(random.randint(0, pilhas - 1))

    lstvelocidade.reverse()

    return lstvelocidade

def retira_candidatas(demanda, placa_atual, i):

    for j in range(len(demanda) -1, -1 , -1):
        if(j != i):
            demanda[j].retira_candidata(placa_atual)
        else:
            demanda[j].inseri_candidatas(placa_atual)

def custo(lst):

    custo = 0
    for i in lst:
        for tupla in i:
            custo+= math.fabs(tupla[0] - tupla[1])

    return custo

