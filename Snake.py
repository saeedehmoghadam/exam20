import random
import time
import arcade

width = 600
height = 400


class Apple(arcade.Sprite):
    def __init__(self,w,h):
        arcade.Sprite.__init__(self)
        self.color=arcade.color.RED
        self.width=16
        self.height=16
        self.center_x=random.randint(0, w)
        self.center_y=random.randint(0, h)
        self.r=8
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)
        
class Snake(arcade.Sprite):
    def __init__(self,width,height):
        arcade.Sprite.__init__(self) 
        self.center_x=width // 2
        self.center_y=height // 2
        self.color2=arcade.color.BLUE
        self.color3=arcade.color.YELLOW
        self.color1=arcade.color.MAGENTA
        self.x_change=0
        self.y_change=0
        self.width=16
        self.height=16
        self.score=0
        self.r=10
        self.speed=3
        self.body=[]
        self.body.append([self.center_x, self.center_y])
        

    def drow(self):
        for i in range(len(self.body)):
            if i == 0:
                arcade.draw_circle_filled(self.body[i][0],self.body[i][1],self.r,self.color)
            else:
                arcade.draw_circle_filled(self.body[i][0],self.body[i][1],self.r,self.body_color)  



    def move(self):
       self.body.append({'x':self.center_x,'y':self.center_y})
       if len(self.body)>self.score:
           self.body.remove(self.body[0])
       if self.x_change==-1:
           self.center_x-=self.speed  

       elif self.x_change==1:
           self.center_x+=self.speed

       elif self.y_change==-1:
           self.center_y-=self.speed  

       elif self.y_change==1:
           self.center_y+=self.speed            

    def eat(self, food):
        if food == 'apple':
            self.score += 1
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
        elif food == 'flower':
            self.score += 2
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
        elif food == 'cactus':
            self.score -= 1
            self.body.pop()

class My_game_window(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,width,height,"snake game")
        arcade.set_background_color(arcade.color.GRAY)
        self.snake = Snake(width,height) 
        self.apple = Apple(width,height)
        self.flower = Flower(width,height)
        self.cactus = Cactus(width,height)
        self.body=0
        self.exit=0

    def on_draw(self):
         arcade.start_render()
         self.snake.draw()
         self.apple.draw()
         self.flower.draw()
         self.cactus.draw()
         arcade.draw_text(
             f"{self.snake.score}",20,400,arcade.color.YELLOW_ROSE,28
         )
        #  if self.snake.score < 0 or self.snake.center_x < 0 or self.snake.center_x > self.width or self.snake.center_y > self.height :
        #     arcade.draw_text(
        #         "GAME OVER",10,40,arcade.color.RED,28
        #         )
        #     time.sleep(2)
        #     return  
        
         if self.body == 1:
            if self.snake.score <= 0:
                arcade.draw_text("Game Over :(", 230, 200, arcade.color.RED, 40)
                self.exit = 1

         if (600 <= self.snake.center_x + self.snake.r) or (0 >= self.snake.center_x - self.snake.r) or (400 <= self.snake.center_y + self.snake.r) or (0 >= self.snake.center_y - self.snake.r):
            arcade.draw_text("Game Over :(", 230, 200, arcade.color.RED, 40)
            self.exit = 1              

    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.flower):
            self.snake.eat("flower")
            self.flower = Flower(100,100)
            print(self.snake.score)
            
        elif arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat("apple")
            self.apple = Apple(100,100)
            print(self.snake.score)
           
        elif arcade.check_for_collision(self.snake, self.cactus):
            self.snake.eat("cactus")
            self.cactus = Cactus(100,50)
            print(self.snake.score)
        
        

    def on_key_release(self,key,nodifiers):
        if key==arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0

        elif key==arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
    
        elif key==arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1

        elif key==arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1

        else:
            print("Button that pressure is not defined!")
            
class Flower(arcade.Sprite):
    def __init__(self,w,h):
            arcade.Sprite.__init__(self)
            self.color=arcade.color.PINK
            self.width=16
            self.height=16
            self.center_x=random.randint(0, w)
            self.center_y=random.randint(0, h)
            self.r=8
           
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class Cactus(arcade.Sprite):   
    def __init__(self,w,h):
            arcade.Sprite.__init__(self)
            self.color=arcade.color.GREEN
            self.width=16
            self.height=16
            self.center_x=random.randint(0, w)
            self.center_y=random.randint(0, h)
            self.r=8
           
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)   



game=My_game_window()
arcade.run()