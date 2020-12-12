import turtle
import random

class rectangulo():
    def __init__(self,h):
        self.h=h
        self.jugador= turtle.Turtle()
        self.jugador.shape("square")
        self.jugador.penup()
        self.jugador.shapesize(1,5)
    def velocidad(self,v=0):
        self.jugador.speed(v)
    def avance(self,avz):
        self.jugador.fd(avz)
        self.jugador.setheading(90)
    def color(self,c="blue"):
        self.jugador.color(c)
    def sube(self):
        if self.jugador.ycor() + 200 <= self.h:
            self.jugador.fd(20)
    def baja(self):
        if self.jugador.ycor() - 200 >= -self.h:
            self.jugador.bk(20)


class pelota():
    def __init__(self):
        self.pelota = turtle.Turtle()
        self.pelota.color("#"+str(hex(random.randint(1048576,16777215))).replace("0x",""))
        self.pelota.shape("circle")
        self.pelota.penup()
        self.pelota.shapesize(1)
        self.angulo=45
        self.pelota.setheading(self.angulo)
    def avanza(self,avnz):
        self.pelota.forward(avnz)
        self.avnz=avnz
    def angulor(self,angulo1):
        if -90 + angulo1 <= self.angulo <= 90 + angulo1:
            if self.angulo > 60 + angulo1:
                self.pelota.setheading(60 + angulo1)
                self.angulo = 60 + angulo1
            elif self.angulo < -60 + angulo1:
                self.pelota.setheading(-60 + angulo1)
                self.angulo = -60 + angulo1
            else:
                self.pelota.setheading(self.angulo)
        elif 90 + angulo1 <= self.angulo <= 270 + angulo1:
            if self.angulo < 120 + angulo1:
                self.pelota.setheading(120 + angulo1)
                self.angulo = 120 + angulo1
            elif self.angulo > 270 + angulo1:
                self.pelota.setheading(240 + angulo1)
                self.angulo = 240 + angulo1
            else:
                self.pelota.setheading(self.angulo)
        else:
            self.pelota.setheading(self.angulo)
        if self.angulo > 360:
            self.angulo -= 360

    def rebote(self,str1,angulo1=0):
        if str1=="vertical":
            self.angulo *= -1
            self.angulo +=  random.randint(-15, 15)
            self.pelota.setheading(self.angulo)
            if self.pelota.ycor() > 0:
                self.pelota.sety(self.pelota.ycor() - self.avnz - 5)
            else:
                self.pelota.sety(self.pelota.ycor() + self.avnz + 5)
            self.angulor(angulo1)
        else:
            if self.pelota.xcor() > 0:
                self.pelota.setx(self.pelota.xcor() - self.avnz - 5)
            else:
                self.pelota.setx(self.pelota.xcor() + self.avnz + 5)
            self.angulo = 180 - self.angulo
            self.angulo += random.randint(-15, 15)
            self.angulor(angulo1)
    def xcoor(self):
        return self.pelota.xcor()
    def ycoor(self):
        return self.pelota.ycor()
