__author__ = 'gabriel'


from leitura import *
from Pso import *
import copy
from geraEnxame import *
from Particula import *

def main():

    patio = monta_patio()
    patio.print_patio()
    demanda = monta_saida()

    #e1 = geraEnxame(patio, demanda, 10000)
    #e1.print_enxame()
    #executa_pso(e1, 2, 2, 0.9)
    #e1.print_enxame()
    #patio.print_patio()
    p = geraParticula(copy.deepcopy(patio), copy.deepcopy(demanda))
    p.print_particula()
    #p.print_particula()
    #patio.print_patio()
    #e1.print_enxame()
    p.movimenta_particula_vel(copy.deepcopy(patio))
    p.calcula_custo()
    p.print_particula()

main()
