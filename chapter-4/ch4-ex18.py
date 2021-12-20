# Chapter 4
# Exercise 18

# Imports that turtle graphic
import turtle

# Sets move to 10  and the turtle head to 90 degrees
move = 10
turtle.setheading(90)

# For loop to move turtle to the 11th loop
for x in range(11):
# For loop that moves turtle in forward then left 4 times before repeating
    for y in range(4):
        turtle.forward(move)
        turtle.left(90)
        move += 10

