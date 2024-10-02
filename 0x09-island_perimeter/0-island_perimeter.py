#!/usr/bin/python3

"""
Island Perimeter Calculator

This script calculates the perimeter of a 2D island
"""


def calculate_island_perimeter(land_grid):
    """
    Determines the perimeter of the island in the given grid.
    Args:
        land_grid: A 2D list of integers (0 or 1)
    Returns:
        The perimeter of the island.
    """

    perimeter = 0
    rows, cols = len(land_grid), len(land_grid[0])

    for row in range(rows):
        for col in range(cols):
            if land_grid[row][col] == 1:
                perimeter += 4
                if row > 0 and land_grid[row - 1][col] == 1:
                    perimeter -= 2
                if row < rows - 1 and land_grid[row + 1][col] == 1:
                    perimeter -= 2
                if col > 0 and land_grid[row][col - 1] == 1:
                    perimeter -= 2
                if col < cols - 1 and land_grid[row][col + 1] == 1:
                    perimeter -= 2

    return perimeter
