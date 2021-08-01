import turtle
shelly = turtle.Turtle()
shelly.shape('turtle') #Change the shape of the cursor from a triangle to a turtle; when you delete Line 3, the shape goes back to a triangle
shelly.forward(100)  # moves shelly forward 100 steps
shelly.right(90)  # turns shelly right 90 degrees
shelly.left(60)  # turns shelly left 60 degrees
shelly.backward(100)  # moves shelly backward 100 steps shelly.color('red')  
shelly.color('red')  # makes shelly draw in color red
shelly.circle(10)  # makes shelly draw a circle of size 10 shelly.penup()  
shelly.penup()# makes shelly lift pen
shelly.pendown() # makes shelly put the pen down to draw shelly.reset()  
shelly.reset() # clears screen and goes back to start position shelly.goto(35, 80)  
shelly.goto(35, 80) # move to x coordinate 35,y coordinate 80 shelly.hideturtle()  
shelly.hideturtle() # makes shelly invisible on the screen
print(shelly.xcor(), shelly.ycor()) #  Find out where you are by printing out the current coordinates (example 35 80).
input ("click anywhere on your code to exit") # You may have to enter the input on Line 13, otherwise the graphic may only appear for a few seconds













