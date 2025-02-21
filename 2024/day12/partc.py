file_name = "C:/Users/danie/Documents/repos/2024/day12/input.txt"
from enum import Enum, unique

import numpy as np


@unique
class PlotState(Enum):
    unknown = 0
    intern = 1
    extern = 2
    none = 3


class Point:

    def __init__(self, row, col):
        self.row = row
        self.col = col


def in_boundaries(point: Point, width, height):
    return 0 <= point.row < height and 0 <= point.col < width


class Plot:

    def __init__(self, type, row, col):
        # Init info
        self.type = type
        self.row = row
        self.col = col

        # Check already next positions
        self.north_border = PlotState.unknown
        self.east_border = PlotState.unknown
        self.west_border = PlotState.unknown
        self.south_border = PlotState.unknown

        # Meta info
        self.edges = 0
        self.region_id = None

    def north(self) -> Point:
        return Point(self.row - 1, self.col)

    def south(self) -> Point:
        return Point(self.row + 1, self.col)

    def east(self) -> Point:
        return Point(self.row, self.col + 1)

    def west(self) -> Point:
        return Point(self.row, self.col - 1)


class Region:

    def __init__(self):
        self.edges = 0
        self.type = ""
        self.id = None
        self.plots = []


class Garden:
    plots: [[Plot]]

    def __init__(self, garden: np.ndarray):
        self.garden = garden
        self.height, self.width = garden.shape
        self.plots = [[None for _ in range(self.height)] for _ in range(self.width)]

    # 1. Fill plots
    def fill_plots(self):
        for row, col in np.ndindex(self.garden.shape):
            type = self.garden[row, col]
            plot = Plot(type, row, col)
            self.plots[row][col] = plot

    # 2. Check neighbours for types, find edges

    def check_neighbours(self):
        for row, col in np.ndindex(self.garden.shape):
            plot: Plot = self.plots[row][col]
            if self.hasNorth(plot):
                if plot.north_border is PlotState.unknown:
                    self.check_north(plot)
                else:
                    # Already knows
                    pass
            else:
                plot.north_border = PlotState.none
                plot.edges += 1

            if self.hasEast(plot):
                if plot.east_border is PlotState.unknown:
                    self.check_east(plot)
                else:
                    # Already knows
                    pass
            else:
                plot.east_border = PlotState.none
                plot.edges += 1

            if self.hasWest(plot):
                if plot.west_border is PlotState.unknown:
                    self.check_west(plot)
                else:
                    # Already knows
                    pass
            else:
                plot.west_border = PlotState.none
                plot.edges += 1

            if self.hasSouth(plot):
                if plot.south_border is PlotState.unknown:
                    self.check_south(plot)
                else:
                    # Already knows
                    pass
            else:
                plot.south_border = PlotState.none
                plot.edges += 1

    def check_north(self, plot: Plot):
        next_point = plot.north()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.north_border = PlotState.intern
            next_plot.south_border = PlotState.intern
        else:
            plot.north_border = PlotState.extern
            plot.edges += 1
            next_plot.south_border = PlotState.extern
            next_plot.edges += 1

    def check_south(self, plot: Plot):
        next_point = plot.south()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.south_border = PlotState.intern
            next_plot.north_border = PlotState.intern
        else:
            plot.south_border = PlotState.extern
            plot.edges += 1
            next_plot.north_border = PlotState.extern
            next_plot.edges += 1

    def check_east(self, plot: Plot):
        next_point = plot.east()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.east_border = PlotState.intern
            next_plot.west_border = PlotState.intern
        else:
            plot.east_border = PlotState.extern
            plot.edges += 1
            next_plot.west_border = PlotState.extern
            next_plot.edges += 1

    def check_west(self, plot: Plot):
        next_point = plot.west()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.west_border = PlotState.intern
            next_plot.east_border = PlotState.intern
        else:
            plot.west_border = PlotState.extern
            plot.edges += 1
            next_plot.east_border = PlotState.extern
            next_plot.edges += 1

    def check_point(self, point: Point, type):
        neighbour = self.garden[point.row, point.col]
        return neighbour == type

    # 3. Find the regions / assign region id's
    def find_regions(self):
        region_counter = 1
        for row, col in np.ndindex(self.garden.shape):
            plot: Plot = self.plots[row][col]
            if not plot.region_id:
                # no region id yet, set one
                self.follow_region(plot, region_counter)
                region_counter += 1
            else:
                pass

    def follow_region(self, plot: Plot, region_id: int):
        if not plot.region_id:
            plot.region_id = region_id
            if plot.north_border == PlotState.intern:
                next_point = plot.north()
                next_plot: Plot = self.plots[next_point.row][next_point.col]
                self.follow_region(next_plot, region_id)
            if plot.south_border == PlotState.intern:
                next_point = plot.south()
                next_plot: Plot = self.plots[next_point.row][next_point.col]
                self.follow_region(next_plot, region_id)
            if plot.east_border == PlotState.intern:
                next_point = plot.east()
                next_plot: Plot = self.plots[next_point.row][next_point.col]
                self.follow_region(next_plot, region_id)
            if plot.west_border == PlotState.intern:
                next_point = plot.west()
                next_plot: Plot = self.plots[next_point.row][next_point.col]
                self.follow_region(next_plot, region_id)

    # Default position checks
    def hasNorth(self, plot):
        return in_boundaries(plot.north(), self.width, self.height)

    def hasEast(self, plot):
        return in_boundaries(plot.east(), self.width, self.height)

    def hasWest(self, plot):
        return in_boundaries(plot.west(), self.width, self.height)

    def hasSouth(self, plot):
        return in_boundaries(plot.south(), self.width, self.height)

    # pricing
    def get_price(self):
        d = {}
        for row, col in np.ndindex(self.garden.shape):
            plot: Plot = self.plots[row][col]
            if plot.region_id in d:
                d[plot.region_id]["area"] += 1
                d[plot.region_id]["fences"] += plot.edges
            else:
                d[plot.region_id] = {"area": 1, "fences": plot.edges, "type": plot.type}
        som = 0
        for key, val in d.items():
            total = val["area"] * val["fences"]
            som += total
            print(f"{val['type']}: {total}")

        print(som)


with open(file_name) as f:
    lines = f.readlines()
    grid = np.array([list(line.strip()) for line in lines])

    garden = Garden(grid)
    garden.fill_plots()
    garden.check_neighbours()
    garden.find_regions()
    print("hellow")

    garden.get_price()
