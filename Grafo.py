class Vertice:
    def __init__(self,id):
        self.tA = float('inf')
        self.tF = float('inf')
        self.pai = None
        self.alteracaoPai = 0
        self.cor = 'B'
        self.id = id
