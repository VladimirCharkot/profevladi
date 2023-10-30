let t
let acc
let pelotas
let cabecita
let malabarista

function preload() {
  cabecita = loadImage('img/cabecita.png');
}

function setup() {
  createCanvas(400, 400)


  acc = createVector(0,0.1)
  pelotas = [new Pelota(createVector(300,300), 'red'),
             new Pelota(createVector(100,150), 'green'),
             new Pelota(createVector(300,300), 'blue')]

  malabarista = new Malabarista(cabecita, pelotas);


  malabarista.derecha.disparar([createVector(1,-6), createVector(1,-5)])
  malabarista.izquierda.disparar([createVector(-0.6,-8)])
  setTimeout(() => malabarista.izquierda.disparar([createVector(-2,-3)]), 3000)
  setTimeout(() => malabarista.derecha.disparar([createVector(1,-6)]), 4000)
}


function draw() {
  background(220)

  // malabarista.derecha.disparar(createVector(1,-4));
  malabarista.malabarear();


}
