import time
import random
import arcade

height = 500
width = 500

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'apple-emoji-android-granny-smith-manzana-verde-green-apple.jpg'
        self.apple = arcade.Sprite(self.image, 0.1)
        self.apple.center_x = random.randint(25, w + 5)
        self.apple.center_y = random.randint(25, h + 5)
        
    def draw(self):
        self.apple.draw()
       
class Flower(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'R.jpg'
        self.flower = arcade.Sprite(self.image, 0.1)
        self.flower.center_x = random.randint(25, w + 5)
        self.flower.center_y = random.randint(25, h + 5)
        
    def draw(self):
        self.flower.draw()

class Cactus(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'R (1).jpg'
        self.cactus = arcade.Sprite(self.image, 0.1)
        self.cactus.center_x = random.randint(25, w + 5)
        self.cactus.center_y = random.randint(25, h + 5)
        
    def draw(self):
        self.cactus.draw()

class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color2=arcade.color.BLUE
        self.color3=arcade.color.YELLOW
        self.color1=arcade.color.MAGENTA
        self.speed = 1
        self.width = 16
        self.height = 16
        self.center_x = w // 2
        self.center_y = h // 2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body = []
        self.body.append([self.center_x, self.center_y])
        
    def draw(self):
        for i in range(len(self.body)):
            if i == 0:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, self.color2)
            else:
                arcade.draw_circle_outline(self.body[i][0], self.body[i][1], self.r, self.color3)
            arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color1)

    def move(self, appleX, appleY):
        self.change_x = 0
        self.change_y = 0
        
        if self.center_x > appleX:
            self.change_x = -1
        if self.center_x < appleX:
            self.change_x = 1        
        if self.center_x == appleX:
            self.change_x = 0
            if self.center_y > appleY:
                self.change_y = -1
            if self.center_y < appleY:
                self.change_y = 1
            if self.center_y == appleY:
                self.change_y = 0
        
        for i in range(len(self.body)-1, 0, -1):
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]
                
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        
        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y

    def eat(self, mode):
        if mode == 0: 
            self.score += 1
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
        
        elif mode == 1: 
            self.score -= 1
            self.body.pop()
            
        elif mode == 2: 
            self.score += 2
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
    
class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, width, height, "Snake Game")
        arcade.set_background_color(arcade.color.BLACK)
        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.cactus = Cactus(width, height)
        self.flower = Flower(width, height)
        
    def on_draw(self):
        arcade.start_render()
        if self.lose():
            arcade.set_background_color(arcade.color.RED)
            arcade.draw_text('Game Over', 160, 250, arcade.color.WHITE, 20, 20)
            time.sleep(5)
            return
        self.snake.draw()
        self.apple.draw()
        self.flower.draw()
        self.cactus.draw()
        # arcade.draw_text('SCORE : ', 50, height - 25, arcade.color.BLACK)
        # arcade.draw_text(str(self.snake.score), 100, height - 25, arcade.color.BLACK, italic=True)


        arcade.draw_text(text=f'Score: {self.snake.score}',start_x=0,start_y=460,width=500, font_size=20, align="center", color=arcade.color.WHITE)



            
    def on_update(self, delta_time: float):
      
        self.snake.move(self.flower.flower.center_x, self.flower.flower.center_y)
        if arcade.check_for_collision(self.apple.apple, self.snake): 
            self.snake.eat(0)
            self.apple = Apple(width, height)
            
        if arcade.check_for_collision(self.cactus.cactus, self.snake): 
            self.snake.eat(1)
            self.pooneh = Cactus(width, height)
            
        if arcade.check_for_collision(self.flower.flower, self.snake): 
            self.snake.eat(2)
            self.pear = Flower(width,height) 

    def lose(self):
        if self.snake.center_x>=490 or self.snake.center_x<=10 or self.snake.center_y>=490 or self.snake.center_y<=10 or self.snake.score<0:
            return True
        else:
            return False        
        
# if __name__ == '__main__':
game = Game()
arcade.run()