from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

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
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for y in range(height):
            for x in range(width):
                if grid[y][x] != LAND_CELL:
                    continue
                if (x, y) in visited:
                    continue
                cells_to_visit.append((x, y))
                visited.add((x, y))
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
                            visited.add((x + direction_x, y + direction_y))
                            cells_to_visit.append((x + direction_x, y + direction_y))
                if current_island_area > max_area_of_island:
                    max_area_of_island = current_island_area
        return max_area_of_island


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        #  LeetCode公式例（最大面積6）
        (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
            ],
            6
        ),
        # 全部水 → 0
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            0
        ),
        # 全部陸 → 9
        (
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            9
        ),
        # 複数の島 → 最大面積5
        (
            [
                [1, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 1, 1],
                [0, 1, 1, 0]
            ],
            5
        ),
        # 島が1セルだけ
        (
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            1
        ),
        # 島が1セル
        (
            [[1]],
            1
        ),
        # 空リスト
        (
            [],
            0
        )
    ]

    for i, (grid, expected) in enumerate(test_cases, start=1):
        result = solution.maxAreaOfIsland([row[:] for row in grid])
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed")
