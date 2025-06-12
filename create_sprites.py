import pygame
import os

def create_snake_head():
    
    os.makedirs("assets/sprites", exist_ok=True)
    
    
    size = 20
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    
    pygame.draw.rect(surface, (0, 255, 0), (0, 0, size, size))
    pygame.draw.rect(surface, (0, 200, 0), (2, 2, size-4, size-4))
    
    
    pygame.draw.circle(surface, (255, 255, 255), (size-5, 5), 2)
    pygame.draw.circle(surface, (255, 255, 255), (size-5, size-5), 2)
    pygame.draw.circle(surface, (0, 0, 0), (size-4, 5), 1)
    pygame.draw.circle(surface, (0, 0, 0), (size-4, size-5), 1)
    
    
    pygame.image.save(surface, "assets/sprites/snake_head.png")

def create_snake_body():
    
    size = 20
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    
    pygame.draw.rect(surface, (0, 255, 0), (0, 0, size, size))
    pygame.draw.rect(surface, (0, 200, 0), (2, 2, size-4, size-4))
    
    
    pygame.draw.rect(surface, (0, 150, 0), (5, 5, size-10, size-10))
    
    
    pygame.image.save(surface, "assets/sprites/snake_body.png")

def create_food():
    
    size = 20
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    
    pygame.draw.circle(surface, (255, 0, 0), (size//2, size//2), size//2)
    pygame.draw.rect(surface, (0, 100, 0), (size//2-2, 0, 4, 5))
    
    
    pygame.image.save(surface, "assets/sprites/food.png")

def main():
    pygame.init()
    create_snake_head()
    create_snake_body()
    create_food()
    pygame.quit()

if __name__ == "__main__":
    main() 