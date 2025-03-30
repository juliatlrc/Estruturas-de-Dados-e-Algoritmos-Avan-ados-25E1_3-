import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))

    def dijkstra(self, origem):
        dist = {vertice: float('inf') for vertice in self.grafo}
        dist[origem] = 0
        pq = [(0, origem)]
        while pq:
            (dist_atual, vertice) = heapq.heappop(pq)
            if dist_atual > dist[vertice]:
                continue
            for vizinho, peso in self.grafo[vertice]:
                distancia = dist_atual + peso
                if distancia < dist[vizinho]:
                    dist[vizinho] = distancia
                    heapq.heappush(pq, (distancia, vizinho))
        return dist

    def floyd_warshall(self):
        dist = {v: {u: float('inf') for u in self.grafo} for v in self.grafo}
        for v in self.grafo:
            dist[v][v] = 0
        for v in self.grafo:
            for u, peso in self.grafo[v]:
                dist[v][u] = peso
        for k in self.grafo:
            for i in self.grafo:
                for j in self.grafo:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

class GrafoComPrim(Grafo):
    def prim(self, origem):
        mst = []
        pq = [(0, origem)]
        dist = {vertice: float('inf') for vertice in self.grafo}
        dist[origem] = 0
        visitados = set()
        
        while pq:
            peso, vertice = heapq.heappop(pq)
            if vertice not in visitados:
                visitados.add(vertice)
                if peso > 0:
                    mst.append((prev_vertice, vertice, peso))
                for vizinho, peso_aresta in self.grafo[vertice]:
                    if vizinho not in visitados and peso_aresta < dist[vizinho]:
                        dist[vizinho] = peso_aresta
                        prev_vertice = vertice
                        heapq.heappush(pq, (peso_aresta, vizinho))
        return mst

# Exercício 7: Planejamento de Redes de Internet - Árvore Geradora Mínima - Algoritmo de Prim
print("Exercício 7: Planejamento de Redes de Internet - Árvore Geradora Mínima - Algoritmo de Prim")
g_internet = GrafoComPrim()
g_internet.adicionar_aresta('Bairro1', 'Bairro2', 5)
g_internet.adicionar_aresta('Bairro2', 'Bairro3', 10)
g_internet.adicionar_aresta('Bairro3', 'Bairro4', 3)
g_internet.adicionar_aresta('Bairro4', 'Bairro5', 7)
g_internet.adicionar_aresta('Bairro1', 'Bairro3', 8)
g_internet.adicionar_aresta('Bairro2', 'Bairro5', 9)

mst_internet = g_internet.prim('Bairro1')
print(mst_internet)
print()

# Exercício 8: Sistema de Navegação GPS - Floyd-Warshall - Caminho Mínimo entre Todos os Pares
print("Exercício 8: Sistema de Navegação GPS - Floyd-Warshall - Caminho Mínimo entre Todos os Pares")
g_gps = Grafo()
g_gps.adicionar_aresta('Bairro1', 'Bairro2', 5)
g_gps.adicionar_aresta('Bairro2', 'Bairro3', 10)
g_gps.adicionar_aresta('Bairro3', 'Bairro4', 3)
g_gps.adicionar_aresta('Bairro4', 'Bairro5', 7)
g_gps.adicionar_aresta('Bairro1', 'Bairro3', 8)
g_gps.adicionar_aresta('Bairro2', 'Bairro5', 9)

distancias_gps = g_gps.floyd_warshall()
print(distancias_gps)
print()

# Exercício 9: Distribuição de Energia Elétrica - Árvore Geradora Mínima - Algoritmo de Prim
print("Exercício 9: Distribuição de Energia Elétrica - Árvore Geradora Mínima - Algoritmo de Prim")
g_energia = GrafoComPrim()
g_energia.adicionar_aresta('Cidade1', 'Cidade2', 6)
g_energia.adicionar_aresta('Cidade2', 'Cidade3', 4)
g_energia.adicionar_aresta('Cidade3', 'Cidade4', 9)
g_energia.adicionar_aresta('Cidade4', 'Cidade5', 2)
g_energia.adicionar_aresta('Cidade1', 'Cidade4', 7)
g_energia.adicionar_aresta('Cidade2', 'Cidade5', 3)

mst_energia = g_energia.prim('Cidade1')
print(mst_energia)
print()

# Exercício 10: Economia de Recursos Hídricos - Árvore Geradora Mínima - Algoritmo de Prim
print("Exercício 10: Economia de Recursos Hídricos - Árvore Geradora Mínima - Algoritmo de Prim")
g_agua = GrafoComPrim()
g_agua.adicionar_aresta('BairroA', 'BairroB', 4)
g_agua.adicionar_aresta('BairroB', 'BairroC', 6)
g_agua.adicionar_aresta('BairroC', 'BairroD', 7)
g_agua.adicionar_aresta('BairroD', 'BairroE', 3)
g_agua.adicionar_aresta('BairroA', 'BairroD', 5)
g_agua.adicionar_aresta('BairroB', 'BairroE', 2)

mst_agua = g_agua.prim('BairroA')
print(mst_agua)
print()

# Exercício 11: Rede de Telefonia - Árvore Geradora Mínima - Algoritmo de Prim
print("Exercício 11: Rede de Telefonia - Árvore Geradora Mínima - Algoritmo de Prim")
g_telefone = GrafoComPrim()
g_telefone.adicionar_aresta('Regiao1', 'Regiao2', 4)
g_telefone.adicionar_aresta('Regiao2', 'Regiao3', 3)
g_telefone.adicionar_aresta('Regiao3', 'Regiao4', 5)
g_telefone.adicionar_aresta('Regiao4', 'Regiao5', 6)
g_telefone.adicionar_aresta('Regiao1', 'Regiao3', 8)
g_telefone.adicionar_aresta('Regiao2', 'Regiao5', 7)

mst_telefone = g_telefone.prim('Regiao1')
print(mst_telefone)
print()

# Exercício 12: Eficiência de Algoritmos - Cálculo de Eficiência de Algoritmos em Grafos
print("Exercício 12: Eficiência de Algoritmos - Cálculo de Eficiência de Algoritmos em Grafos")
import time

# Gerando grafos para o teste de eficiência
g_eficiencia_dijkstra = Grafo()
g_eficiencia_floyd = Grafo()

g_eficiencia_dijkstra.adicionar_aresta('A', 'B', 1)
g_eficiencia_dijkstra.adicionar_aresta('B', 'C', 1)
g_eficiencia_dijkstra.adicionar_aresta('A', 'C', 2)

g_eficiencia_floyd.adicionar_aresta('A', 'B', 1)
g_eficiencia_floyd.adicionar_aresta('B', 'C', 1)
g_eficiencia_floyd.adicionar_aresta('A', 'C', 2)

# Teste para Dijkstra
start = time.time()
g_eficiencia_dijkstra.dijkstra('A')
end = time.time()
print(f"Dijkstra (Tempo): {end - start} segundos")

# Teste para Floyd-Warshall
start = time.time()
g_eficiencia_floyd.floyd_warshall()
end = time.time()
print(f"Floyd-Warshall (Tempo): {end - start} segundos")
print()

