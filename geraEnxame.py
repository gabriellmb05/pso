__author__ = 'gabriel'


from Enxame import *
from geraParticula import *
import copy




def geraEnxame(patio, demanda, qtdParticulas):

    lstParticulas = []
    cont = 0
    while(cont < qtdParticulas):

        p = geraParticula(copy.deepcopy(patio), copy.deepcopy(demanda))
        if(p != None):
            lstParticulas.append(p)
            if(cont == 0):
                melhor_part = lstParticulas[0]
            else:
                if(p.custo < melhor_part.custo):
                    melhor_part = p
            cont+=1
    enxame = Enxame(qtdParticulas,patio, demanda, melhor_part, lstParticulas)

    return enxame








