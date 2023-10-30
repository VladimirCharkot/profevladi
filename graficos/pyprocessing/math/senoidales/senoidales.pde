void setup(){
  background(0);
  size(600,600);
}

float t = 0;
void draw(){
  delay(20);
  //background(0);
  //fill(205,10);
  //rect(0,0,width-1,height-1);
  
  fill(255);
  
  float a = 50;
  float f = 1.0/8; 
  
  float p1_x = 300 + a*cos(f*t);
  float p1_y = 500 + a*sin(2*f*t);
  
  float p2_x = 100 + a*cos(3*f*t);
  float p2_y = 100 + a*sin(2*f*t);
  
  float p3_x = 500 + a*cos(f*t);
  float p3_y = 100 + a*sin(3*f*t);
  
  stroke(color(255, 10));
  line(p1_x, p1_y, p2_x, p2_y);
  line(p2_x, p2_y, p3_x, p3_y);
  line(p3_x, p3_y, p1_x, p1_y);
  
  //ellipse(p1_x, p1_y, 20, 20);
  //ellipse(p2_x, p2_y, 20, 20);
  //ellipse(p3_x, p3_y, 20, 20);
  
  t += 1;
}
