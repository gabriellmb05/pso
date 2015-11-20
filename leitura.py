__author__ = 'Michelle e Gabriel'

from Patio import *
from Pilha import *
from Bobina import *
TAM_PILHA=5

def monta_patio():
    lista=[]
    arq = open('test.txt', 'rt')
    linha = arq.readline()
    posicao=1
    patio=Patio()
    while linha != "":
        lista.append(linha[0])
        linha = arq.readline()
    i=0
    while i < len(lista):
        pilha=Pilha()
        for j in range(TAM_PILHA):

            if lista[i]=="1":
                pilha.add_placa(posicao)
            posicao+=1
            i+=1
        patio.add_pilha(pilha)
    return patio

def monta_saida():
    arq = open('saida.txt', 'rt')
    linha = arq.readline()
    posicao=1
    bobinas=[]
    while linha != "":
        aux=[]
        lst=linha.split()
        for i in range(len(lst)):
            if lst[i]!="-1":
              aux.append(int(lst[i]))
        bobina = Bobina(posicao, aux)
        bobinas.append(bobina)
        linha = arq.readline()
        posicao+=1
    return bobinas





