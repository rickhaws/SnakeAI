# Snake game written by ChatGPT in May 2023


import pygame
import random

# Define constants
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
BG_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
SCORE_FONT = "Arial"
SCORE_SIZE = 30
SCORE_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define classes
class Snake:
    def __init__(self):
        self.body = [(WIDTH/2, HEIGHT/2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        
    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()
        
    def grow(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE
        self.body.insert(0, (x, y))
        
    def change_direction(self, direction):
        if (direction == "UP" and self.direction != "DOWN" or
            direction == "DOWN" and self.direction != "UP" or
            direction == "LEFT" and self.direction != "RIGHT" or
            direction == "RIGHT" and self.direction != "LEFT"):
            self.direction = direction
            
    def check_collision(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        for i in range(1, len(self.body)):
            if self.body[i] == self.body[0]:
                return True
        return False
    
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, SNAKE_COLOR, (x, y, CELL_SIZE, CELL_SIZE))
            
class Food:
    def __init__(self):
        self.x = random.randrange(0, WIDTH, CELL_SIZE)
        self.y = random.randrange(0, HEIGHT, CELL_SIZE)
        
    def check_eaten(self, snake):
        if (self.x, self.y) == snake.body[0]:
            return True
        return False
        
    def draw(self):
        pygame.draw.rect(window, FOOD_COLOR, (self.x, self.y, CELL_SIZE, CELL_SIZE))
        
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE)
        
    def increase(self):
        self.value += 1
        
    def draw(self):
        score_text = self.font.render(f"Score: {self.value}", True, SCORE_COLOR)
        window.blit(score_text, (10, 10))
        
# Create game objects
snake = Snake()
food = Food()
score = Score()

# Start game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
                
    # Move the snake
    snake.move()
    
    # Check for collision with food
    if food.check_eaten(snake):
        snake.grow()
        food = Food()
        score.increase()
    
    # Check for collision with wall or body
    if snake.check_collision():
        running = False
        
    # Draw the game objects
    window.fill(BG_COLOR)
    snake.draw()
    food.draw()
    score.draw()
    pygame.display.update()
    
# Quit Pygame
pygame.quit()

