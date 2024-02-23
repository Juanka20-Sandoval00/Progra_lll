import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Crear el gráfico
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Calcular las distancias más cortas desde el nodo 'A'
start_node = 'A'
distances = dijkstra(graph, start_node)

# Crear un gráfico dirigido
G = nx.DiGraph()

# Añadir nodos y arcos al gráfico
for node in graph:
    G.add_node(node)
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

# Dibujar el gráfico
pos = nx.spring_layout(G)  # Posiciones para todos los nodos
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')

# Añadir etiquetas de distancia
labels = {node: f"{node}\nDistancia: {distances[node]}" for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels)

# Añadir etiquetas de peso en los arcos
edge_labels = {(node, neighbor): weight['weight'] for node, neighbor, weight in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Algoritmo de Dijkstra y Distancias más Cortas")
plt.show()