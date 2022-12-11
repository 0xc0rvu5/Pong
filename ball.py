from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1


    def move(self):
        '''Ball movement functionality.'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        '''y axis bounce functionality.'''
        self.y_move *= -1


    def bounce_x(self):
        '''x axis bounce functionality.'''
        self.x_move *= -1
        self.move_speed *= .9


    def reset_position(self):
        '''Reset ball to center.'''
        self.goto(0, 0)
        self.move_speed = .1
        self.bounce_x()