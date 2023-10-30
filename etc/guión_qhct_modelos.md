# Modelos

## Rubik

El escultor y profesor de arquitectura húngaro Ernö Rubik construyó en 1974 el juguete más vendido del mundo. El cubo Rubik nos cautivó con su simultánea sencillez y complejidad.

El cubo tiene 43.252.003.274.489.856.000 estados posibles, y un estado "armado". Y mover una pieza cualquiera invariablemente mueve muchas otras más. Es difícil de armar.

Por lo que la mayoría de nosotros buscamos algún tutorial y aprendemos a armarlo.

Para transmitir la materia, se inventó un lenguaje, en el que se usan seis letras para representar los movimientos de las diferentes caras.

![](recursos/movimientos1.png)

![](recursos/movimientos2.png)

A una secuencia de esos movimientos se la llama "algoritmo", y nos lleva de un estado a otro, armando progresivamente, capa a capa, el cubo.

![](recursos/algunos_algoritmos.png)

A mí no me alcanza. ¿Cómo funciona? ¿Por qué? ¿Cómo haría yo para descubrirlo?

La esencia de un algoritmo (del cubo), me doy cuenta, es mover una cantidad de piezas manteniendo intactas otras. Si por ejemplo encuentro un algoritmo que me altere tan solo una cara del cubo, puedo usarlo para modificar las piezas de esa cara sin desarmar el resto, si ya lo tuviera armado. Todo algoritmo que modifique la posición de una cantidad de piezas produce una **permutación** entre ellas; es decir, intercambia las posiciones de estas entre sí.

Por ejemplo, al mover una sola cara, las piezas de uno de los bordes terminan en otro, y esas en el siguiente, y esas otras en donde se hallaban las primeras. Es como si en una ronda todxs nos pusiesemos de pie y nos cambiaramos a la silla a nuestra derecha... se produce un cambio en la disposición pero hay una estructura que se mantiene.

Bien, este es un punto clave: **toda permutación, si la repetimos una cantidad de veces, nos vuelve a dejar en donde empezamos**.

![](recursos/órbita.png)

Por lo que podemos afirmar que toda secuencia de movimientos en el cubo nos produce una **órbita** de estados. Agarrá los movimientos que quieras, repetilos, y evntualmente vas a volver al principio.

Investigando estas órbitas podemos encontrar los algoritmos que nos desplazan entre estados que reconozcamos, y hacernos un "mapa" de los lugares por los que los algoritmos nos van llevando.


## Modelando con código

_Nota: podés saltearte esta sección si no estás muy afinadx al código fuente_

