from .entity import Entity
import random

class Food(Entity):
    def __init__(self, size, width, height):
        x = random.randrange(0, width, size)
        y = random.randrange(0, height, size)
        super().__init__(x, y, size, (255, 0, 0), "assets/sprites/food.png")
        self.width = width
        self.height = height
    
    def respawn(self, snake_body):
        while True:
            self.x = random.randrange(0, self.width, self.size)
            self.y = random.randrange(0, self.height, self.size)
            self.update()
            
            
            if (self.x, self.y) not in snake_body:
                break 