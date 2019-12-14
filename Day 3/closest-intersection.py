# take into account that the same line crossing should not contribute to the distance
import numpy as np

def markGridPosition(grid, pos_1, pos_2, intersecting_distance, line_number):
    if pos_1 not in grid:
        grid[pos_1] = {}

    if pos_2 not in grid[pos_1]:
        grid[pos_1][pos_2] = line_number
    elif line_number != grid[pos_1][pos_2]:
        distance = abs(pos_1) + abs(pos_2)
        intersecting_distance.append(distance)

def insertLineIntoGrid(grid, line, intersecting_distance, line_number):
    position = (0,0)
    segmentsList = line.split(',')

    for segment in segmentsList:
        direction = segment[0]
        magnitude = int(segment[1:])
        if direction == 'L':
            for i in range(position[0], position[0] - magnitude, -1):
                markGridPosition(grid, i, position[1], intersecting_distance, line_number)
            position = (position[0] - magnitude, position[1])
        elif direction == 'R':
            for i in range(position[0], position[0] + magnitude, 1):
                markGridPosition(grid, i, position[1], intersecting_distance, line_number)
            position = (position[0] + magnitude, position[1])
        elif direction == 'U':
            for i in range(position[1], position[1] + magnitude, 1):
                markGridPosition(grid, position[0], i, intersecting_distance, line_number)
            position = (position[0], position[1] + magnitude)
        elif direction == 'D':
            for i in range(position[1], position[1] - magnitude, -1):
                markGridPosition(grid, position[0], i, intersecting_distance, line_number)
            position = (position[0], position[1] - magnitude)

def main():
    # Read in the file
    line_input = open('input.txt', 'r')
    grid = {}
    intersecting_distance = []
    line_number = 1
    for line in line_input.readlines():
        line_id = line_number
        insertLineIntoGrid(grid, line, intersecting_distance, line_number)
        line_number += 1

    intersecting_distance.remove(0)
    print(min(intersecting_distance))
    
if __name__ == "__main__":
    main()