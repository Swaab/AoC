file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day2/input.txt"

import re
import sys
class Game:

    def __init__(self, s: str):
        game, sets =  s.split(":")
        self.id = int(re.findall(r'\d+', game)[0])
        self.sets = sets.split(";")
        self.min_red = 1
        self.min_blue = 1
        self.min_green = 1


    def min_set_power(self):
        print(self.sets)
        for set in self.sets:
            colors = set.split(',')
            for color in colors:
                if "green" in color:
                    green = int(re.findall(r'\d+', color)[0])
                    if green > self.min_green:
                        self.min_green = green
                elif "red" in color:
                    red = int(re.findall(r'\d+', color)[0])
                    if red > self.min_red:
                        self.min_red = red
                elif "blue" in color:
                    blue = int(re.findall(r'\d+', color)[0])
                    if blue > self.min_blue:
                        self.min_blue = blue
                else:
                    raise Exception(f"no color found: {color} ")
            print(self.min_green, self.min_red, self.min_blue)
        return self.min_red * self.min_blue * self.min_green

    def is_valid(self):
        """only 12 red cubes, 13 green cubes, and 14 blue cubes?"""
        reds = 12
        blues = 14
        greens = 13
        green = 0
        red = 0
        blue = 0
        for set in self.sets:
            colors = set.split(',')
            for color in colors:
                if "green" in color:
                    green = int(re.findall(r'\d+', color)[0])
                elif  "red" in color:
                    red = int(re.findall(r'\d+', color)[0])
                elif "blue" in color:
                    blue = int(re.findall(r'\d+', color)[0])
                else:
                    raise Exception(f"no color found: {color} ")

            if red > reds or green> greens or blue > blues:
                return False
        return True


sum = 0
with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
        game = Game(line)
        # part A
        # if game.is_valid():
        #     sum+= game.id
        # Part B
        sum += game.min_set_power()


print(sum)