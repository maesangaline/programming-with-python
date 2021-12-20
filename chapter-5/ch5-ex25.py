# Chapter 5
# Exercise 25

import turtle

# Named constants
ANIMATION_SPEED = 0
SCREEN_WIDTH = 500
SCREEN_HEIGHT = SCREEN_WIDTH
NUM_SQUARES_IN_A_ROW = 5
NUM_SQUARES_IN_A_COL = 5
SQUARE_WIDTH = int(SCREEN_WIDTH / NUM_SQUARES_IN_A_ROW)
SCREEN_LEFT_EDGE_X = int(-(SCREEN_WIDTH / 2))
SCREEN_TOP_EDGE_Y = int(SCREEN_HEIGHT / 2)
FIRST_X = SCREEN_LEFT_EDGE_X
LAST_X = FIRST_X + (NUM_SQUARES_IN_A_ROW * SQUARE_WIDTH)
FIRST_Y = SCREEN_TOP_EDGE_Y - SQUARE_WIDTH
LAST_Y = FIRST_Y - (NUM_SQUARES_IN_A_COL * SQUARE_WIDTH)


# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to the specified location
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling
    
# Main function that creates the squares using x, y, width and color
def main():
    square(0,0,50,'black')
    square(50,0,50,'white')
    square(100,0,50,'black')
    square(150,0,50,'white')
    square(200,0,50,'black')

    square(0,50,50,'white')
    square(50,50,50,'black')
    square(100,50,50,'white')
    square(150,50,50,'black')
    square(200,50,50,'white')

    square(0,100,50,'black')
    square(50,100,50,'white')
    square(100,100,50,'black')
    square(150,100,50,'white')
    square(200,100,50,'black')
    
    square(0,150,50,'white')
    square(50,150,50,'black')
    square(100,150,50,'white')
    square(150,150,50,'black')
    square(200,150,50,'white')
    
    square(0,200,50,'black')
    square(50,200,50,'white')
    square(100,200,50,'black')
    square(150,200,50,'white')
    square(200,200,50,'black')
    
main()