Para estudiar estas órbitas sin tener que pelarnos los dedos cubeando y anotando, desarrollémonos una herramienta en javascript. Vamos a usar p5, una biblioteca para dibujar en canvas, inspirada en processing, que ofrece [un editor](https://editor.p5js.org/) en su sitio web.

Para modelar esta situación vamos a representar el cubo como una secuencia de letras. Cada posición en la secuencia va a representar una carita del cubo, y la letra en esa posición va a representar el color de esa carita.

Las 9 primeras posiciones van a representar la cara de arriba. Las 9 que siguen, la cara de la izquierda. Las 9 que siguen, la cara de adelante, y así con el resto... la cara de la derecha, de atrás y de abajo.

El cubo armado, con la cara blanca arriba, la amarilla abajo y la roja adelante, se vería así (z es azul):

`bbbbbbbbbvvvvvvvvvrrrrrrrrrzzzzzzzzznnnnnnnnnaaaaaaaaa`

Y luego vamos a representar los movimientos que apliquemos sobre el cubo como funciones que reciben este texto y lo devuelven con las piezas que correspondan intercambiadas de lugar.

En esencia, el modelado es ese. El resto es código.

Girar una cara consta de recibir las 9 letras correspondiente a una cara y devolver en otro orden:

```js
const rotar_reloj = (cara) =>
  cara[6] + cara[3] + cara[0] +
  cara[7] + cara[4] + cara[1] +
  cara[8] + cara[5] + cara[2]
```

Girar los bordes de esa cara es un poco más complicado. Al girar la cara de arriba, por ejemplo, hay que mandar las posiciones 18, 19 y 20 de nuestra cadena de caracteres a las posiciones 9, 10, 11. Estas últimas tienen que ir a la posición 36, 37 y 38; esas a las 27, 28 y 29 y esas a donde se encontraban las primeras... 18, 19 y 20.

¿Qué cómo obtuve esos numeritos? En verdad, primero escribí la función que dibuja el cubo -desplegado, para visualizarlo en 2d- con los números sobre cada carita.

Para el resto de las caras el proceso va a ser similar... vamos a rotar una cara y luego "ciclar" los cuatro grupos de tres piezas que correspondan a sus bordes.

Vamos a escribirnos una función que reciba estos cuatro grupos de tres piezas y los intercambie entre sí:

```js
// bordes sería por ejemplo:
// [[18,19,20], [9,10,11], [36,37,38], [27,28,29]]

const ciclar = (bordes) => (cubo) => {
  let ncubo = cubo
  const [b1, b2, b3, b4] = bordes;
  for(let i = 0; i < 3; i++){
    ncubo = ciclar4(b1[i], b2[i], b3[i], b4[i])(ncubo);
  }
}

const ciclar4 = (p1,p2,p3,p4) => (cubo) => swap(p1, p4)(swap(p1, p3)(swap(p1, p2)(cubo)));

const swap = (p1, p2) => (cubo) => {
  const a = min(p1, p2);
  const b = max(p1, p2);
  return cubo.slice(0, a) + cubo[b] + cubo.slice(a+1, b) + cubo[a] + cubo.slice(b + 1, cubo.length);
}
```

Tenemos tres funciones: `swap`, que intercambia dos posiciones entre sí, `ciclar4`, que usa a swap para ciclar 4 posiciones entre sí, y `ciclar`, que usa a `ciclar4` para intercambiar todos los bordes.

Si por ejemplo `ciclar` recibe `[[18,19,20], [9,10,11], [36,37,38], [27,28,29]]`, va a ciclar 18, 9, 36 y 27 entre sí, luego 19, 10, 27 y 28 entre sí, y por último 20, 11, 38 y 29 entre sí.

Combinando `ciclar` y `rotar_reloj`, podemos representar los movimientos básicos de las 6 caras del cubo. Todos los demás son secuencias de estos.

Agregamos algunas funciones para dibujar el cubo a partir de la cadena de caracteres, y tenemos una herramienta decente.

Ahora la otra función clave, `orbitar`: una función que reciba una transformación y la repita hasta regresar al estado inicial, devolviendo toda la cadena de estados intermedios. Es una deliciosa función recursiva.

```js
const orbitar = (transf) => (cubo) => {
  const inicial = cubo;
  const recurse = (estado) =>
    transf(estado) == inicial ?
    [estado] :
    [estado].concat(recurse(transf(estado)));
  return recurse(cubo);
}
```

[Accedé al código entero acá](https://editor.p5js.org/vlad.chk/sketches/8ju2Uocei) (apretá la flechita encima de los números de línea para ver todos los archivos del proyecto)

Este proyecto está en desarrollo. Puede crecer mucho más. A continuación crearíamos una función `mapear`, que tome un algoritmo, genere sus "espejos" y los aplique sucesivamente, para alcanzar a ver todos los estados a los que se puede llegar mediante un solo algoritmo.

## Teoría de Grupos

Ya, ¿de qué se trata todo esto?

Existe un -fascinante- campo de la matemática que estudia la simetría. Si las acciones que se pueden efectuar sobre ciertas estructuras -como el cubo rubik- exhiben ciertas propiedades, se dice que el conjunto -la estructura junto a las operaciones- forman un _grupo_. A partir de ahí se puede estudiar con las herramientas de esta teoría.

Para ilustrar de qué se trata, voy a tomar algunas animaciones de Grant Sanderson, de [3blue1brown](https://www.youtube.com/watch?v=mH0oCDa74tE).

![](recursos/simetría_copo.gif)

Tomemos una figura con simetría sextil (un copo de nieve) y definamos algunas operaciones... podemos rotarla cualquier múltiplo de 60 grados o voltearla a lo largo de la recta que se forma entre dos vértices.

![](recursos/simetrías_copo.gif)

La teoría de grupos nos propone considerar qué sucede cuando aplicamos operaciones sucesivas, y cómo la composiciones de operaciones se comparan entre sí.

Por ejemplo, en el copo, voltear sobre la horizontal y rotar 60 grados en el sentido antihorario produce el mismo efecto que voltear sobre una de las diagonales.

También, los resultados de operaciones que definimos caen siempre dentro de nuestra estructura... no estamos admitiendo por ejemplo la operación de partir el copo a la mitad, por ejemplo.

Esto se llama clausura... si consideramos los números enteros con la suma y la multiplicación, este es un grupo con clausura: siempre produce otro entero. Si consideramos en cambio también la división, la clausura se rompe, porque 4 dividido 3, por ejemplo, nos produce algo que no es un entero.

Esta cosa tan aparentemente irrelevante es muy potente en el mundo de la computación, donde las excepciones tienen una relación tan estrecha con los errores. Saber que una transformación produce o no una clausura sobre un conjunto puede orientar el desarrollo de un sistema.

Bien.

La potencia de la teoría viene con su movimiento de abstracción: para diversas estructuras y operaciones pueden resultar tablas de operaciones exactamente iguales. La teoría de grupos estudia estas estructuras en su nivel abstracto, de la misma manera que estudiamos los números mediante los símbolos, independientemente de las cantidades que están respresentando.

Veamos por ejemplo la tabla de composición del grupo del cuadrado con las operaciones que vimos antes (rotación y reflexión):

![](recursos/composicion_cuadrado.gif)

![](recursos/Simetrías_cuadrado.png)

En cada celda tenemos la operación equivalente a realizar la operación de arriba seguida de la operación de la derecha. Si el orden es indiferente (como en este caso), el grupo es conmutativo y se pueden afirmar ciertas otras propiedades.

Finalmente, la tabla queda abstraída cuando se traduce todo a símbolos:

![](recursos/abstracción.gif)

Luego, cualquier otro grupo que presente la misma estructura se dice que es un **isomorfismo** de este (quiere decir "misma-forma").

Los grupos isomórficos entre sí comparten las mismas propiedades estructurales.

![](recursos/Isomorfismo.png)

```
Para ponderar:
¿Es conmutativo el cubo rubik?
¿Qué relación podría existir entre los grupos y los atractores?
```

---

Si querés checkear el video original del que tomé estas capturas, es [este](https://www.youtube.com/watch?v=mH0oCDa74tE)

El script del cubo Rubik se encuentra [acá](https://editor.p5js.org/vlad.chk/sketches/8ju2Uocei), y podés llegar a encontrarlo algo cambiado de lo que expuse acá dado que sigue en desarrollo.

Cualquier aporte, comentario o pregunta es bienvenido. Encontrame en nuestro [servidor de Discord](https://discord.gg/948GcGFDGj) o mandame un mail a ![](recursos/mail.png)

[Acá](https://youtu.be/KTnRcb9UIsE) tenés el videotutorial para armar el cubo que hice en 2020 para un colegio primario en el que trabajé
