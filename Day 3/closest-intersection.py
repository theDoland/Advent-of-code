# take into account that the same line crossing should not contribute to the distance
import numpy as np

class GridMarker:
    def __init__(self, step_count, line_id):
        self.step_count = step_count
        self.line_id = line_id
    
def markGridPosition(grid, pos_1, pos_2, intersecting_distance, grid_marker):
    if pos_1 not in grid:
        grid[pos_1] = {}

    if pos_2 not in grid[pos_1]:
        grid[pos_1][pos_2] = grid_marker
    elif grid_marker.line_id != grid[pos_1][pos_2].line_id:
        distance = grid[pos_1][pos_2].step_count + grid_marker.step_count
        intersecting_distance.append(distance)

def insertLineIntoGrid(grid, line, intersecting_distance, line_id):
    step_count = 0
    position = (0,0)
    segmentsList = line.split(',')

    for segment in segmentsList:
        direction = segment[0]
        magnitude = int(segment[1:])
        if direction == 'L':
            for i in range(position[0], position[0] - magnitude, -1):
                markGridPosition(grid, i, position[1], intersecting_distance, GridMarker(step_count, line_id))
                step_count += 1
            position = (position[0] - magnitude, position[1])
        elif direction == 'R':
            for i in range(position[0], position[0] + magnitude, 1):
                markGridPosition(grid, i, position[1], intersecting_distance, GridMarker(step_count, line_id))
                step_count += 1
            position = (position[0] + magnitude, position[1])
        elif direction == 'U':
            for i in range(position[1], position[1] + magnitude, 1):
                markGridPosition(grid, position[0], i, intersecting_distance, GridMarker(step_count, line_id))
                step_count += 1
            position = (position[0], position[1] + magnitude)
        elif direction == 'D':
            for i in range(position[1], position[1] - magnitude, -1):
                markGridPosition(grid, position[0], i, intersecting_distance, GridMarker(step_count, line_id))
                step_count += 1
            position = (position[0], position[1] - magnitude)

def main():
    # Read in the file
    line_input = open('input.txt', 'r')
    grid = {}
    intersecting_distance = []
    line_id = 1
    for line in line_input.readlines():
        insertLineIntoGrid(grid, line, intersecting_distance, line_id)
        line_id += 1

    intersecting_distance.remove(0)
    print(min(intersecting_distance))
    
if __name__ == "__main__":
    main()