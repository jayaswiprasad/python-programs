import pygame
import math

# Initialize Pygame
pygame.init()

# Set the size of the window and the caption
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("3D Cube")

# Set the color of the cube
color = (255, 255, 255)

# Define the cube vertices
vertices = [(0, 0, 0), (0, 100, 0), (100, 100, 0), (100, 0, 0), (0, 0, 100), (0, 100, 100), (100, 100, 100), (100, 0, 100)]

# Define the edges that connect the vertices
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

# Define the angle to rotate the cube
angle = 0

# Define the distance of the camera from the cube
distance = 1000

# Define the main game loop
while True:
    # Clear the screen
    screen.fill((0, 0, 0))

    # Rotate the cube
    angle += 0.01

    # Define the projected vertices
    projected_vertices = []

    # Project the vertices onto the 2D screen
    for vertex in vertices:
        # Rotate the vertex around the y-axis
        x = vertex[0] * math.cos(angle) + vertex[2] * math.sin(angle)
        y = vertex[1]
        z = -vertex[0] * math.sin(angle) + vertex[2] * math.cos(angle)

        # Calculate the distance from the camera to the vertex
        distance_from_camera = 1 / (z / distance)

        # Calculate the 2D coordinates of the vertex on the screen
        x = x * distance_from_camera + 250
        y = y * distance_from_camera + 250

        projected_vertices.append((x, y))

    # Draw the edges of the cube
    for edge in edges:
        pygame.draw.line(screen, color, projected_vertices[edge[0]], projected_vertices[edge[1]], 1)

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
