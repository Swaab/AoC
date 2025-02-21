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


class Direction(Enum):
    north = 0
    east = 1
    south = 2
    west = 3


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
        self.corners = 0

    def north(self) -> Point:
        return Point(self.row - 1, self.col)

    def south(self) -> Point:
        return Point(self.row + 1, self.col)

    def east(self) -> Point:
        return Point(self.row, self.col + 1)

    def west(self) -> Point:
        return Point(self.row, self.col - 1)

    def get_start(self):
        if not self.north_border is PlotState.intern:
            return Direction.east
        if not self.east_border is PlotState.intern:
            return Direction.south
        if not self.south_border is PlotState.intern:
            return Direction.west
        if not self.west_border is PlotState.intern:
            return Direction.north

        return None

    def count_corners(self):
        count = 0
        x = 0
        y = 0
        if not self.north_border is PlotState.intern:
            count += 1
            x += 1
        if not self.east_border is PlotState.intern:
            count += 1
            y += 1
        if not self.south_border is PlotState.intern:
            count += 1
            x += 1
        if not self.west_border is PlotState.intern:
            count += 1
            y += 1

        # x and y for parallel borders
        if count <= 1:
            # Might still be outer counters that are set
            self.corners += 0
        elif count == 2:
            if y == 2 or x == 2:
                self.corners += 0
            else:
                self.corners += 1
        elif count == 3:
            self.corners += 2
        else:
            self.corners = 4

    def __str__(self):
        return f"{self.type}: {self.corners}; pos:[{self.row}.{self.col}]"


class Region:

    def __init__(self):
        self.edges = 0
        self.type = ""
        self.id = None
        self.area = 0


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

            if self.hasEast(plot):
                if plot.east_border is PlotState.unknown:
                    self.check_east(plot)
                else:
                    # Already knows
                    pass
            else:
                plot.east_border = PlotState.none

            if self.hasWest(plot):
                if plot.west_border is PlotState.unknown:
                    self.check_west(plot)
                else:
                    # Already knows
                    pass
            else:
                plot.west_border = PlotState.none

            if self.hasSouth(plot):
                if plot.south_border is PlotState.unknown:
                    self.check_south(plot)
                else:
                    # Already knows
                    pass
            else:
                plot.south_border = PlotState.none

    def check_north(self, plot: Plot):
        next_point = plot.north()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.north_border = PlotState.intern
            next_plot.south_border = PlotState.intern
        else:
            plot.north_border = PlotState.extern
            next_plot.south_border = PlotState.extern

    def check_south(self, plot: Plot):
        next_point = plot.south()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.south_border = PlotState.intern
            next_plot.north_border = PlotState.intern
        else:
            plot.south_border = PlotState.extern
            next_plot.north_border = PlotState.extern

    def check_east(self, plot: Plot):
        next_point = plot.east()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.east_border = PlotState.intern
            next_plot.west_border = PlotState.intern
        else:
            plot.east_border = PlotState.extern
            next_plot.west_border = PlotState.extern

    def check_west(self, plot: Plot):
        next_point = plot.west()
        next_plot: Plot = self.plots[next_point.row][next_point.col]
        if self.check_point(next_point, plot.type):
            plot.west_border = PlotState.intern
            next_plot.east_border = PlotState.intern
        else:
            plot.west_border = PlotState.extern
            next_plot.east_border = PlotState.extern

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

    def next(self, direction: Direction, plot: Plot):
        if direction == Direction.north and not plot.north_border is PlotState.none:
            next_point = plot.north()
        elif direction == Direction.east and not plot.east_border is PlotState.none:
            next_point = plot.east()
        elif direction == Direction.west and not plot.west_border is PlotState.none:
            next_point = plot.west()
        elif direction == Direction.south and not plot.south_border is PlotState.none:
            next_point = plot.south()
        else:
            return None

        next_plot: Plot = self.plots[next_point.row][next_point.col]
        return next_plot

    def check_outer_corners(self, plot: Plot):
        north = self.next(Direction.north, plot)
        east = self.next(Direction.east, plot)
        west = self.next(Direction.west, plot)
        south = self.next(Direction.south, plot)
        if north and north.type != plot.type:
            if east and north.type == east.type:
                # get corner between
                north_east = self.next(Direction.east, north)
                if north_east.type == north.type:
                    north.corners += 1
            if west and north.type == west.type:
                # get corner between
                north_west = self.next(Direction.west, north)
                if north_west.type == north.type:
                    north.corners += 1
        if south and south.type != plot.type:
            if east and south.type == east.type:
                # get corner between
                south_east = self.next(Direction.east, south)
                if south_east.type == south.type:
                    south.corners += 1
            if west and south.type == west.type:
                # get corner between
                south_west = self.next(Direction.west, south)
                if south_west.type == south.type:
                    south.corners += 1

    def calc_border(self):
        for row, col in np.ndindex(self.garden.shape):
            plot: Plot = self.plots[row][col]
            plot.count_corners()
            self.check_outer_corners(plot)

    # def follow_border(self, plot: Plot):
    #     # find first start direction
    #     completed = False
    #     start_plot = plot
    #     direction = plot.get_start()
    #     while not completed:
    #         next_plot = self.next(direction, plot)
    #         if direction == Direction.east:
    #             if not next_plot.north_border is PlotState.intern:
    #                 # continue in direction
    #                 pass
    #             elif not plot.west_border is PlotState.intern:
    #
    #         if next_plot.row == plot.row and next_plot.col == plot.col:
    #             completed = True
    #
    #         plot = next_plot

    #
    # def get_sides(self):
    #     res = {}
    #     for row in range(self.height):
    #         region = Region()
    #         region_id = None
    #         nort_edges = 0
    #         south_edges = 0
    #         for col in range(self.width):
    #             plot: Plot = self.plots[row][col]
    #             if region_id != plot.region_id:
    #                 if not region_id is None:
    #                     if region_id in res:
    #                         region_obj: Region = res[region_id]
    #                         region_obj.edges += region.edges
    #                         region_obj.area += region.area
    #                     else:
    #                         res[region_id] = region
    #
    #                 # create new region
    #                 region = Region()
    #                 region.type = plot.type
    #                 region.area = 1
    #                 region.id = plot.region_id
    #                 region_id = plot.region_id
    #             else:
    #                 if not plot.north_border is PlotState.intern:
    #                     pass
    #                 else:
    #                     nort_edges += 1
    #

    # pricing
    def get_price(self):
        d = {}
        for row, col in np.ndindex(self.garden.shape):
            plot: Plot = self.plots[row][col]
            if plot.region_id in d:
                d[plot.region_id]["area"] += 1
                d[plot.region_id]["fences"] += plot.edges
                d[plot.region_id]["corners"] += plot.corners
            else:
                d[plot.region_id] = {
                    "area": 1,
                    "fences": plot.edges,
                    "type": plot.type,
                    "corners": plot.corners,
                }
        som = 0
        for key, val in d.items():
            total = val["area"] * (val["corners"])
            som += total
            print(
                f"{val['type']}: {total} | area: {val["area"]}, corners: {val["corners"] }"
            )

        print(som)


with open(file_name) as f:
    lines = f.readlines()
    grid = np.array([list(line.strip()) for line in lines])

    garden = Garden(grid)
    garden.fill_plots()
    garden.check_neighbours()
    garden.find_regions()
    garden.calc_border()
    garden.get_price()
