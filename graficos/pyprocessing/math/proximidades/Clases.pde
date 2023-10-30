// - - - - - - - - - - - - - - - - - - - 
class Clase {
  //Atributos
  float x;
  float y; 
  float velocidadX;
  float velocidadY; 
  float tamano;
  float r, g, b;
  
  Clase() {//Constructor
    x = random(0, width);
    y = random(0, height);
    r = random(0, 256);
    g = random(0, 256);
    b = random(0, 256);
    velocidadX = random(-3, 3);
    velocidadY = random(-3, 3);
    tamano = random(20, 50);
  }
  //Metodos - - - - - - - - - - - - - - - - -
  void update() {
    x +=  velocidadX;
    y +=  velocidadY;
  }
  
  void limite() {
    if(x > width){
      x = 0;
    }
    if(x < 0){
      x = width;
    }
    if(y > height){
      y = 0;
    }
    if(y < 0){
      y = height;
    }
  }
  
  void dibujar() {
    fill(r, g, b, 127);
    //ellipse(x, y, tamano, tamano);
  }
  
  void perturbar(float base_x, float base_y){
    float ppx = random(-5,5);
    float ppy = random(-5,5);
    x += base_x + ppx;
    y += base_y + ppy;
  }
}
