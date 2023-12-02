import cv2
import numpy as np
"""
    We're gonna display the visualization like so:
                -----
                | Y Y Y |
                | Y Y Y |
                | Y Y Y |
        -----   -----   -----   -----
        | B B B | R R R | G G G | O O O |
        | B B B | R R R | G G G | O O O |
        | B B B | R R R | G G G | O O O |
        -----   -----   -----   -----
                | W W W |
                | W W W |
                | W W W |
                -----
    """
grid = {
    'white': [1, 2],
    'orange': [3, 1],
    'green': [2, 1],
    'red': [1, 1],
    'blue': [0, 1],
    'yellow': [1, 0],
    }

color_map = {
    'white': (255, 255, 255),
    'orange': (0, 165, 255),
    'green': (0, 255, 0),
    'red': (0, 0, 255),
    'blue': (255, 0, 0),
    'yellow': (0, 255, 255),
    }


def draw_2d_cube_state(image, faces):

    cube_simple = np.zeros((3,4),dtype=object)
    for face in faces.values():
        cube_simple[grid[face.name][1],grid[face.name][0]] = face.face
    

 #draw a 4x3 grid
    for i in grid:
        x = grid[i][0]
        y = grid[i][1]
        #split each section into 3x3
        for j in range(3):
            for k in range(3):
                #get the color of the center of the contour
                color = cube_simple[y][x][j][k]
                #draw a rectangle on the center of the contour
                if color != None:
                    cv2.rectangle(image, (x*80+k*27, y*80+j*27), (x*80+k*27+27, y*80+j*27+27), color_map[color], -1)
                cv2.rectangle(image, (x*80+k*27, y*80+j*27), (x*80+k*27+27, y*80+j*27+27), (0,0,0), 1)

    color_cycle = {(i, j): 0 for i in range(3) for j in range(4)}

    # Function to handle mouse events

    return image

    

