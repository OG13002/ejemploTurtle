import turtle
import winsound
import random
ventana = turtle.Screen()
ventana.setup(0.6,0.4)
anchoJuego= ventana.canvwidth-40

ventana.title("Juego tenis con Turtle")
ventana.tracer(1)
class rectangulo():
    def __init__(self):
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
        if self.jugador.ycor() + 200 <= ventana.canvheight:
            self.jugador.fd(20)
    def baja(self):
        if self.jugador.ycor() - 200 >= -ventana.canvheight:
            self.jugador.bk(20)

jugador1 = rectangulo()
jugador1.color("blue")
jugador1.velocidad(0)
jugador1.avance(anchoJuego)

jugador2 = rectangulo()
jugador2.color("red")
jugador2.velocidad(0)
jugador2.avance(-anchoJuego)

pelota= turtle.Turtle()
pelota.speed(4)
pelota.color("red")
pelota.shape("circle")
pelota.shapesize(1)
angulo=45
avance=6
pelota.setheading(angulo)
pelota.penup()

score = turtle.Turtle()
score.write("jugardor 1: 0   jugador 2: 0 ", align="center", font=("courier",16,"bold"))
puntos=0
puntos2=0
gameOver = False
ventana.onkeypress(jugador1.sube, "Up")
ventana.onkeypress(jugador1.baja, "Down")
while not gameOver:
    if pelota.ycor() >= ventana.canvheight/2-10 or pelota.ycor()  <= -ventana.canvheight/2 +10:
        angulor=random.randint(-10,10)
        angulo*=-1
        angulo+=angulor
        pelota.setheading(angulo)
        if pelota.ycor()>0:
            pelota.sety(pelota.ycor() - avance - 5)
        else:
            pelota.sety(pelota.ycor() + avance + 5)


    if pelota.xcor() >=  anchoJuego-20 or pelota.xcor() <=  -anchoJuego+20:
        if jugador1.jugador.ycor()-50 <= pelota.ycor() <= jugador1.jugador.ycor()+50 or jugador2.jugador.ycor()-50 <= pelota.ycor() <= jugador2.jugador.ycor()+50:
            winsound.Beep(1000, 100)
        elif pelota.xcor()>0:
            puntos2 += 1
            str1 = "jugardor 1: "+str(puntos2)+"   jugador 2: " + str(puntos)
            score.clear()
            score.write(str1, align="center", font=("courier", 16, "bold"))
        else:
            puntos += 1
            str1 = "jugardor 1: "+str(puntos2)+"   jugador 2: " + str(puntos)
            score.clear()
            score.write(str1, align="center", font=("courier", 16, "bold"))
        if pelota.xcor()>0:
            pelota.setx(pelota.xcor() - avance - 5)
        else:
            pelota.setx(pelota.xcor() + avance + 5)
        angulor = random.randint(-15, 15)
        angulo = 180 - angulo
        angulo += angulor
        if -90<=angulo<=90:
            if angulo>60:
                pelota.setheading(60)
                angulo=60
            elif angulo<-60:
                pelota.setheading(-60)
                angulo = -60
            else:
                pelota.setheading(angulo)
        elif 90<=angulo<=270:
            if angulo<120:
                pelota.setheading(120)
                angulo=120
            elif angulo>270:
                pelota.setheading(270)
                angulo = 270
            else:
                pelota.setheading(angulo)
        else:
            pelota.setheading(angulo)

    if pelota.xcor() <= -anchoJuego+40:
        if jugador2.jugador.ycor()+50 < pelota.ycor():
            jugador2.sube()
        elif pelota.ycor() < jugador2.jugador.ycor()-50:
            jugador2.baja()
    try:
        pelota.forward(avance)
    except:
        gameOver = True
    try:
        ventana.listen()
    except:
        gameOver = True







#ventana.exitonclick()


