from typing import List, Tuple
from collections import deque
from itertools import product


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # gridを破壊的に変更するので注意！！
        LAND_CELL = '1'
        WATER_CELL = '0'
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def is_in_bounds(row: int, column: int) -> bool:
            return 0 <= row < rows and 0 <= column < cols

        def sink_island_with_bfs(start_row: int, start_column: int) -> None:
            cells_to_visit: deque[Tuple[int, int]] = deque([(start_row, start_column)])
            grid[start_row][start_column] = WATER_CELL
            while cells_to_visit:
                row, column = cells_to_visit.popleft()
                for direction_row, direction_column in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row, next_column = row + direction_row, column + direction_column
                    if is_in_bounds(next_row, next_column) and grid[next_row][next_column] == LAND_CELL:
                        grid[next_row][next_column] = WATER_CELL
                        cells_to_visit.append((next_row, next_column))

        islands = 0
        for row, column in product(range(rows), range(cols)):
            if grid[row][column] == LAND_CELL:
                islands += 1
                sink_island_with_bfs(row, column)
        return islands
