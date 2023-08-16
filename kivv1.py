from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import  NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Paddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self,ball):#here self refers to the paddle
        if self.collide_widget(ball):#this function checks whether the self collide with the ball objest
            ball.velocity_x *= -1#if collide change direction


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    #new pos = current velocity(with direction) + current position
    def move(self):
        #to find the current position after the movement of the ball
        self.pos = Vector(*self.velocity)+self.pos

#update
class PongGame(Widget):

    ball = ObjectProperty(None)
    player1=ObjectProperty(None)
    player2 = ObjectProperty(None)
    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    #this update function used whenver you want to check something evry sec
    def update(self,dt):
        self.ball.move()
        #to make the ball bounce and no to go out of the window
        #top and bottom
        if(self.ball.y<0) or (self.ball.y>self.height-50):#-50 because the ball size is 50 which counts from left of the ball
            self.ball.velocity_y*=-1 #by multiplying it by -1 the velocity vector direction changes

        #bounce of left
        if(self.ball.x<0):
            self.ball.velocity_x*=-1
            self.player1.score+=1
        if(self.ball.x > self.width - 50):
            self.ball.velocity_x *= -1
            self.player2.score+=1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if(touch.x<self.width/1/4):
            self.player1.center_y=touch.y
        if(touch.x>self.width*3/4):
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game=PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)#evry 1 sec we are calling the update function 60times
        return game

PongApp().run()



# in a rectangle to make sure the ball pos does not go abv this limit
# top left=(0,0)
# top right=(0,self.width)
# bottom_left=(self.height,0)
# bottom_right=(self.height,self.width)

# on_touch_down()-when our fingers/mouse touches the screen
# on_touch_up()-when we lift our finger off the screen after touching it
# on_touch_move()-when we drag our finger on the screen