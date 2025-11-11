Dijkstra’s Algorithm — Detailed Explanation
🔹 Introduction

Dijkstra’s Algorithm is one of the most popular algorithms used to find the shortest path from a single source node to all other nodes in a weighted graph (directed or undirected).
It was developed by Edsger W. Dijkstra in 1956.

It works only when all edge weights are non-negative.

🔹 Basic Idea

The algorithm maintains a set of nodes whose minimum distance from the source is already known.
It repeatedly selects the node with the smallest tentative distance, explores its neighbors, and updates their distances if a shorter path is found.

🔹 Key Concepts

Source vertex (S): The starting point.

Distance (d): The current shortest known distance from the source to each vertex.

Visited set: Vertices for which the shortest distance is finalized.

Priority Queue (Min-Heap): Efficiently selects the vertex with the smallest distance.

🔹 Algorithm Steps

Initialization

Set the distance to the source vertex as 0: distance[source] = 0.

Set the distance to all other vertices as ∞ (infinity).

Mark all vertices as unvisited.

Visit the vertex with the smallest tentative distance

Initially, this is the source vertex.

For the current vertex, explore all its neighbors:

Calculate the new distance:
new_distance = distance[current] + weight(current, neighbor)

If new_distance < distance[neighbor], update it.

Mark the current vertex as visited

Once a vertex is visited, its shortest distance is finalized and will not change.

Repeat Steps 2–4

Continue until all vertices have been visited or the smallest distance among unvisited vertices is ∞.

Result

The distance[] array now holds the shortest distance from the source to every vertex.

🔹 Example

Consider this graph:

        (2)
     A ------ B
     |        |
   (4)|        |(1)
     |        |
     C ------ D
        (3)


Goal: Find the shortest distance from A to all vertices.

Vertex	Initial Distance	Updated Distance	Final
A	0	—	✔
B	∞ → 2	—	✔
C	∞ → 4	—	✔
D	∞ → 3 (via B)	—	✔

Shortest Distances from A:

A → A = 0

A → B = 2

A → D = 3

A → C = 4

🔹 Pseudocode
Dijkstra(G, source):
    create distance[] and set all to ∞
    distance[source] = 0
    create priority queue PQ
    PQ.push((0, source))

    while PQ not empty:
        (dist, u) = PQ.pop()   // vertex with smallest distance

        for each neighbor v of u:
            if distance[v] > distance[u] + weight(u, v):
                distance[v] = distance[u] + weight(u, v)
                PQ.push((distance[v], v))

    return distance[]

🔹 Time Complexity

Using adjacency matrix: O(V²)

Using min-priority queue (heap): O((V + E) log V)

🔹 Applications

GPS navigation systems (shortest driving route)

Network routing protocols (like OSPF)

Flight or delivery route optimization

Game AI pathfinding (in maps or terrains)

🔹 Limitations

Cannot handle negative edge weights

Not suitable for negative cycles

Works for single-source shortest path only