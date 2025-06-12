import pygame
import sys
from game.game import Game
from database.database import Database

def main():
    # Inicializa o Pygame
    pygame.init()
    
    # Inicializa o banco de dados
    db = Database()
    db.create_tables()
    
    # Cria e inicia o jogo
    game = Game()
    game.run()
    
    # Finaliza o Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 