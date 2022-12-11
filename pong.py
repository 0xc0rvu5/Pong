import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


#initialize screen and create game window prior to additional global variables for rendering purposes.
SCREEN = Screen()


#create game window
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor('black')
SCREEN.title('Pong')
SCREEN.tracer(0)


#initialize additional global variables
BALL = Ball()
L_PADDLE = Paddle((-350, 0))
PLAY = True
R_PADDLE = Paddle((350, 0))
SCOREBOARD = Scoreboard()


#connect keyboard strokes to pong movements
SCREEN.listen()
SCREEN.onkey(L_PADDLE.go_up, 'w')
SCREEN.onkey(L_PADDLE.go_down, 's')
SCREEN.onkey(R_PADDLE.go_up, 'Up')
SCREEN.onkey(R_PADDLE.go_down, 'Down')


#initiate game loop
try:
    while PLAY:
        time.sleep(BALL.move_speed)
        SCREEN.update()
        BALL.move()

        #detect collision with wall
        if BALL.ycor() > 280 or BALL.ycor() < -280:
            BALL.bounce_y()

        #detect collision with paddle
        if BALL.distance(R_PADDLE) < 50 and BALL.xcor() > 320 or BALL.distance(L_PADDLE) < 50 and BALL.xcor() < -320:
            BALL.bounce_x()

        #detect when r paddle misses
        if BALL.xcor() > 380:
            BALL.reset_position()
            SCOREBOARD.l_point()

        #detect when l paddle misses
        if BALL.xcor() < - 380:
            BALL.reset_position()
            SCOREBOARD.r_point()

except KeyboardInterrupt:
    print('\nSee you later.')
    
SCREEN.exitonclick()