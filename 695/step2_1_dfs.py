from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND_CELL = 1
        # WATER_CELL = 0

        height = len(grid)
        width = len(grid[0])

        max_area_of_island = 0

        def is_land_in_bound(x, y):
            if not (0 <= x < width and 0 <= y < height):
                return False
            if grid[y][x] != LAND_CELL:
                return False
            return True

        cells_to_visit = []
        visited = []
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for y in range(height):
            for x in range(width):
                if grid[y][x] != LAND_CELL:
                    continue
                if (x, y) in visited:
                    continue
                cells_to_visit.append((x, y))
                visited.append((x, y))
                current_island_area = 0
                while cells_to_visit:
                    x, y = cells_to_visit.pop()
                    if not is_land_in_bound(x, y):
                        continue
                    current_island_area += 1
                    for direction_x, direction_y in directions:
                        if (x + direction_x, y + direction_y) in visited:
                            continue
                        if is_land_in_bound(x + direction_x, y + direction_y):
                            visited.append((x + direction_x, y + direction_y))
                            cells_to_visit.append((x + direction_x, y + direction_y))
                if current_island_area > max_area_of_island:
                    max_area_of_island = current_island_area
        return max_area_of_island
