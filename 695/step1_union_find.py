from typing import List


class UnionFind():
    def __init__(self, grid_size):
        # self.num_of_components = 0
        self.max_area_of_island = 0
        self.parents = list(range(grid_size))
        self.component_sizes = [1] * grid_size

    def find_parent(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, a, b):
        root_of_a = self.find_parent(a)
        root_of_b = self.find_parent(b)
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
        if self.component_sizes[parent_root] > self.max_area_of_island:
            self.max_area_of_island = self.component_sizes[parent_root]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND_CELL = 1
        num_of_rows = len(grid)
        num_of_columns = len(grid[0])
        grid_size = num_of_rows * num_of_columns
        island_groups = UnionFind(grid_size)

        def map_to_cell_index(row, column):
            return row * num_of_columns + column

        def is_land_cell_in_bound(row, column):
            return 0 <= row < num_of_rows and 0 <= column < num_of_columns and grid[row][column] == LAND_CELL

        for row in range(num_of_rows):
            for column in range(num_of_columns):
                if grid[row][column] != LAND_CELL:
                    continue
                if island_groups.max_area_of_island == 0:
                    island_groups.max_area_of_island = 1

                cell_index = map_to_cell_index(row, column)
                if is_land_cell_in_bound(row + 1, column):
                    island_groups.union(cell_index, map_to_cell_index(row + 1, column))
                if is_land_cell_in_bound(row, column + 1):
                    island_groups.union(cell_index, map_to_cell_index(row, column + 1))
        return island_groups.max_area_of_island
