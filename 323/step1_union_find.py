from typing import List


class UnionFind:
    def __init__(self, number_of_nodes):
        self.parents = list(range(number_of_nodes))
        self.sizes = [1] * number_of_nodes
        self.number_of_components = number_of_nodes

    def find_root(self, node_index):
        while self.parents[node_index] != node_index:
            self.parents[node_index] = self.parents[self.parents[node_index]]
            node_index = self.parents[node_index]
        return node_index

    def union(self, a, b):
        root_of_a = self.find_root(a)
        root_of_b = self.find_root(b)
        if root_of_a == root_of_b:
            return

        if self.sizes[root_of_a] > self.sizes[root_of_b]:
            parent_root = root_of_a
            child_root = root_of_b
        else:
            parent_root = root_of_b
            child_root = root_of_a

        self.parents[child_root] = parent_root
        self.sizes[parent_root] += self.sizes[child_root]
        self.number_of_components -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_connections = UnionFind(n)
        for edge in edges:
            node_connections.union(edge[0], edge[1])
        return node_connections.number_of_components
