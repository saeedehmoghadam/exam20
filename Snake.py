import time
import random
import arcade

height = 800
width = 600

class Apple(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=10
        self.center_x=random.randint(40,460)
        self.center_y=random.randint(40,460)
        self.color=arcade.color.RED
        self.width=20
        self.height=20
    def show(self):
       arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)
       
class Flower(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=10
        self.center_x=random.randint(40,460)
        self.center_y=random.randint(40,460)
        self.color=arcade.color.PINK
        self.height=20
        self.width=20
    def show(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)

class Cactus(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.r=10
        self.center_x=random.randint(40,460)
        self.center_y=random.randint(40,460)
        self.color=arcade.color.GREEN
        self.height=20
        self.width=20
    def show(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)

class Snake(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.center_x=250
        self.center_y=250
        self.color2=arcade.color.RED
        self.color3=arcade.color.GREEN
        self.color1=arcade.color.BLUE
        self.x_change=0
        self.y_change=0
        self.width=16
        self.height=16
        self.score=0
        self.r=10
        self.speed=2
        self.body=[]
    
    def show(self):
        i=0
        for b in self.body:
            i+=1
            if i%2==0:
                arcade.draw_circle_filled(b['x'],b['y'],self.r,self.color2)
            else:
                arcade.draw_circle_filled(b['x'],b['y'],self.r,self.color3)
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color1)

    def on_update(self, delta_time: float = 1/40):
        self.body.append({'x':self.center_x,'y':self.center_y})
        if len(self.body)>self.score:
            self.body.remove(self.body[0])
        # if self.x_change==-1:
        #     self.center_x-=self.speed
        # elif self.x_change==1:
        #     self.center_x+=self.speed
        # elif self.y_change==-1:
        #     self.center_y-=self.speed
        # elif self.y_change==1:
        #     self.center_y+=self.speed
        self.center_x += self.speed * self.x_change
        self.center_y += self.speed * self.y_change
    
class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 500, 500, 'Super Snake')
        arcade.set_background_color(arcade.color.BLACK)
        self.snake=Snake()
        self.apple=Apple()
        self.flower=Flower()
        self.cactus=Cactus()

    def on_draw(self):
        arcade.start_render()
        if self.GameOver():
            arcade.set_background_color(arcade.color.PINK)
            arcade.draw_text('Game Over :(', 160, 250, arcade.color.BLACK, 20)
            time.sleep(5)
            return
        self.snake.show()
        self.apple.show()
        self.flower.show()
        self.cactus.show()
        arcade.draw_text(text=f'Score: {self.snake.score}',start_x=0,start_y=460,width=500, font_size=20, color=arcade.color.WHITE)


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.snake.x_change= -1
            self.snake.y_change= 0
    
        elif key == arcade.key.RIGHT:
            self.snake.x_change = 1
            self.snake.y_change = 0

        elif key == arcade.key.UP:
            self.snake.x_change = 0
            self.snake.y_change = 1
    
        elif key == arcade.key.DOWN:
            self.snake.x_change = 0
            self.snake.y_change = -1

    def on_update(self,delta_time: float):
        self.apple.on_update()
        self.flower.on_update()
        self.cactus.on_update()
        self.snake.on_update(delta_time)
        
        if arcade.check_for_collision(self.snake,self.apple):
            self.apple=Apple()
            self.snake.score+=1

        if arcade.check_for_collision(self.snake,self.flower):
            self.flower=Flower()
            self.snake.score+=2

        if arcade.check_for_collision(self.snake,self.cactus):
            self.cactus=Cactus()
            self.snake.score -=1
            
        
    def GameOver(self):
        if self.snake.center_x>=490 or self.snake.center_x<=10 or self.snake.center_y>=490 or self.snake.center_y<=10 or self.snake.score<0:
            return True
        else:
            return False
        
window = Game()
arcade.run()