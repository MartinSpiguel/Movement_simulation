###############################
# Movimiento de una partícula #
###############################

import simplegui
from math import *

########################################
# Inicialización de variables globales #
########################################

# Tamaño de la ventana en la que vamos a graficar (en pixels)
WIDTH = 1000
HEIGHT = 500

# Radio del círculo con que vamos a representar a nuestra partícula
radio = 10

# Valor inicial de tiempo
time = 0.

# Paso o incremento temporal
dt = 0.01

# Variables cinemáticas y sus valores iniciales.
pos0x = 10.
posx = pos0x
vel0x = 100.
velx = vel0x
acc0 = 0
acc = acc0

#########################################
# A continuación se definen los eventos #
#########################################

# Aquí tenemos lo que se grafica
def draw(canvas): 
    
    # De esta forma uno puede introducir texto en la representación
    # gráfica, dando la posición, tamaño y color de dicho texto.
    canvas.draw_text("Este movimiento es un MRU", (20, 625), 20, "White")
    # Dibuja un segmento que une los dos puntos especificados, 
    # de ancho tres y de color gris
    canvas.draw_line((0,350),(WIDTH,350),3,"Grey")
    
    # Dibuja un círculo en la posición indicada por las 
    # coordenadas de la variable "pos"
    # De color azul, radio= valor de la variable "radio" y 
    # un borde de tamaño 2 y también de color azul
    canvas.draw_circle((posx,350),radio, 2,"Green","Violet")

# Aqui tenemos las instrucciones que se ejecutan en cada
# paso de la simulación
def tick():
    global time #si uno quiere modificar el valor de una variable global, debe incluir estas líneas.
    global posx
    global velx
    global inp
 
    time += dt #al valor de tiempo previo le suma "dt"
     
    # Actualización de la posición (aquí tenemos el cálculo
    # de la nueva posición basado en el valor previo de 
    # posición y en la forma en la que se está moviendo 
    # el objeto)
    posx = posx + velx * dt + 0.5 * acc * dt**2
   
    # Actualización de la velocidad 
    velx = velx + acc * dt
    
    # Imprime en pantalla los valores de las variables mencionadas.
    # print time,posx,velx
    
    #Actualizacion de la aceleración
    inp.set_text(acc)
    
# Aquí tenemos una acción de control para iniciar y frenar
#la simulación (más abajo incluimos un botón)
def start_stop():
    if timer.is_running():
        timer.stop()
    else:
        timer.start()
        
# Aquí tenemos una acción de control para reiniciar la 
# simulación (más abajo incluimos otro botón)
def restart():
    global posx
    global time
    global velx
    global acc
    posx = pos0x
    velx = vel0x
    acc = 0
    time = 0
    
def increase_acc():
    global acc
    global inp
    acc += 100
    inp.set_text(acc)

def decrease_acc():
    global acc
    global inp
    acc -= 100
    inp.set_text(acc)

def input_handeler(input_text):
    global acc
    global inp
    acc = int(inp.get_text())
    inp.set_text(acc)
    
#############################################
# Aquí tenemos los controles de los eventos #
#############################################

# Crea una ventana donde se realiza la representación gráfica
frame = simplegui.create_frame("Movimiento", WIDTH, HEIGHT)
frame.set_canvas_background('Black')

# Aquí tenemos los que se representan en esa ventana
frame.set_draw_handler(draw)
frame.add_button("START/STOP",start_stop)
frame.add_button("Reset",restart)
frame.add_label("---------------------------")
inp = frame.add_input("Handle acceleration", input_handeler, 50)
frame.add_button("+100",increase_acc)
frame.add_button("-100",decrease_acc)
inp.set_text(acc0)
# Crea un timer para la simulación
timer = simplegui.create_timer(1000*dt,tick)

# Abre la ventana
frame.start()