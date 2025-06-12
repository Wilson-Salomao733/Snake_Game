import pygame
import sys
from .snake import Snake
from .food import Food
from database.database import Database

class Game:
    def __init__(self):
        
        self.width = 800
        self.height = 600
        self.cell_size = 20
        
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        
        
        self.snake = Snake(self.width//2, self.height//2, self.cell_size)
        self.food = Food(self.cell_size, self.width, self.height)
        self.score = 0
        self.game_over = False
        self.db = Database()
        
        
        self.font = pygame.font.Font(None, 36)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
    
    def update(self):
        if not self.game_over:
            self.snake.move()
            
            
            if self.snake.rect.colliderect(self.food.rect):
                self.snake.grow_snake()
                self.food.respawn(self.snake.body)
                self.score += 10
            
            
            if self.snake.check_collision(self.width, self.height):
                self.game_over = True
                self.db.save_score("Player", self.score)
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to restart", True, (255, 255, 255))
            text_rect = game_over_text.get_rect(center=(self.width//2, self.height//2))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()
    
    def reset_game(self):
        self.snake = Snake(self.width//2, self.height//2, self.cell_size)
        self.food = Food(self.cell_size, self.width, self.height)
        self.score = 0
        self.game_over = False
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  