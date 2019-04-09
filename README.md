
1. Dado um grafo direcionado G = (V, E), dizemos que um vértice x domina um vértice y
se todo caminho partindo do vértice 0 (primeiro vértice do grafo) para y
deve passar obrigatoriamete por x. Se y não é alcançável a partir do vértice 0, então y não tem vértice dominante.
Todo vértice alcançável a partir do vértice inicial domina a si próprio. 
Como exemplo, suponha o grafo representado pela lista de adjacência abaixo:

0: 1, 2
1: 3
2: 3
3: 4
4: -
Note que o vértice 3 domina o vértice 4, uma vez que todos os caminhos de 0 ao vértice
4 devem passar pelo vértice 3. O vértice 1 não domina o vértice 3, uma vez que existe
o caminho 0-2-3 que não passa por 1. Sua tarefa consiste em determinar os vértices
dominantes de todos os vértices de um grafo G.
