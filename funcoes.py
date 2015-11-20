__author__ = 'gabriel'
import random

TAM_MAX = 5

def sorteia_elem_lista(lst):
    qtd = len(lst)
    indice = random.randint(0,qtd - 1)
    return lst[indice]

def encontra_tupla(movimento_bobina, placa):

    for tupla in movimento_bobina:
        if(tupla[2] == placa):
            return tupla

    return -1