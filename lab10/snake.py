import random
import sys
import pygame
import snake_table as sn

import pygame
pygame.init()
#screen information
screen = pygame.display.set_mode((500, 500))
#food colors
RED = (238,44,44)
YELLOW = (255,215,0)
score_font = pygame.font.SysFont("comicsansms", 17)
pausef = pygame.font.SysFont("comicsansms", 50)
colors = (RED,RED,YELLOW,RED)
#score
def Your_score(score, levelnum):
    value = score_font.render("Score: " + str(score), True, (255,193,37) )
    screen.blit(value, [410, 0])
    levelnum = score_font.render("Level: " + str(levelnum), True,(233,150,122)  )
    screen.blit(levelnum, [10, 0])
#loading walls from the working directory
def load_wall(level):
    with open(f'levels/level{level}.txt', 'r') as f:
        global wall_body
        wall_body = f.readlines()
        
def pause():
    paused = True
    while paused:
        if sn.score < snake.score:
            sn.sql = f"""
                    update snake
                    set score = '{snake.score}'
                    where username = '{sn.user}';
                    """
            sn.cursor.execute(sn.sql)
        if sn.level < wall.level:
            sn.sql = f"""
                    update snake
                    set level = '{wall.level}'
                    where username = '{sn.user}';
                    """
            sn.cursor.execute(sn.sql)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
        
                elif event.key == pygame.K_q:
                    pygame.quit()
        screen.fill((255,255,255))
        value = pausef.render("PAUSED", True, (200,193,137) )
        screen.blit(value, [150,170])
        value = score_font.render("Click C to continue, click Q to quit", True, (200,193,137) )
        screen.blit(value, [120,250])
        Your_score(snake.score, wall.level)
        pygame.display.update()
        clock.tick(5)

class Wall:
     #appending coordinates of # from files
  def __init__(self):
    self.body = []
    self.level = 0
    load_wall(self.level)
    for i, line in enumerate(wall_body):
      for j, value in enumerate(line):
        if value == '#':
          self.body.append([j, i])
     #new level update  
  def update(self) :
    self.level += 1
    load_wall(self.level)
    for i, line in enumerate(wall_body):
      for j, value in enumerate(line):
        if value == '#':
          self.body.append([j, i])
     #drawing walls
  def draw(self):
    for x, y in self.body:
      pygame.draw.rect(screen, (230,85,175), (x * 20, y * 20, 20, 20))


class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]] 
        self.radius = 10
        self.dx = 5  # Right.
        self.dy = 0
        self.is_add = False
        self.speed = 30
        self.score = 0

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen,(84,139,84), element , self.radius)
     #adding circles to the end of the snake
    def add_to_snake(self, food_color):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
          #if usual then +1 if rare then +3
        if food_color == RED:
            self.score += 1
        else:
            self.score += 3
        #increasing level and speed when size is divisible by 4  
        if (self.size - 1) % 4 == 0:
            self.speed += 5
            if wall.level < 4 :
                wall.update()
    #moving snake         
    def move(self):
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
  
    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx - 10 <= x <= foodx + 30 and foody - 10 <= y <= foody + 30:
            return True
        return False
#if snake hit itself then game over
    def check_fail(self):
        for block in self.elements[1:]:
            if block == self.elements[0]:
                self.game_over()
 #quit if game over
    def game_over(self):
        if sn.score < snake.score:
            sn.sql = f"""
                    update snake
                    set score = '{snake.score}'
                    where username = '{sn.user}';
                    """
            sn.cursor.execute(sn.sql)
        if sn.level < wall.level:
            sn.sql = f"""
                    update snake
                    set level = '{wall.level}'
                    where username = '{sn.user}';
                    """
            sn.cursor.execute(sn.sql)
        pygame.quit()
        sys.exit()
class Food:
    def __init__(self):
        #randomly choosing food
        self.color = random.choice(colors)
        self.x = random.randint(0, 480)
        self.y = random.randint(0, 480)
        #different sizes of food
        self.w = 10 if self.color == RED else 18

    def gen(self):
        self.color = random.choice(colors)
        #if color is not green, make food bigger
        self.w = 10 if self.color == RED else 18
        self.x = random.randint(0, 500 - self.w)
        self.y = random.randint(0, 500 - self.w)

    def draw(self):
        pygame.draw.rect(screen, self.color , (self.x, self.y ,self.w, self.w))
#calling classes
snake = Snake(100, 100)
wall = Wall()
food = Food()
running = True
#FramePerSecond
FPS = 30
d = 5
clock = pygame.time.Clock()
while running:
 #moving snake
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d  
            if event.key == pygame.K_p:
                pause()
    if snake.eat(food.x, food.y):
        #getting longer length by eating food, if snake collides with food then food goes to another place
        snake.is_add = True
        snake.add_to_snake(food.color)
        food.gen()
    #when snake and food collides with wall
    for x, y in wall.body :
        rect = pygame.Rect(x * 20 + 10 , y * 20 + 10 , 20, 20)
        rect2 = pygame.Rect(x * 20 - 10 , y * 20 - 10 , 20, 20)
        if rect.collidepoint(snake.elements[0]) or rect2.collidepoint(snake.elements[0]):
            snake.game_over()
        if rect.collidepoint(food.x,food.y) or rect2.collidepoint(food.x,food.y):
            food.gen()
    #if snake reaches the end of the screen , it appears from another end
    if snake.elements[0][0] > 490:
        snake.elements[0][0] = 0
    if snake.elements[0][0] < 0:
        snake.elements[0][0] = 490
    if snake.elements[0][1] > 490:
        snake.elements[0][1] = 0
    if snake.elements[0][1] < 0:
        snake.elements[0][1] = 490
    snake.move()
    #timer for the yellow food
    if food.color == YELLOW :
            if food.w >= 0:
                food.w -= 0.1
            if food.w < 0 :
                food.gen()
    screen.fill((255,255,255))
    snake.draw()
    food.draw()
    snake.check_fail()
    wall.draw()
    Your_score(snake.score, wall.level)

    pygame.display.flip()

sn.cursor.close()
pygame.quit()