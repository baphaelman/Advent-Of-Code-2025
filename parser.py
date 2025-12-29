# module for parsing input data for Advent of Code 2025
from Point import Point
from Grid import Grid

def parse_lines(filepath, raw=False):
    """Reads the input file and returns a list of stripped lines."""
    with open(filepath, 'r') as file:
        if raw:
            lines = [line.strip('\n') for line in file.readlines()]
        else:
            lines = [line.strip() for line in file.readlines()]
    return lines

def parse_comma_line(filepath):
    """Reads a single line from the input file and returns a list of values split by commas."""
    with open(filepath, 'r') as file:
        line = file.readline().strip()
    return line.split(',')

def parse_grid(filepath):
    """Reads the input file and returns a grid of characters."""
    
    with open(filepath, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        size = [len(lines[0]), len(lines)]
        grid = Grid(size)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                grid.set(Point(x, y), char)
    return grid