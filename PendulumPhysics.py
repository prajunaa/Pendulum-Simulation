from vpython import sphere,rate,vector,cylinder,color
from math import cos,sin
import math

#Constants and Initial Positions are recorded here to place into our equations. Theta must be in radians.

theta = math.radians(60) # initial angle, CHANGEABLE
lineLength = 10 # length of the rope, CHANGEABLE
g = 9.8 # gravitational constant
angularVel = 0 # initial angular velocity from which its released with, CHANGEABLE
deltaTime = 0.01 # The change of time for each frame of the simulation, 0.01 since we have 100 FPS

# Creating the initial rope and mass objects, 
# I also make sure to adjust the size of the string based on the length to maintain visibility
s = sphere(
    radius=lineLength/20,
    color=color.cyan
)

string = cylinder(
    radius=lineLength/100,
    length=lineLength,
    axis=vector(0,-1,0),
    color=color.white
)

# creating the stand , this isn't important, just cosmetic

standNeck = cylinder(
    radius=lineLength/70,
    length=(12*lineLength/10),
    axis=vector(0,-1,0),
    pos=vector(0,0,-0.2)
)

standArm = cylinder(
    radius=lineLength/70,
    length=0.2,
    axis=vector(0,0,1),
    pos=vector(0,0,-0.2)
)

standBaseLeft = cylinder(
    radius=lineLength/70,
    length=lineLength/4,
    axis=vector(-1,0,0),
    pos=vector(0,-(12*lineLength/10),-0.2)
)

standBaseRight = cylinder(
    radius=lineLength/70,
    length=lineLength/4,
    axis=vector(1,0,0),
    pos=vector(0,-(12*lineLength/10),-0.2)
)

# Creating the origin of the string where the string is gonna hang from
origin = vector(0,0,0)

#I put it in a "While" loop in order to make it repeat the movement infinitely rather than stop.
while(True):
    # the rate() function tells the program how many times can the ball 
    # move in a second, equivalent to that of 100 frames per second.
    rate(100)
    
    # Angular Acceleration is calculated using -(gravity/length) * sin(theta)
    angularAccel = - (g / lineLength) * sin(theta)

    # Angular Velocity was calculated using angular velocity = angular velocity (initial) + angular acceleration * delta time
    angularVel += angularAccel * deltaTime

    # The current theta after a bit of time is found with theta = theta (initial) + angular velocity * delta time + (angular accel)/2 * time^2
    theta += angularVel * deltaTime + 1/2 * angularAccel * deltaTime**2

    # I am using circleX and circleY as reference for the x and y positions of the ball so that I can relocate the sphere to the
    # new spot based on how much time has passed.
    circleX = lineLength * sin(theta)
    circleY = -lineLength * cos(theta)
    s.pos = vector(circleX,circleY,0)

    # I am assigning the origin of the string to the center, and making the angle match that of 
    # the sphere by matching the axis the position of the sphere minus the origin.
    string.pos = origin
    string.axis = s.pos - origin
