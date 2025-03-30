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

class GrafoComEstacoesRecarga(Grafo):
    def __init__(self, autonomia_maxima):
        super().__init__()
        self.autonomia_maxima = autonomia_maxima

    def dijkstra_com_recarga(self, origem):
        dist = {vertice: float('inf') for vertice in self.grafo}
        dist[origem] = 0
        pq = [(0, origem, 0)]  # Distância, vértice, distância percorrida
        while pq:
            dist_atual, vertice, distancia_percorrida = heapq.heappop(pq)
            if dist_atual > dist[vertice]:
                continue
            for vizinho, peso in self.grafo[vertice]:
                if distancia_percorrida + peso > self.autonomia_maxima:
                    continue
                nova_distancia = dist_atual + peso
                if nova_distancia < dist[vizinho]:
                    dist[vizinho] = nova_distancia
                    heapq.heappush(pq, (nova_distancia, vizinho, distancia_percorrida + peso))
        return dist

class GrafoComEscalasObrigatorias(Grafo):
    def __init__(self, tempo_maximo_conexao):
        super().__init__()
        self.tempo_maximo_conexao = tempo_maximo_conexao

    def dijkstra_com_escala(self, origem):
        dist = {vertice: float('inf') for vertice in self.grafo}
        dist[origem] = 0
        pq = [(0, origem)]
        while pq:
            dist_atual, vertice = heapq.heappop(pq)
            if dist_atual > dist[vertice]:
                continue
            for vizinho, peso in self.grafo[vertice]:
                if peso > self.tempo_maximo_conexao:
                    continue
                nova_distancia = dist_atual + peso
                if nova_distancia < dist[vizinho]:
                    dist[vizinho] = nova_distancia
                    heapq.heappush(pq, (nova_distancia, vizinho))
        return dist

class GrafoDeAeroportos(GrafoComEscalasObrigatorias):
    def __init__(self, tempo_maximo_conexao, escalas_obrigatorias):
        super().__init__(tempo_maximo_conexao)
        self.escalas_obrigatorias = escalas_obrigatorias

    def dijkstra_com_custo(self, origem):
        dist = {vertice: float('inf') for vertice in self.grafo}
        dist[origem] = 0
        pq = [(0, origem)]
        while pq:
            dist_atual, vertice = heapq.heappop(pq)
            if dist_atual > dist[vertice]:
                continue
            for vizinho, (peso, escala) in self.grafo[vertice]:
                custo_adicional = 0
                if escala:
                    custo_adicional = 50  # Custo adicional de escala
                nova_distancia = dist_atual + peso + custo_adicional
                if nova_distancia < dist[vizinho]:
                    dist[vizinho] = nova_distancia
                    heapq.heappush(pq, (nova_distancia, vizinho))
        return dist

# Exercício 1: Logística de Entregas
print("Exercício 1: Logística de Entregas - Algoritmo de Dijkstra - Menor Caminho")
g = Grafo()
g.adicionar_aresta('Centro', 'Bairro1', 5)
g.adicionar_aresta('Centro', 'Bairro2', 10)
g.adicionar_aresta('Bairro1', 'Bairro2', 2)
g.adicionar_aresta('Bairro1', 'Bairro3', 7)
g.adicionar_aresta('Bairro2', 'Bairro3', 1)

distancias = g.dijkstra('Centro')
print(distancias)
print()

# Exercício 2: Roteamento de Ônibus
print("Exercício 2: Roteamento de Ônibus - Algoritmo de Dijkstra - Menor Caminho")
# O código é o mesmo do Exercício 1, pois só muda o contexto
distancias = g.dijkstra('Centro')
print(distancias)
print()

# Exercício 3: Rede de Transportes Aéreos
print("Exercício 3: Rede de Transportes Aéreos - Algoritmo de Dijkstra - Menor Caminho")
g_voos = GrafoDeAeroportos(2, {'A': ['B', 'C'], 'B': ['C', 'D']})
g_voos.adicionar_aresta('A', 'B', (5, True))
g_voos.adicionar_aresta('B', 'C', (2, False))
g_voos.adicionar_aresta('C', 'D', (6, True))

distancias_voos = g_voos.dijkstra_com_custo('A')
print(distancias_voos)
print()

# Exercício 4: Transporte de Mercadorias
print("Exercício 4: Transporte de Mercadorias - Algoritmo de Dijkstra - Menor Caminho")
# O código para esse exercício seria similar ao primeiro, com peso como custo de pedágio e combustível
distancias = g.dijkstra('Centro')
print(distancias)
print()

# Exercício 5: Otimização de Rotas em uma Cidade Inteligente
print("Exercício 5: Otimização de Rotas em uma Cidade Inteligente - Algoritmo de Dijkstra - Menor Caminho")
g_estacao = GrafoComEstacoesRecarga(10)
g_estacao.adicionar_aresta('A', 'B', 5)
g_estacao.adicionar_aresta('B', 'C', 3)
g_estacao.adicionar_aresta('C', 'D', 8)
g_estacao.adicionar_aresta('D', 'E', 4)

distancias_recarga = g_estacao.dijkstra_com_recarga('A')
print(distancias_recarga)
print()

# Exercício 6: Transporte Aéreo Internacional
print("Exercício 6: Transporte Aéreo Internacional - Algoritmo de Dijkstra - Menor Caminho")
g_voos = GrafoDeAeroportos(2, {'A': ['B', 'C'], 'B': ['C', 'D']})
g_voos.adicionar_aresta('A', 'B', (5, True))
g_voos.adicionar_aresta('B', 'C', (2, False))
g_voos.adicionar_aresta('C', 'D', (6, True))

distancias_voos = g_voos.dijkstra_com_custo('A')
print(distancias_voos)
print()
