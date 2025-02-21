from typing import Dict

file_name = "C:/Users/danie/Documents/repos/2024/day12/input.txt"
import numpy as np


class Plot:

    def __init__(self, type, row, col):
        self.type = type
        self.row = row
        self.col = col
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.edges = 0
        self.region_id = None

    def check_neigbours(self):
        pass


class Region:

    def __init__(self):
        self.edges = 0
        self.type = ""
        self.id = None
        self.plots = []

    def check_north(self, plot: Plot, garden: np.array):
        try:
            neigbour = garden[plot.row - 1, plot.col]
            if neigbour == self.type:
                plot.north = True
                next_plot = Plot(neigbour, plot.row - 1, plot.col)
                # We are coming from south, dont need to check
                next_plot.south = True
                return next_plot
            else:
                plot.north = False
                plot.edges += 1
        except:
            pass

    def find_region(self, plot: Plot, garden):
        # check all other neigbours
        if not plot.north:
            self.check_north(plot, garden)


def check_plot(row, col, garden):
    pass


class Point:

    def __init__(self, row, col):
        self.row = row
        self.col = col


with open(file_name) as f:
    lines = f.readlines()
    garden = np.array([list(line.strip()) for line in lines])

    regions = {}
    height, width = garden.shape

    plots = np.zeros(garden.shape)
    region = 0
    regions: Dict[str, int] = {}
    for row, col in np.ndindex(garden.shape):
        type = garden[row, col]
        north = Point(row - 1, col)
        # east = Point(row, col + 1)
        # south = Point(row + 1, col)
        west = Point(row, col - 1)
        edges = 0

        next_plot = Plot(type, row, col)

        # TODO: check alleen boven en rechts?
        for point in [north, west]:
            if 0 <= point.row <= height and 0 <= point.col <= width:
                plot = plots[point.row, point.col]
                if plot !=0 :
                    if plot.type == type:
                        pass
                    else:
                        edges +=1
                        regions[type] += 1
                else:
                    sign = garden[point.row, point.col]
                    if sign == type:
                        if:
                            pass
                    else:
                        edges += 1
                        region_id = region
            else:
                pass

        plot = Plot(type, row, col)
        plot.edges = edges
        plot.region = region_id
