__author__ = 'gabriel'

import copy
from random import *

def executa_pso(enxame, c1, c2, w):

    x = 0
    while(x < 3000):

        for particula in enxame.particulas:
            enxame.atualiza_enxame(particula)
            particula.atualiza_custo()
            particula.nova_velocidade(enxame.melhor_particula, c1, c2, w)
            particula.movimenta_particula_vel(copy.deepcopy(enxame.patio))
            particula.calcula_custo()

    #print(enxame.melhor_particula.melhor_movimentacoes)
    #print(enxame.melhor_particula.melhor_custo)


def pilha_destino(patio, lst, porigem):

    for i in range(len(lst)):
        if(lst[i] == porigem or patio.pilhas[lst[i]].sequenciada ):
            del lst[i]

    if(lst != []):
        return lst[randint(0,len(lst) -1)]
    else:
        print("velocidade não permite movimentação")
        return -1

def retira_pilha_com_placa(lst_pilhas, i):

    for j in range(len(lst_pilhas)):
            if(lst_pilhas[j] == i):
                del lst_pilhas[j]
                break

def print_demanda(demanda):

    for bobina in demanda:
        print("------------------------------------")
        bobina.print_bobina()
    print("------------------------------------")
