Clase objeto[];
int cantObjetos = 50;
int umbral = 100;
void setup() {
  size(600, 600);
  objeto = new Clase [cantObjetos];//Creo el vector
  for ( int i=0; i < cantObjetos; i++ ) {
    objeto[i] = new Clase();//Construyo cada Objeto
  }
  
}
// - - - - - - - - - - - - - - - - - - - 
void draw() {
  background(220);
  for ( int i = 0; i < cantObjetos; i++ ) {
    objeto[i].update();
    objeto[i].limite();
    for ( int j = i + 1; j < cantObjetos; j++ ) {
      float distancia = dist(objeto[i].x, objeto[i].y, objeto[j].x, objeto[j].y );
      
      if(distancia < umbral){
        stroke(255);
        stroke(random(110,130), random(110,130), random(110,130));
        line(objeto[i].x, objeto[i].y, objeto[j].x, objeto[j].y);
      }
    }
    objeto[i].dibujar();//Construyo cada Objeto
  }
}

void keyPressed(){
  int intensidad = 25;
  float px = random(-intensidad,intensidad);
  float py = random(-intensidad,intensidad);
  for ( int i = 0; i < cantObjetos; i++ ) {
    objeto[i].perturbar(px, py);
  }
}
