from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        grid_size = rows * columns
        union_find = UnionFind(grid_size)

        def map_to_cell_no(row, column):
            return row * columns + column

        LAND_CELL = '1'
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == LAND_CELL:
                    union_find.add_component()

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] != LAND_CELL:
                    continue
                cell_no = map_to_cell_no(row, column)
                if row + 1 < rows and grid[row + 1][column] == LAND_CELL:
                    union_find.union(cell_no, map_to_cell_no(row + 1, column))
                if column + 1 < columns and grid[row][column + 1] == LAND_CELL:
                    union_find.union(cell_no, map_to_cell_no(row, column + 1))
        return union_find.num_of_components


class UnionFind():
    def __init__(self, grid_size):
        self.component_sizes = [1] * grid_size
        self.parents = list(range(grid_size))
        self.num_of_components = 0

    def add_component(self):
        self.num_of_components += 1

    def find_root_with_path_halving(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, a, b):
        root_of_a = self.find_root_with_path_halving(a)
        root_of_b = self.find_root_with_path_halving(b)

        if root_of_a == root_of_b:
            return

        if self.component_sizes[root_of_a] > self.component_sizes[root_of_b]:
            parent_root = root_of_a
            child_root = root_of_b
        else:
            parent_root = root_of_b
            child_root = root_of_a

        self.parents[child_root] = parent_root
        self.component_sizes[parent_root] += self.component_sizes[child_root]
        self.num_of_components -= 1
