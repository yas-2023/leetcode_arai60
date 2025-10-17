class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # gridを破壊的に変更するので注意！！
        def land_to_water(row, column, rows, columns):
            stacked_tiles = [(row, column)]
            while stacked_tiles:
                current_row, current_column = stacked_tiles.pop()
                print(current_row, current_column)
                if current_row + 1 < rows and grid[current_row + 1][current_column] == "1":
                    grid[current_row + 1][current_column] = "0"
                    stacked_tiles.append((current_row + 1, current_column))
                if current_row - 1 >= 0 and grid[current_row - 1][current_column] == "1":
                    grid[current_row - 1][current_column] = "0"
                    stacked_tiles.append((current_row - 1, current_column))
                if current_column + 1 < columns and grid[current_row][current_column + 1] == "1":
                    grid[current_row][current_column + 1] = "0"
                    stacked_tiles.append((current_row, current_column + 1))
                if current_column - 1 >= 0 and grid[current_row][current_column - 1] == "1":
                    grid[current_row][current_column - 1] = "0"
                    stacked_tiles.append((current_row, current_column - 1))

        islands = 0
        rows, columns = len(grid), len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    land_to_water(row, column, rows, columns)
        return islands
