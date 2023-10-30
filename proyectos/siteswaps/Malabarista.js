const linep = (p1, p2) => line(p1.x, p1.y, p2.x, p2.y)
const sumvec = (v1, v2) => p5.Vector.add(v1,v2)
const subvec = (v1, v2) => p5.Vector.sub(v1,v2)

class Mano{
  constructor(pos){
    this.pelotas = []    // pelotas sujetas por la mano
    this.pos_fija = pos
    this.pos = pos.copy()
    this.alcance = 40
    this.agarre = 8
    this.velmax = 0.25   // factor
    this.activa = false
  }

  dibujar_alcance(){
    if(this.activa){
      fill(255,100)
    }else{
      noFill()
    }
    circle(this.pos.x, this.pos.y, this.alcance * 2)
  }

  alcanza(pelota){
    const dv = p5.Vector.sub(pelota.pos, this.pos);

    const alcanza = dv.mag() < this.alcance;
    this.activa = alcanza
    return alcanza
  }

  intentar_agarrar(pelota){
    this.acercarce_a(pelota.pos)

    if (this.distancia_a(pelota.pos).mag() < this.agarre){
      this.agarrar(pelota)
    }
  }

  agarrar(pelota){
    this.pelotas.push(pelota)
    pelota.sujetar(this)
    this.activa = false
  }

  disparar(vs){

    if(this.pelotas.length >= vs.length){
      vs.forEach(v => {
        let p = this.pelotas.pop()
        p.disparar(v)
      })
    }else{
      console.log('Mano vacía!')
    }
  }

  tomar(pelota){
    this.pelotas.push(pelota)
    pelota.sujetar(this)
  }

  volver(){
    this.acercarce_a(this.pos_fija);
  }

  acercarce_a(v){
    const dp = p5.Vector.sub(v, this.pos)
    dp.setMag(this.velmax * dp.mag())
    this.pos = p5.Vector.add(this.pos, dp);
  }

  distancia_a(v){
    return p5.Vector.sub(v, this.pos)
  }
}



class Malabarista{
  constructor(cabecita, pelotas){

    this.cabecita = cabecita

    // Cabecita
    this.pc = createVector(width/2, 300)

    // Hombros
    this.ph = p5.Vector.add(this.pc, createVector(0, 20))

    // Codos
    this.ci = p5.Vector.add(this.ph, createVector(20, 30))
    this.cd = p5.Vector.add(this.ph, createVector(-20, 30))

    // Manos
    this.mi = p5.Vector.add(this.ci, createVector(30, 30)) // this.izquierda.pos
    this.md = p5.Vector.add(this.cd, createVector(-30, 30))

    this.izquierda = new Mano(this.mi)
    this.derecha = new Mano(this.md)

    this.pelotas = pelotas
    this.tomar_pelotas()
    this.debug()
  }

  debug(){
    console.log('Izquierda')
    console.log(this.izquierda)
    console.log(this.izquierda.pelotas.slice(0, this.izquierda.pelotas.length))
    console.log('Derecha')
    console.log(this.derecha)
    console.log(this.derecha.pelotas.slice(0, this.derecha.pelotas.length))
    console.log(this);
  }

  tomar_pelotas(){
    let alternar = false

    for(const pelota of this.pelotas){
      if(alternar){
        this.izquierda.tomar(pelota)
      }else{
        this.derecha.tomar(pelota)
      }
      alternar = !alternar
    }

  }

  malabarear(){

    for(const pelota of this.pelotas){

      if(pelota.libre() && this.izquierda.alcanza(pelota))
        this.izquierda.intentar_agarrar(pelota)
      if(pelota.libre() && this.derecha.alcanza(pelota))
        this.derecha.intentar_agarrar(pelota)

      pelota.updraw();
    }

    if(!this.izquierda.activa) this.izquierda.volver()
    if(!this.derecha.activa) this.derecha.volver()

    this.draw();

  }

  draw(){
    imageMode(CENTER)

    // Tronco
    linep(this.pc, createVector(this.pc.x, height))

    // Brazos
    linep(this.ph, this.ci)
    linep(this.ph, this.cd)

    // Antebrazos
    linep(this.ci, this.izquierda.pos)
    linep(this.cd, this.derecha.pos)

    // Manitos
    fill(255)
    circle(this.izquierda.pos.x, this.izquierda.pos.y, 5)
    circle(this.derecha.pos.x, this.derecha.pos.y, 5)

    image(this.cabecita, this.pc.x, this.pc.y, this.cabecita.width/16, this.cabecita.height/16)

    this.izquierda.dibujar_alcance();
    this.derecha.dibujar_alcance();
  }

  //update(){}

}
