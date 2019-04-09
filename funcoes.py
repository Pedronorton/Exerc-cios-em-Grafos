from Grafo import *



def montarMatriz(arquivo):
    manipulador = open(arquivo,'r')
    matriz = {}

    for linha in manipulador:
        linha = linha.rstrip()
        linha = linha.rsplit()
        for v in linha[0]:
            aux = {}
            for u in range(1,len(linha)):
                if(linha[u]!='-'):
                    aux[linha[u]] = 1
            matriz[v] = aux
    return matriz


def listaVertice(arquivo):
    lista = {}
    manipulador = open(arquivo,'r')
    for linha in manipulador:
        linha = linha.rstrip()
        linha = linha.rsplit()
        v = Vertice(linha[0])
        lista[linha[0]] = v

    return lista


def DFS(matriz,lista,v0):
    Q = lista
    dom = list(lista)
    for v in Q:
        if (lista[v].cor == 'B'):
            dfsVisit(lista[v],lista,matriz,dom)
    return lista


def dfsVisit(v,lista,matriz,dom):
    v.cor = 'C'
    for u in matriz[v.id]:
        #if lista[u].cor == 'B':
            lista[u].cor = 'C'
            if (lista[u].pai != v):
                lista[u].pai = v
                lista[u].alteracaoPai+=1
            dfsVisit(lista[u],lista,matriz,dom)
    v.cor = 'P'

def dominantes(lista):
    dom = []
    for v in lista:
        if (lista[v].alteracaoPai == 1):
           if (int(lista[v].pai.id) not in dom):
               dom.append(int(lista[v].pai.id))
    return dom
