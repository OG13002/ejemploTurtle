import turtle
import winsound
import random
import clases
ventana = turtle.Screen()
ventana.setup(0.6,0.4)
anchoJuego= ventana.canvwidth-40

ventana.title("Juego tenis con Turtle")
ventana.tracer(1)
jugador1 = clases.rectangulo((ventana.window_height()))
jugador1.color("blue")
jugador1.velocidad(0)
jugador1.avance(anchoJuego)

jugador2 = clases.rectangulo((ventana.window_height()))
jugador2.color("red")
jugador2.velocidad(0)
jugador2.avance(-anchoJuego)



pelota1 = clases.pelota()


score = turtle.Turtle()
score.write("jugardor 1: 0   jugador 2: 0 ", align="center", font=("courier",16,"bold"))
puntos=0
puntos2=0
gameOver = False
ventana.onkeypress(jugador1.sube, "Up")
ventana.onkeypress(jugador1.baja, "Down")
while not gameOver:
    if pelota1.ycoor() >= ventana.canvheight/2-10 or pelota1.ycoor()  <= -ventana.canvheight/2 +10:

        pelota1.rebote("vertical",0)

    if pelota1.xcoor() >=  anchoJuego-20 or pelota1.xcoor() <=  -anchoJuego+20:
        if jugador1.jugador.ycor()-50 <= pelota1.ycoor() <= jugador1.jugador.ycor()+50 or jugador2.jugador.ycor()-50 <= pelota1.ycoor() <= jugador2.jugador.ycor()+50:
            winsound.Beep(1000, 100)
        elif pelota1.xcoor()>0:
            puntos2 += 1
            str1 = "jugardor 1: "+str(puntos2)+"   jugador 2: " + str(puntos)
            score.clear()
            score.write(str1, align="center", font=("courier", 16, "bold"))
        else:
            puntos += 1
            str1 = "jugardor 1: "+str(puntos2)+"   jugador 2: " + str(puntos)
            score.clear()
            score.write(str1, align="center", font=("courier", 16, "bold"))
        pelota1.rebote("horizontal",0)


    if pelota1.xcoor() <= -anchoJuego+40:
        if jugador2.jugador.ycor()+50 < pelota1.ycoor():
            jugador2.sube()
        elif pelota1.ycoor() < jugador2.jugador.ycor()-50:
            jugador2.baja()
    try:
        pelota1.avanza(5)
    except:
        gameOver = True
    try:
        ventana.listen()
    except:
        gameOver = True





