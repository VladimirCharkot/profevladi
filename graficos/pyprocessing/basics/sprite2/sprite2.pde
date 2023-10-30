PImage[] idle = new PImage[4];
PImage[] walk = new PImage[4];
int escala = 2;

int cantidad_chaboncitos = 10;
Chaboncito[] chavitos = new Chaboncito[cantidad_chaboncitos];

class Chaboncito{
  int x, y, vx, vy;
  int t = 0;
  int vmax = 20;
  
  Chaboncito(){
    x = int(random(0,600));
    y = int(random(0,600));
    vx = int(random(-vmax,vmax));
    vy = int(random(-vmax,vmax));
  }
  
  void dibujar(){
    deslizar();
    image(walk[t%4], x, y);
    t += 1;
  }
  
  void deslizar(){
    
    // Randomizar la velocidad un toque
    vx = vx + int(random(-vmax/2,vmax/2));
    vy = vy + int(random(-vmax/2,vmax/2));
    
    // Actualizar la velocidad
    x = x + vx;
    y = y + vy;
    
    // Volver a aparecer al salir de los límites de la pantalla
    if(x > 600) x = 0;
    if(y > 600) y = 0;
    if(x < 0) x = 600;
    if(y < 0) y = 600;
    
    // Límite para la velocidad
    if(vx > vmax) vx = vmax;
    if(vy > vmax) vy = vmax;
    if(vx < -vmax) vx = -vmax;
    if(vy < -vmax) vy = -vmax;
  }
  
}

void setup(){
  
  size(600,600);
  
  // Cargar las imágenes: 
  for(int i=1; i<5; i++){
    PImage img = loadImage("Ranger_Idle_" + i + ".png");
    img.resize(img.width*escala, img.height*escala);
    idle[i-1] = img;
  }
  
  for(int i=1; i<5; i++){
    PImage img = loadImage("Ranger_Walk_" + i + ".png");
    img.resize(img.width*escala, img.height*escala);
    walk[i-1] = img;
  }
  
  imageMode(CENTER);
  for(int i  = 0; i < cantidad_chaboncitos; i++){
    chavitos[i] = new Chaboncito();
  }
}

void draw() {
  background(228,228,228);
  for(int i  = 0; i < cantidad_chaboncitos; i++){
    chavitos[i].dibujar();
  }
  delay(100);
}
