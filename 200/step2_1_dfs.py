from typing import List, Tuple
from itertools import product


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFSのgrid非破壊の実装。visitedの座標をキューに入れていく仕組み
        # gridをハードコピーする実装もあるがvisitedのキューを用意したほうが空間計算量の観点から有利と考えた
        LAND_TILE = '1'
        # WATER_TILE = '0' # 宣言したが使わないのでコメントアウト
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])

        def is_in_bounds(row: int, column: int) -> bool:
            return 0 <= row < rows and 0 <= column < columns

        visited: set[Tuple[int, int]] = set()

        def explore_island(start_row: int, start_column: int) -> None:
            tiles_to_check = [(start_row, start_column)]
            visited.add((start_row, start_column))
            while tiles_to_check:
                row, column = tiles_to_check.pop()
                for direction_row, direction_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row, next_column = row + direction_row, column + direction_column
                    if (
                        is_in_bounds(next_row, next_column) and
                        grid[next_row][next_column] == LAND_TILE and
                        (next_row, next_column) not in visited
                    ):
                        visited.add((next_row, next_column))
                        tiles_to_check.append((next_row, next_column))

        islands = 0
        for row, column in product(range(rows), range(columns)):
            if grid[row][column] == LAND_TILE and (row, column) not in visited:
                islands += 1
                explore_island(row, column)
        return islands
