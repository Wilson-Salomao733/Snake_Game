# Snake Game
## Jogo da Cobrinha com Interface Gráfica e Banco de Dados

### Integrantes do Grupo
- Wilson Salomão

---

## 1. Introdução

O Snake Game é uma recriação moderna do clássico jogo da cobrinha, desenvolvido em Python utilizando a biblioteca Pygame. O objetivo do jogo é controlar uma cobra que deve coletar alimentos para crescer e ganhar pontos, evitando colidir com as paredes ou com o próprio corpo.

### Objetivos do Jogo
- Controlar a cobra usando as setas do teclado
- Coletar alimentos para aumentar o tamanho da cobra
- Acumular pontos
- Evitar colisões com as paredes e com o próprio corpo
- Competir por recordes salvos no banco de dados

---

## 2. Desenvolvimento

### 2.1 Critérios Avaliativos Implementados

#### 2.1.1 Funções Vistas Durante o Curso
- **Classes e Objetos**: Implementadas 5 classes principais:
  - `Entity`: Classe base para objetos do jogo
  - `Snake`: Classe que herda de Entity e implementa a lógica da cobra
  - `Food`: Classe que herda de Entity e implementa a lógica da comida
  - `Game`: Classe principal que gerencia o jogo
  - `Database`: Classe para gerenciar o banco de dados

- **Herança**: Implementada através da classe `Entity` que serve como base para `Snake` e `Food`
  ```python
  class Snake(Entity):
      def __init__(self, x, y, size):
          super().__init__(x, y, size, (0, 255, 0), "assets/sprites/snake_head.png")
  ```

- **Polimorfismo**: Demonstrado através da sobrescrita de métodos nas classes filhas:
  ```python
  # Na classe Entity
  def draw(self, screen):
      pygame.draw.rect(screen, self.color, self.rect)

  # Na classe Snake
  def draw(self, screen):
      for segment in self.body[1:]:
          rect = pygame.Rect(segment[0], segment[1], self.size, self.size)
          screen.blit(self.body_sprite, rect)
      screen.blit(self.sprite, self.rect)
  ```

#### 2.1.2 Banco de Dados
- Implementado usando SQLite3 para armazenar pontuações
- Tabela `scores` com campos:
  - id (chave primária)
  - player_name
  - score
  - date

#### 2.1.3 Interface Gráfica
- Desenvolvida usando Pygame
- Elementos visuais:
  - Sprites personalizados para a cobra e comida
  - Sistema de pontuação
  - Mensagens de game over
  - Animações suaves

#### 2.1.4 Criatividade
- Sprites personalizados gerados programaticamente
- Sistema de rotação da cabeça da cobra baseado na direção
- Diferentes sprites para cabeça e corpo da cobra
- Comida em formato de maçã

---

## 3. Conclusão

### 3.1 Resultado do Projeto
O projeto foi concluído com sucesso, atendendo a todos os requisitos solicitados:
- Implementação completa do jogo da cobrinha
- Sistema de banco de dados funcionando
- Interface gráfica intuitiva e atraente
- Código organizado e bem estruturado
- Documentação completa

### 3.2 Contribuição para o Desenvolvimento do Conhecimento
O desenvolvimento deste projeto proporcionou:
1. **Aprendizado Prático**:
   - Aplicação dos conceitos de Programação Orientada a Objetos
   - Uso de herança e polimorfismo em um contexto real
   - Implementação de banco de dados em Python

2. **Desenvolvimento de Habilidades**:
   - Trabalho com bibliotecas gráficas (Pygame)
   - Manipulação de sprites e animações
   - Gerenciamento de estados do jogo
   - Implementação de lógica de colisão

3. **Conhecimentos Adicionais**:
   - Versionamento de código com Git
   - Documentação de projetos
   - Organização de código em módulos
   - Gerenciamento de dependências

---

## 4. Instruções para Execução

1. Instalar as dependências:
```bash
pip install -r requirements.txt
```

2. Executar o jogo:
```bash
python main.py
```

3. Controles:
- Setas do teclado para mover a cobra
- R para reiniciar após game over

---

## 5. Demonstração

O jogo pode ser demonstrado executando o arquivo `main.py`. Durante a demonstração, será possível observar:
1. Movimentação suave da cobra
2. Coleta de alimentos e crescimento
3. Sistema de pontuação
4. Salvamento automático de recordes
5. Interface gráfica com sprites personalizados 