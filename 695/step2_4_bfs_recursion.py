from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND_CELL = 1
        # WATER_CELL = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        height = len(grid)
        width = len(grid[0])

        visited = []
        max_island_area = 0

        def is_land_in_bounds(x, y):
            if not (0 <= x < width):
                return False
            if not (0 <= y < height):
                return False
            if grid[y][x] != LAND_CELL:
                return False
            return True

        def measure_island_area(x, y):
            frontier_cells = deque([(x, y)])
            island_area = 0
            while frontier_cells:
                x, y = frontier_cells.popleft()
                if (x, y) in visited:
                    continue
                visited.append((x, y))
                if not is_land_in_bounds(x, y):
                    continue
                island_area += 1
                for dx, dy in directions:
                    if (x + dx, y + dy) in visited:
                        continue
                    if not is_land_in_bounds(x + dx, y + dy):
                        continue
                    frontier_cells.append((x + dx, y + dy))
            return island_area

        for y in range(height):
            for x in range(width):
                if not is_land_in_bounds(x, y):
                    continue
                if (x, y) in visited:
                    continue
                current_island_area = measure_island_area(x, y)
                max_island_area = max(max_island_area, current_island_area)
        return max_island_area
