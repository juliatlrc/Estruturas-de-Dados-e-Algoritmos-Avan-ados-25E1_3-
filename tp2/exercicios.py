# Exercício 1: Representação de Relacionamentos
print("Exercício 1: Representação de Relacionamentos")

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([("Alice", "Bob"), ("Alice", "Carlos"), ("Bob", "Diana"), ("Carlos", "Diana"), ("Carlos", "Eduardo")])

nx.draw(G, with_labels=True, font_weight='bold', node_size=2000, node_color='skyblue')
plt.show()

vertices = list(G.nodes())
arestas = list(G.edges())

print("Vértices:", vertices)
print("Arestas:", arestas)
print("O grafo é não direcionado. Justificativa: As conexões entre os usuários indicam uma relação bidirecional (amizade).")

# Exercício 2: Conceitos Fundamentais
print("\nExercício 2: Conceitos Fundamentais")

class Grafo:
    def __init__(self, bairros):
        self.bairros = bairros
        self.grafo = {bairro: [] for bairro in bairros}

    def adicionar_aresta(self, bairro1, bairro2):
        self.grafo[bairro1].append(bairro2)
        self.grafo[bairro2].append(bairro1)

    def exibir_bairros_vizinhos(self, bairro):
        return self.grafo[bairro]

bairros = ["Centro", "Bairro A", "Bairro B", "Bairro C", "Bairro D", "Bairro E"]
grafo = Grafo(bairros)
grafo.adicionar_aresta("Centro", "Bairro A")
grafo.adicionar_aresta("Centro", "Bairro B")
grafo.adicionar_aresta("Bairro A", "Bairro C")
grafo.adicionar_aresta("Bairro B", "Bairro C")
grafo.adicionar_aresta("Bairro C", "Bairro D")
grafo.adicionar_aresta("Bairro D", "Bairro E")

print("Vizinhos do Centro:", grafo.exibir_bairros_vizinhos("Centro"))
print("Vizinhos do Bairro A:", grafo.exibir_bairros_vizinhos("Bairro A"))

# Exercício 3: Construção de Matriz de Adjacência
print("\nExercício 3: Construção de Matriz de Adjacência")

import numpy as np

cidades = ["A", "B", "C", "D"]
matriz_adj = np.zeros((4, 4), dtype=int)

matriz_adj[0][1] = 1
matriz_adj[0][2] = 1
matriz_adj[1][0] = 1
matriz_adj[1][3] = 1
matriz_adj[2][0] = 1
matriz_adj[2][3] = 1
matriz_adj[3][1] = 1
matriz_adj[3][2] = 1

print("Matriz de Adjacência:", matriz_adj)

matriz_adj_direcionada = np.zeros((4, 4), dtype=int)
matriz_adj_direcionada[0][1] = 1
matriz_adj_direcionada[0][2] = 1
matriz_adj_direcionada[1][3] = 1
matriz_adj_direcionada[2][3] = 1

print("Matriz de Adjacência para grafo direcionado:", matriz_adj_direcionada)

# Exercício 4: Construção de Lista de Adjacência
print("\nExercício 4: Construção de Lista de Adjacência")

class ListaAdjacencia:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, bairro1, bairro2):
        if bairro1 not in self.grafo:
            self.grafo[bairro1] = []
        if bairro2 not in self.grafo:
            self.grafo[bairro2] = []
        self.grafo[bairro1].append(bairro2)
        self.grafo[bairro2].append(bairro1)

    def vizinhos(self, bairro):
        return self.grafo.get(bairro, [])

grafo_logistica = ListaAdjacencia()
grafo_logistica.adicionar_aresta("Centro", "Bairro A")
grafo_logistica.adicionar_aresta("Centro", "Bairro B")
grafo_logistica.adicionar_aresta("Bairro A", "Bairro C")
grafo_logistica.adicionar_aresta("Bairro B", "Bairro C")
grafo_logistica.adicionar_aresta("Bairro C", "Bairro D")

print("Vizinhos do Centro:", grafo_logistica.vizinhos("Centro"))
print("Vizinhos do Bairro A:", grafo_logistica.vizinhos("Bairro A"))

# Exercício 5: Implementação em Python
print("\nExercício 5: Implementação em Python")

class GrafoComPesos:
    def __init__(self, centros):
        self.centros = centros
        self.grafo = {centro: [] for centro in centros}

    def adicionar_aresta(self, centro1, centro2, peso):
        self.grafo[centro1].append((centro2, peso))
        self.grafo[centro2].append((centro1, peso))

    def vizinhos(self, centro):
        return self.grafo[centro]

    def bfs(self, inicio, fim):
        fila = [inicio]
        visitados = {inicio: None}
        while fila:
            atual = fila.pop(0)
            if atual == fim:
                caminho = []
                while atual is not None:
                    caminho.insert(0, atual)
                    atual = visitados[atual]
                return caminho
            for vizinho, _ in self.grafo[atual]:
                if vizinho not in visitados:
                    visitados[vizinho] = atual
                    fila.append(vizinho)
        return None

centros = ["A", "B", "C", "D", "E"]
grafo = GrafoComPesos(centros)
grafo.adicionar_aresta("A", "B", 10)
grafo.adicionar_aresta("A", "C", 5)
grafo.adicionar_aresta("B", "D", 15)
grafo.adicionar_aresta("C", "E", 20)
grafo.adicionar_aresta("D", "E", 10)

print("Vizinhos de A:", grafo.vizinhos("A"))
print("Rota mais curta de A para E:", grafo.bfs("A", "E"))

# Exercício 6: Comparação entre Matriz e Lista de Adjacência
print("\nExercício 6: Comparação entre Matriz e Lista de Adjacência")

n = 1000
m = 10
matriz_adj = np.zeros((n, n), dtype=int)
lista_adj = {i: [] for i in range(n)}

# Lista de adjacência
for i in range(m):
    lista_adj[i].append(i + 1)
    lista_adj[i + 1].append(i)

print("Estrutura de Lista de Adjacência para 1000 vértices e 10 arestas:")
print(lista_adj)

# Matrizes de adjacência
print("Estrutura de Matriz de Adjacência para 1000 vértices e 10 arestas:")
print(matriz_adj)

