# Exercício 7: Representação e Travessia de um Grafo

print("Exercício 7: Representação e Travessia de um Grafo")

class Grafo:
    def __init__(self):
        self.grafo = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'E'],
            'D': ['B', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }

    def mostrar_adjacencia(self):
        return self.grafo

grafo = Grafo()
print(grafo.mostrar_adjacencia())

# A lista de adjacência foi representada como um dicionário em Python, que é eficiente para armazenar e acessar os vizinhos de cada vértice.

# Exercício 8: Detecção de Fraudes Financeiras com Grafos

print("\nExercício 8: Detecção de Fraudes Financeiras com Grafos")

class GrafoTransacoes:
    def __init__(self):
        self.grafo = {
            'A': ['B', 'C'],
            'B': ['C'],
            'C': ['A']
        }
    
    def dfs(self, vertice, visitados=None, caminho=None):
        if visitados is None:
            visitados = set()
        if caminho is None:
            caminho = []
        
        visitados.add(vertice)
        caminho.append(vertice)

        for vizinho in self.grafo.get(vertice, []):
            if vizinho not in visitados:
                if self.dfs(vizinho, visitados, caminho):
                    return True
            elif vizinho in caminho:
                print(f"Ciclo detectado! Transações fraudulentas entre {caminho} e {vizinho}")
                return True
        caminho.pop()
        return False

grafo_transacoes = GrafoTransacoes()
grafo_transacoes.dfs('A')

# Exercício 9: Implementação do Algoritmo Breadth-First Search (BFS)

print("\nExercício 9: Implementação do Algoritmo Breadth-First Search (BFS)")

from collections import deque

class GrafoBFS:
    def __init__(self):
        self.grafo = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'E'],
            'D': ['B', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }

    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        ordem_visita = []

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                ordem_visita.append(vertice)
                fila.extend(self.grafo.get(vertice, []))
        
        return ordem_visita

grafo_bfs = GrafoBFS()
print(grafo_bfs.bfs('A'))

# Exercício 10: Comparação entre DFS e BFS

print("\nExercício 10: Comparação entre DFS e BFS")

class GrafoComparacao:
    def __init__(self):
        self.grafo = {
            1: [2, 3],
            2: [4],
            3: [5],
            4: [6],
            5: [6],
            6: []
        }

    def dfs(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(vertice)

        for vizinho in self.grafo.get(vertice, []):
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

        return visitados

    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        ordem_visita = []

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                ordem_visita.append(vertice)
                fila.extend(self.grafo.get(vertice, []))

        return ordem_visita

grafo_comparacao = GrafoComparacao()
print("DFS:", grafo_comparacao.dfs(1))
print("BFS:", grafo_comparacao.bfs(1))

# Exercício 11: Implementação de DFS (Busca em Profundidade)

print("\nExercício 11: Implementação de DFS (Busca em Profundidade)")

class GrafoDFS:
    def __init__(self):
        self.grafo = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'E'],
            'D': ['B', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()

        visitados.add(vertice)

        for vizinho in self.grafo.get(vertice, []):
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

        return visitados

grafo_dfs = GrafoDFS()
print(grafo_dfs.dfs_recursivo('A'))

# Exercício 12: Caminho Mais Curto em um Grafo Não Ponderado

print("\nExercício 12: Caminho Mais Curto em um Grafo Não Ponderado")

class GrafoBFS_CaminhoCurto:
    def __init__(self):
        self.grafo = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'E'],
            'D': ['B', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }

    def bfs_caminho_curto(self, inicio, fim):
        visitados = set()
        fila = deque([(inicio, [inicio])])

        while fila:
            vertice, caminho = fila.popleft()

            if vertice == fim:
                return caminho

            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in self.grafo.get(vertice, []):
                    fila.append((vizinho, caminho + [vizinho]))
        return None

grafo_bfs_caminho = GrafoBFS_CaminhoCurto()
print(grafo_bfs_caminho.bfs_caminho_curto('A', 'F'))
