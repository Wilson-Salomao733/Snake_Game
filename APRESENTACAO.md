# Snake Game
## Apresentação do Projeto

---

## Contextualização

- Recriação moderna do clássico jogo da cobrinha
- Desenvolvido em Python com Pygame
- Implementa banco de dados SQLite
- Interface gráfica com sprites personalizados

---

## Arquitetura do Projeto

### Estrutura de Classes
- `Entity`: Classe base para objetos do jogo
- `Snake`: Implementa a lógica da cobra
- `Food`: Implementa a lógica da comida
- `Game`: Gerencia o jogo
- `Database`: Gerencia o banco de dados

---

## Critérios Avaliativos

### 1. Funções do Curso
- Classes e Objetos
- Herança (Entity → Snake, Food)
- Polimorfismo (métodos draw() e update())

### 2. Banco de Dados
- SQLite3 para armazenar pontuações
- Tabela `scores` com histórico de jogadas

---

## Demonstração do Código

### Exemplo de Herança
```python
class Snake(Entity):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, (0, 255, 0))
```

### Exemplo de Polimorfismo
```python
# Entity
def draw(self, screen):
    pygame.draw.rect(screen, self.color, self.rect)

# Snake
def draw(self, screen):
    for segment in self.body[1:]:
        screen.blit(self.body_sprite, rect)
    screen.blit(self.sprite, self.rect)
```

---

## Demonstração do Jogo

### Funcionalidades
1. Movimentação da cobra
2. Coleta de alimentos
3. Sistema de pontuação
4. Salvamento de recordes
5. Interface gráfica

### Controles
- Setas do teclado para mover
- R para reiniciar

---

## Conclusão

### Resultados
- Jogo completo e funcional
- Código organizado e documentado
- Implementação de todos os requisitos

### Aprendizados
- Programação Orientada a Objetos
- Desenvolvimento de jogos
- Banco de dados
- Versionamento de código

---

## Obrigado!
### Perguntas? 