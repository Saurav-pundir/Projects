import pygame
from pygame.locals import *
import time
import random

pygame.init()
pygame.display.set_caption("Snake Game")

SIZE = 30
BACKGROUND_COLOR = (111,111,2)
class Apple:
    def __init__(self,parent_screen) :
        self.apple = pygame.image.load("apple.png").convert_alpha()
        self.parent_screen = parent_screen
        self.x = SIZE*random.randint(3,15)
        self.y = SIZE*random.randint(3,15)

    def draw(self):
        self.parent_screen.blit(self.apple,(self.x,self.y))
        pygame.display.flip()

    def move(self,snake_x,snake_y):
        while True:
            new_x = random.randint(0,29)*SIZE
            new_y = random.randint(0,19)*SIZE
            collides_with_snake = any(new_x == x and new_y == y for x, y in zip(snake_x, snake_y))
            if not collides_with_snake:
                self.x = new_x
                self.y = new_y
                break

class snake:
    def __init__(self,parent_screen,length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("square.png").convert()
        self.direction = "down"
       
        self.length = length
        self.x = [SIZE]*length
        self.y = [SIZE]*length

    def increase_length(self):
        self.length+=1
        self.x.append(1)
        self.y.append(1)


    def move_up(self):
        if self.direction != "down":
            self.direction="up"
    def move_down(self):
        if self.direction != "up":
            self.direction="down"
    def move_left(self):
        if self.direction != "right":
            self.direction="left"
    def move_right(self):
        if self.direction != "left":
            self.direction="right"
    

    def walk(self):
        if self.direction=="up":
            self.y[0] -=SIZE
            if self.y[0] == -30:
                self.y[0] = 570
        elif self.direction=="down":
            self.y[0] +=SIZE
            if self.y[0] >= 600:
                self.y[0] = 0
        elif self.direction=="left":
            self.x[0] -=SIZE
            if self.x[0] == -30:
                self.x[0] = 870
        elif self.direction=="right":
            self.x[0] +=SIZE
            if self.x[0] >= 900:
                self.x[0] = 0
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1] 
        self.draw()

    def draw(self):
        self.parent_screen.fill((BACKGROUND_COLOR))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()


class Game:
    def __init__(self) :
        pygame.init()
        self.surface =  pygame.display.set_mode((900,600))
        self.surface.fill((27, 233, 245))
        self.snake = snake(self.surface,2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()


    def collision(self, x1, y1, x2, y2):
        rect1 = pygame.Rect(x1, y1, SIZE, SIZE)
        rect2 = pygame.Rect(x2, y2, SIZE, SIZE)
        return rect1.colliderect(rect2)

    

    def score(self):
        font = pygame.font.SysFont("arial",32,bold=5)
        score = font.render(f"Score:{self.snake.length-1}",True,(255,255,255))
        self.surface.blit(score,(400,35))


    def play(self):
            self.snake.walk()
            self.apple.draw()
            self.score()
            pygame.display.flip()

            # snake coliding with apple
            if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move(self.snake.x,self.snake.y)

            #snake coliding with itself
            for i in range(2,self.snake.length):
                if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                    raise Exception ("Game Over")

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial',35)
        line1 = font.render(f"Game Over! Total Score:{self.snake.length -1 }",True,(255,255,255))
        self.surface.blit(line1,(200,300))
        line2 = font.render(f"Press Enter to play again . To exit press Escape.",True,(255,255,255))
        self.surface.blit(line2,(200,350))
        pygame.display.flip()

    def reset(self):
        self.snake = snake(self.surface, 2)
        self.apple = Apple(self.surface)
        self.surface.fill((27, 233, 245))
        self.snake.draw()
        self.apple.draw()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False
        while running :
            for event in pygame.event.get():
                if event.type == QUIT:
                        running = False
                elif event.type==KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            running = False
                        if event.key == K_RETURN:
                            self.reset()
                            pause = False
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:                        
                            self.snake.move_right()
   
            try :
                if not pause:
                    self.play()
            except Exception as e :
                self.show_game_over()
                pause = True
                print(e)
            time.sleep(0.3)
        

if __name__=="__main__":
    game = Game()
    game.run()
