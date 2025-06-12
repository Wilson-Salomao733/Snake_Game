import pygame

class Entity:
    def __init__(self, x, y, size, color, sprite_path=None):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)
        
        
        if sprite_path:
            self.sprite = pygame.image.load(sprite_path)
            self.sprite = pygame.transform.scale(self.sprite, (size, size))
        else:
            self.sprite = None
    
    def draw(self, screen):
        if self.sprite:
            screen.blit(self.sprite, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y 