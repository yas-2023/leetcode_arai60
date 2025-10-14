from typing import List


class UnionFind:
    def __init__(self, grid_size: int) -> None:
        self.parents = list(range(grid_size))
        self.component_sizes = [1] * grid_size
        self.num_of_components = 0  # LAND_CELL のみカウントに使う

    def add_component(self) -> None:
        self.num_of_components += 1

    def find_root_with_path_halving(self, x: int) -> int:
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]  # (path halving)
            x = self.parents[x]
        return x

    def union(self, a: int, b: int) -> None:
        root_of_a = self.find_root_with_path_halving(a)
        root_of_b = self.find_root_with_path_halving(b)

        if root_of_a == root_of_b:
            return  # すでに同じ集合に属している

        # サイズが大きい方を親にする
        # sortを使うと１行で示せるが、今回のケースでは可読性の点で良くなさそう
        # parent_root, child_root = sorted([root_of_a, root_of_b], key=lambda r: self.component_sizes[r], reverse=True)
        if self.component_sizes[root_of_a] >= self.component_sizes[root_of_b]:
            parent_root = root_of_a
            child_root = root_of_b
        else:
            parent_root = root_of_b
            child_root = root_of_a

        self.parents[child_root] = parent_root
        self.component_sizes[parent_root] += self.component_sizes[child_root]
        self.num_of_components -= 1  # 結合によりコンポーネントが1つ減る


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND_CELL = '1'
        # WATER_CELL = '0' このケースでは使わないのでコメントアウト
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])

        def map_to_cell_no(row: int, column: int) -> int:
            # 2d -> 1d
            return row * columns + column

        grid_size = rows * columns
        union_find = UnionFind(grid_size)

        # まず LAND_CELL の数をコンポーネントとして数える
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == LAND_CELL:
                    union_find.add_component()

        # 右・下だけ見れば十分（重複unionを避ける）
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
