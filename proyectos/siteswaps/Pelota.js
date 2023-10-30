let ground = 50;
let piso = 400;

class Particula {
  constructor(pos, vel) {
    this.pos = pos;
    // this.posd = pos
    this.vel = vel;
    this.r = 5;
    this.acc = createVector(0, 1); // gravedad?
    this.sujeta = false  // Puede ser un vector o false
    this.cayendo = false
  }

  libre(){
    return !this.sujeta && this.cayendo
  }

  sujetar(obj){
    this.sujeta = obj
    this.cayendo = false
    this.pos = obj.pos.copy()
    this.vel = createVector(0, 0);
    this.acc = createVector(0, 0);
  }

  disparar(v) {
    this.sujeta = false;
    this.vel = v;
  }

  updraw(){
    this.update()
    this.draw()
  }

  update() {
    if (!this.sujeta) {
      this.pos.add(this.vel);
      this.vel.add(acc);

      if (this.pos.y > piso) {
        this.pos.y = piso;
        this.vel = createVector(
          this.vel.x - this.vel.x * 0.5,
          -(this.vel.y - this.vel.y * 0.4)
        );
      }
      this.cayendo = this.vel.y > 0

    } else {
      this.pos = this.sujeta.pos.copy()
    }
  }

  draw() {
    //console.log(`En ${this.pos}\n`)
    circle(this.pos.x, this.pos.y, this.r);
  }
}

class Pelota extends Particula {
  constructor(pos, color) {
    super(pos, createVector(0, 0));
    this.color = color;
  }

  draw() {
    fill(this.color);
    super.draw();
  }
}
