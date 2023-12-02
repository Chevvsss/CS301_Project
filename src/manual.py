import pygame
import sys

# Constants
GRID_SIZE = 3
CUBE_SIZE = 80
WINDOW_SIZE = (GRID_SIZE * CUBE_SIZE, GRID_SIZE * CUBE_SIZE)
COLORS = [(255, 255, 255), (255, 165, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]
order = ['yellow', 'blue', 'red', 'green', 'orange', 'white']

# Main game loop
def main_manual():
    # Initialize Pygame
    pygame.init()

    # Create the window
    screen = pygame.display.set_mode(WINDOW_SIZE)
    # Initial cube state
    rubiks_cube = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    # Function to draw the Rubik's Cube
    def draw_rubiks_cube():
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                color = COLORS[rubiks_cube[i][j]]
                rect = pygame.Rect(j * CUBE_SIZE, i * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    # Function to rotate a face of the Rubik's Cube
    def rotate_face(row, col):
        rubiks_cube[row][col] = (rubiks_cube[row][col] + 1) % len(COLORS)

    # Function to convert the cube state to a string of colors
    def cube_to_string():
        color_str = ''.join([str(rubiks_cube[i][j]) for i in range(GRID_SIZE) for j in range(GRID_SIZE)])
        result = ''
        for char in color_str:
            if char == '0':
                result += 'w'
            elif char == '1':
                result += 'o'
            elif char == '2':
                result += 'g'
            elif char == '3':
                result += 'r'
            elif char == '4':
                result += 'b'
            elif char == '5':
                result += 'y'
        return result

    cube_states = []
    counter = 0

    print(f"Enter {order[counter]} Face while the red center is in DOWN face")

    while counter < 6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // CUBE_SIZE
                row = y // CUBE_SIZE
                rotate_face(row, col)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(f"{order[counter]} Face saved!")
                    cube_states.append(cube_to_string())
                    counter += 1
                    if counter < 6:  # Check if there are more faces to input
                        if order[counter] == 'white':
                            print(f"Enter {order[counter]} Face while the red center is in UP face")
                        if order[counter] != 'white':
                            print(f"Enter {order[counter]} Face while the Yellow center is in UP face")

        screen.fill((255, 255, 255))  # Clear the screen
        draw_rubiks_cube()  # Draw the Rubik's Cube

        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(30)  # Cap the frame rate

    pygame.quit()  # Quit Pygame when the loop is done
    return ''.join(cube_states)

if __name__ == '__main__':
    main_manual()
"""    if order[counter] != 'yellow' and order[counter] != 'white':
        print(f"Enter {order[counter]} Face while the yellow center is in UP face")
    elif order[counter] == 'yellow':
        print(f"Enter {order[counter]} Face while the red center is in DOWN face")
    elif order[counter] == 'white':
        print(f"Enter {order[counter]} Face while the red center is in UP face")"""