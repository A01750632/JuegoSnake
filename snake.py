"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""
# Código modificado
# Autor: Daniela Avila Luna
# Autor: Liam Garay Monroy

from turtle import *
from random import randrange, sample, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Cambia la dirección de la serpiente dependiendo de las coordenadas

    Args:
        x ([int]): [dirección que tomara la serpiente en x]
        y ([int]): [dirección que tomara la serpiente en y]
    """
    aim.x = x
    aim.y = y


def inside(head):
    """Recibe un vector y regresa un bool dependiendo de si esta en el rango

    Args:
        head ([vector]): [coordenadas]

    Returns:
        [bool]: [Regresa si true si el ambas partes de el vector
        correspondientes]
    """
    return -200 < head.x < 190 and -200 < head.y < 190


colors = sample(["black", "green", "yellow", "purple", "blue"], 2)
serpiente = colors[0]
comida = colors[1]


def move():
    """Cambia la dirección de la cabeza de la serpiente
    Si la cabeza llega a alguno de los límites de la pantalla,
    entonces será el fin del juego.
    Cuando las coordenadas de la cabeza y la de la comida coincidan,
    se incrementará el score del jugador y crecerá la lista del cuerpo.
    La comida se mueve constantemente de manera aleatoria sin
    salirse del borde.
    """
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, serpiente)

    food.move(vector(choice([-10, 0, 10]), choice([-10, 0, 10])))

    if not inside(food):        # Si la comida llega a los bordes de la ventana
        food.x, food.y = 0, 0  # Manda la comida al centro de la ventana.

    square(food.x, food.y, 9, comida)   # Pinta la nueva posición de la comida
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Al presionar algunas de las flechas, moverá a la serpiente en esa dirección.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
