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


with open(file_name) as f:
    lines = f.readlines()
    garden = np.array([list(line.strip()) for line in lines])

    regions = {}

    marked = np.zeros(garden.shape)
    for row, col in np.ndindex(garden.shape):
        if marked[row, col]:
            # Already in region
            pass
        else:
            # find region
            region = Region()
            sign = garden[row, col]

            plot = Plot(sign, row, col)

            find_region(plot, garden)

    print(som)
