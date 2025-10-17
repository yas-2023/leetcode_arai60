from collections import defaultdict
from typing import Dict, List, Set


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def build_undirected_adjacency(
            num_nodes: int, edges: List[List[int]]
        ) -> Dict[int, List[int]]:
            adjacency: Dict[int, List[int]] = defaultdict(list)
            for a, b in edges:
                if 0 <= a < num_nodes and 0 <= b < num_nodes and a != b:
                    adjacency[a].append(b)
                    adjacency[b].append(a)
            return adjacency

        adjacency = build_undirected_adjacency(n, edges)
        visited: Set[int] = set()
        num_components = 0

        for node in range(n):
            if node in visited:
                continue
            # 新しいコンポーネントを発見
            num_components += 1
            frontier_node = [node]
            visited.add(node)

            while frontier_node:
                current_node = frontier_node.pop()
                for neighbor in adjacency[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        frontier_node.append(neighbor)

        return num_components
