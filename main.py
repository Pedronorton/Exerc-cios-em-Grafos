from funcoes import *

def main():
    arquivo = "in.txt"
    matriz = montarMatriz(arquivo)
    lista = listaVertice(arquivo)
    print('Vertices Dominantes: ')
    dfsList = DFS(matriz, lista, 0)
    print(dominantes(dfsList))




main()
