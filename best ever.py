#exploring colormode using loop variable
import turtle
from myfunctionfile import*
jay=turtle.Turtle()
jay.speed(11)
turtle.colormode(255)
turtle.bgcolor("blue")


for times in range(244):
   c =(183,24,233)
   jay.circle(255-times)
   jay.forward(55)
   jay.right(45)
for times in range(256):
    jay.color(c)
    polygon(jay,1,1-times)
    jay.forward(55)
    jay.right(45)


  
   


   

  
