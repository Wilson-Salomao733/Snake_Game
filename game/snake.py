from .entity import Entity
import pygame

class Snake(Entity):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, (0, 255, 0), "assets/sprites/snake_head.png")
        self.direction = "RIGHT"
        self.body = [(x, y)]
        self.grow = False
        
        
        self.body_sprite = pygame.image.load("assets/sprites/snake_body.png")
        self.body_sprite = pygame.transform.scale(self.body_sprite, (size, size))
    
    def move(self):
        if self.direction == "RIGHT":
            self.x += self.size
        elif self.direction == "LEFT":
            self.x -= self.size
        elif self.direction == "UP":
            self.y -= self.size
        elif self.direction == "DOWN":
            self.y += self.size
        
        self.body.insert(0, (self.x, self.y))
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
        self.update()
    
    def change_direction(self, new_direction):
        opposites = {
            "RIGHT": "LEFT",
            "LEFT": "RIGHT",
            "UP": "DOWN",
            "DOWN": "UP"
        }
        if opposites.get(new_direction) != self.direction:
            self.direction = new_direction
            
            
            if new_direction == "UP":
                self.sprite = pygame.transform.rotate(self.sprite, 90)
            elif new_direction == "DOWN":
                self.sprite = pygame.transform.rotate(self.sprite, -90)
            elif new_direction == "LEFT":
                self.sprite = pygame.transform.rotate(self.sprite, 180)
            elif new_direction == "RIGHT":
                self.sprite = pygame.transform.rotate(self.sprite, 0)
    
    def grow_snake(self):
        self.grow = True
    
    def check_collision(self, width, height):
        
        if (self.x < 0 or self.x >= width or 
            self.y < 0 or self.y >= height):
            return True
        
        
        if (self.x, self.y) in self.body[1:]:
            return True
        
        return False
    
    def draw(self, screen):
        
        for segment in self.body[1:]:
            rect = pygame.Rect(segment[0], segment[1], self.size, self.size)
            screen.blit(self.body_sprite, rect)
        
        
        screen.blit(self.sprite, self.rect) 