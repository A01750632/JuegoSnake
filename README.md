# JuegoSnake
Repositorio de la SemanaTec para el programa de snake.

Iniciamos con el código base de Snake que incluía:

* Cambiar la dirección de la serpiente
* Revisar si está dentro de los límites de la ventana
* Mover la serpiente con las flechas del teclado

Agregamos:

* Liam Garay Monroy:  Colores aleatorios para la serpiente y la comida

```python
colors = sample(["black", "green", "yellow", "purple", "blue"], 2)
serpiente = colors[0]
comida = colors[1]

    for body in snake:
        square(body.x, body.y, 9, serpiente)
    
    square(food.x, food.y, 9, comida)   # Pinta la nueva posición de la comida

```


* Daniela Avila Luna: Movimiento aleatorio de la comida sin salirse de la pantalla

```python
 food.move(vector(choice([-10, 0, 10]), choice([-10, 0, 10])))

    if not inside(food):        # Si la comida llega a los bordes de la ventana
        food.x, food.y = 0, 0  # Manda la comida al centro de la ventana.```



