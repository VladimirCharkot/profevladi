# Sistemas

Una de las aplicaciones de la programación que me trae mayor dicha es la de modelar aspectos del mundo e investigar qué me puede enseñar el modelo sobre el mundo.

Hay que saber que el modelo nunca va a ser exacto. Siempre es un recorte del mundo.
Hay un cuento de Borges que habla de un imperio donde el arte de la cartografía había alcanzado tal perfección que los mapas, para describir con exactitud el territorio que mapeaban, se habían vuelto tan grandes como el territorio mismo.

El mapa no es el territorio. Sin embargo el mapa puede colaborar mucho en investigar el territorio. Nos puede decir en qué dirección queda lo que estamos buscando. Lo que no pueden es ir a buscarlo por nosotros.

Los modelos son como mapas, nos permiten examinar algunas cosas sobre el mundo con las cuales _luego podemos acudir al mundo a investigar_. Nos marcan direcciones. No son el mundo.

---

## Predación

Veamos un modelo muy querido en el mundo de la computación. Es un modelo de predación, en el que hay lobos, liebres y pasto. Las liebres comen pasto y los lobos comen liebres. [Veamoslo funcionando...](https://turbowarp.org/632753209/fullscreen)

Este modelo explora la estabilidad de un ecosistema. Si alguna de las especies se extingue, decimos que el ecosistema es inestable. Si alcanzan un equilibrio que dura a través del tiempo, decimos que es estable.

Si las liebres abundan, los lobos comen bien y se reproducen. Pero a medida que crecen en número, empiezan a competir por la comida. La población de libres diezma y los lobos comienzan a morir de hambre. Con menos lobos, las liebres se reproducen más y el ciclo comienza a repetirse.

A nivel programación el modelo funciona así: los lobos y las liebres tienen una cantidad de energía que pierden a cada paso de la simulación. Cuando comen alguna de sus presas, ganan energía, y si superan una cierta cantidad, se reproducen, perdiendo mucha energía en el proceso. El pasto se reproduce solo. Si una criatura se queda sin energía, muere.

Este modelo que programé en scratch es prácticamente un juguete, pero pueden reinventarlo e intervenirlo. ¡Háganlo! Estaré feliz de ver y comentar los resultados.

En la dinámica de poblaciones, esto sucede: las poblaciones oscilan, las cantidades crecen y decrecen alternadamente. Veamos un modelo más elaborado en [NetLogo](http://netlogoweb.org/launch#http://netlogoweb.org/assets/modelslib/Sample%20Models/Biology/Wolf%20Sheep%20Predation.nlogo).


### Comentarios

Prueben distintos valores iniciales en Netlogo y vean cómo varía la evolución del sistema.

También hay una versión 3d muy buena hecha en Unity por Sebastian Lague

Para quienes aman la matemática pura y dura, está el modelo de Mike Bostock, que incluye las ecuaciones utilizadas para estudiar esto (con visuzalizaciones interactivas ¡yay!)

Links a todo esto en la sección de [recursos](#recursos)

---

## El juego de la vida

Existe un modelo de 1970 que dejó pasmada a la comunidad matemática. Se trata de el juego de la vida de Conway -que es el apellido del tipo que lo inventó-. Conway encontró inspiración en un modelo de otro tipo -von Neumann- que describía el comportamiento de fluídos como un montón de unidades discretas... o sea, como si fueran un montón de "gotitas" independiente, cuyo movimiento estaba gobernado por sus vecinas. Con esto en mente, se largó a intentar fabricar un modelo similar y que fuera impredecible e interesante.

Finalmente dió con un juego con estas características. El juego es así:

Existe un "mundo" que consiste en una grilla de celdas. Cada celda puede estar en uno de dos estados, o viva (negra) o muerta (blanca). En cada momento de la simulación, cada celda cuenta sus vecinas vivas y hace lo siguiente:
- Si está viva, y tiene dos o tres vecinas vivas, sigue viva
- Si está viva y tiene solo una vecina viva, muere, como si fuera por aislamiento
- Si está viva y tiene cuatro o más vecinas vivas, muere, como si fuera por sobrepoblación
- Si está muerta y tiene tres vecinas vivas, pasa a estar viva, como si fuera por reproducción

La simulación es tan solo la aplicación de estas reglas turno tras turno.

Lo notable es que de estas simples reglas _emergen_ patrones que se mueven a través de la grilla, y evolucionan de maneras sorprendentes. Patrones complejos, dinámicos, surgiendo de reglas simples.

Veamos mi propia [implementación](https://turbowarp.org/681243011?turbo) en scratch

---

## El mapa logístico

Nos damos cuenta que hemos dado con un buen modelo cuando podemos explicar varios fenómenos con el mismo fundamento. Esto pasó en el siglo XVII cuando Newton demostró que la ley que gobernaba el movimiento de caída libre de los objetos y las órbitas de los planetas eran los mismos.

Algo parecido sucede el mapa logístico. Es un modelo famoso por dos razones: provee una manera de predecir cómo va a evolucionar una población de animales en el tiempo, e ilustra el fenómeno del caos matemático.

Más adelante este fenómeno fue estudiado en las ciencias sociales, política y planeamiento urbano.

Un físico Australiano, pionero en la interdisciplina física-biología llamado Robert May, estudió este modelo no lineal buscando una manera sencilla de explicar la dinámica poblacional, y luego lo hizo famoso a través de un artículo publicado en una revista. Su objetivo al crear este modelo era que en principio la población en un instante podía predecirse a partir de la población en un instante previo al multiplicarla por una constante, pero que además tuviese en cuenta el hecho de que a medida que la población crece y se acerca a un valor considerado máximo, el valor de la población resulta cada vez menos alejado del valor previo. Esto reflejaría, por ejemplo, que para valores de la población muy grandes faltarán alimentos y las enfermedades se propagarán con más facilidad.

La **dinámica** de un sistema es el estudio de lo que le va pasando a medida que avanza el tiempo.

Bien, imaginemos que tenemos un acuario lo suficientemente grande como para contener 100 pececitos. La pregunta es, ¿cuántos pececitos podemos esperar tener el próximo mes si los dejamos procrear libremente? Bueno depende del tamaño del acuario, la comida que haya disponible, las otras criaturas que pudiera haber dando vueltas, etc...

---

## Cosas a intentar en Scratch ("ejercicios")
Reproducción de clones - Qué pasa cuando un clon crea otros clones? Cómo varía esto con diferentes cantidades de clones? Y con diferentes tiempos o ciclos de vida?
Darles conducta y hacer que les pase algo cuando interactúen

## Recursos
- [Modelo de libélulas y agua en Scratch](https://scratch.mit.edu/projects/498342889/)
- [Netlogo Web](http://netlogoweb.org/launch#http://netlogoweb.org/assets/modelslib/Sample%20Models/Biology/Wolf%20Sheep%20Predation.nlogo)
- [Netlogo Descarga](http://ccl.northwestern.edu/netlogo/)
- [Wolf-Sheep predation en 3d por Sebastian Lague](https://www.youtube.com/watch?v=r_It_X7v-1E)
- [Wolf-Sheep Mike Bostock, con visualización de ecuaciones](https://observablehq.com/@mbostock/predator-and-prey)
- [Buen simulador del Game of life](https://conwaylife.com/)
- [Game of life en Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Video de curva logística por Veritasium](https://www.youtube.com/watch?v=EOvLhZPevm0)
- [Ríos fractales en Scratch](https://scratch.mit.edu/projects/551161908/)
