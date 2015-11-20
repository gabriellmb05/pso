__author__ = 'Gabriel'

from funcoes import *
class Patio :

    def __init__(self):
        self.pilhas=[]

    def add_pilha(self,pilha):
        self.pilhas.append(pilha)

    def print_patio(self):
        cont = 0
        print("Pátio: \n")
        for pilha in self.pilhas:
            print(cont , " -> " , end="")
            print("[", end="")
            pilha.imprime()
            print("]", end="")
            print()
            cont+=1
        print("\n")

    def busca_placa(self, id):

        for i in range(len(self.pilhas)):
            if(self.pilhas[i].placas != []):
                for k in range(len(self.pilhas[i].placas)):

                    if(self.pilhas[i].placas[k] == id):

                        return i, k
            else:
                continue

        print("Placa não encontrada")

    def movimenta_placas_entre_pilhas(self, i, j):

        lst_movimento = []
        qtd_placas_tirar = self.pilhas[i].qtd_placas_acima(j)
        cont = 0
        indices_pilha = list(range(len(self.pilhas)))

        while(cont < qtd_placas_tirar):

            placa = self.pilhas[i].desempilha()
            indice_pilha = self.escolhe_indice_pilha_a_receber(indices_pilha, i)
            if(indice_pilha == -1):
                print("TODAS AS PILHAS DO PATIO ESTAO BLOQUEADA")
                return -1
            self.pilhas[indice_pilha].empilha(placa)

            lst_movimento.append((i,indice_pilha, placa))
            cont+=1
        if(lst_movimento == []):
            lst_movimento.append((i,i,self.pilhas[i].placas[j]))
        self.pilhas[i].sequenciada = True

        return lst_movimento

    def escolhe_indice_pilha_a_receber(self, indices_pilha, i):
        if(i in indices_pilha):
            indices_pilha.remove(i)
        if(indices_pilha != []):
            indice = sorteia_elem_lista(indices_pilha)
        else:
            return -1
        if(self.pilhas[indice].sequenciada == False and len(self.pilhas[indice].placas) < TAM_MAX):
            return indice
        else:
            return self.escolhe_indice_pilha_a_receber( indices_pilha, indice)

    def movimenta_placas_entre_pilhas_vel(self, indice_pilha, indice_placa,velocidade, movimento_bobina):
        lst_movimento = []
        qtd_placas_tirar = self.pilhas[indice_pilha].qtd_placas_acima(indice_placa)
        cont = 0
        while(cont < qtd_placas_tirar):
            placa = self.pilhas[indice_pilha].desempilha()
            tupla = encontra_tupla(movimento_bobina, placa)
            if(tupla != -1):
                lst_pilhas_possiveis = self.conj_pilhas( tupla[1], velocidade)
            else:
                lst_pilhas_possiveis = self.conj_pilhas( indice_pilha, velocidade)
            indice_pilha_receber = self.escolhe_indice_pilha_a_receber(lst_pilhas_possiveis[:], indice_pilha)
            if(indice_pilha_receber != -1):
                self.pilhas[indice_pilha_receber].empilha(placa)
                lst_movimento.append((indice_pilha, indice_pilha_receber, placa) )
            else:
                if(velocidade == 0):
                    lst_pilhas_possiveis = [indice_pilha]
                    indice_pilha_receber = self.retorna_posicao_possivel(lst_pilhas_possiveis)
                else:
                    indice_pilha_receber = self.retorna_posicao_possivel(lst_pilhas_possiveis)
                if(indice_pilha_receber == -1):
                    print("TODAS AS PILHAS BLOQUEADAS")
                    return -1
                else:
                    self.pilhas[indice_pilha_receber].empilha(placa)
                    lst_movimento.append((indice_pilha, indice_pilha_receber, placa) )
            cont+=1

        if(lst_movimento == []):
            lst_movimento.append((indice_pilha,indice_pilha,self.pilhas[indice_pilha].placas[indice_placa]))
        self.pilhas[indice_pilha].sequenciada = True

        return lst_movimento

    def retorna_posicao_possivel(self, lst_pilhas_possiveis):
        auxMenor = lst_pilhas_possiveis[0]
        auxMaior = lst_pilhas_possiveis[-1]
        binario = 1
        indice = lst_pilhas_possiveis[0]
        while( 0<= indice <= len(self.pilhas) - 1):
            if(self.pilhas[indice].sequenciada):
                if(binario > 0 and indice > 0):
                    auxMenor = auxMenor - 1
                    indice = auxMenor
                    binario = binario*-1
                else:
                    auxMaior = auxMaior + 1
                    indice = auxMaior
                    binario = binario*-1
            else:
                return indice
        return -1
    def conj_pilhas(self, pilha, vel):

        pilhas = len(self.pilhas) - 1
        if(pilha - vel < 0 and pilha + vel > pilhas):
            pilhas_possiveis = list(range(0, len(self.pilhas)))
        elif(pilha - vel < 0 ):
            pilhas_possiveis = list(range(0, pilha + vel + 1))
        elif(pilha + vel > pilhas):
            pilhas_possiveis = list(range(pilha - vel, len(self.pilhas)))
        else:
            pilhas_possiveis = list(range(pilha - vel, pilha+vel + 1))

        return pilhas_possiveis
