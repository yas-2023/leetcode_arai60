from collections import defaultdict, deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def build_adjacency(n, edges):
            adjacency = defaultdict(list)
            for a, b in edges:
                adjacency[a].append(b)
                adjacency[b].append(a)
            return adjacency

        adjacency = build_adjacency(n, edges)
        visited = set()
        num_components = 0
        for start_node in range(n):
            if start_node in visited:
                continue
            num_components += 1
            visited.add(start_node)
            frontier_nodes = deque([start_node])
            while frontier_nodes:
                node = frontier_nodes.popleft()
                for neighbor_node in adjacency[node]:
                    if neighbor_node not in visited:
                        visited.add(neighbor_node)
                        frontier_nodes.append(neighbor_node)
        return num_components
