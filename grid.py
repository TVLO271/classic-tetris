import pygame
from colors import Colors

#create grid size and format for game pieces
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        #call from the Colors class 
        self.colors = Colors.get_cell_colors()
        
    #used to print grid and values
    def print_grid(self):
        for row in range(self.num_cols):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    
    #drawing grid/ assigning values 
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                #creating cell of the grid (x, y, w, h), edit cells to have game be 29 pixels
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)