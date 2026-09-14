from heapq import heappop, heappush
from dataclasses import dataclass


@dataclass
class Node:
    val: int 
    neighbors: list["Edge"]

@dataclass
class Edge:
    weight: int
    to_index: int

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        nodes = []
        for i in range(n):
            nodes.append(Node(i, []))

        for edge in edges:
            nodes[edge[0]].neighbors.append(Edge(edge[2], edge[1]))

        shortest = {}
        frontier: list[tuple[int, int]] = [(0, src)]

        while frontier:
            curr_cost, curr_node_idx = heappop(frontier)

            if curr_node_idx in shortest:
                continue

            shortest[curr_node_idx] = curr_cost
            for neighbor in nodes[curr_node_idx].neighbors:
                heappush(frontier, (curr_cost + neighbor.weight, neighbor.to_index))

        return {n: shortest.get(n, -1) for n in range(n)}