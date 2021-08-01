import turtle
shelly = turtle.Turtle()
shelly.shape('turtle')
colors = ['red', 'green', 'blue']
for i in range(3):
    shelly.color(colors[i])
    shelly.forward(175)
    print(colors[i])