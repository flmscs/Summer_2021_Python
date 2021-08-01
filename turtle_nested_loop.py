import turtle
shelly = turtle.Turtle()
shelly.shape('turtle')
shelly.begin_fill()  # start filling shape 
shelly.color('green')  # use color red
for n in range(10):# outer loop repeats the square 10 times 
    for i in range(4): # inner loop repeats 4 times to make a square
        shelly.forward(100)
        shelly.left(90)
    shelly.right(30) # add a 30 degree turn before the next square