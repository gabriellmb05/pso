__author__ = 'gabriel'

from geraParticula import *
import Pso


class Enxame:

    def __init__(self, qtd_particulas, patio, demanda, melhor_particula, particulas):
        self.qtd_particulas = qtd_particulas
        self.patio = patio
        self.demanda = demanda
        self.particulas = particulas
        self.melhor_particula = melhor_particula

    def print_enxame(self):
        print("qtd_particulas: ", self.qtd_particulas, "\n")
        self.patio.print_patio()
        Pso.print_demanda(self.demanda)
        print_particulas(self.particulas)
        print("melhor_particula: \n")
        self.melhor_particula.print_particula()

    def atualiza_enxame(self, particula):
        if(particula.custo < self.melhor_particula.custo):
            self.melhor_particula = particula






