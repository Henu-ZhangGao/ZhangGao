ArrayList<Link> links = new ArrayList<Link>();

void setup() {
  size(640, 640);

  for (int i = 0; i < 360; i+=90) {
    links.add(new Link(i));
  }
}

void draw() {
  background(255);
  translate(width/2, height/2);
  for (Link l : links) {
    l.move();
    l.draw();
  }
}

class Link {
  Particle p, p2;
  
  int i;

  Link(int i) {
    this.i = i;
    p = new Particle();
    p2 = new Particle();
  }

  void draw() {
    p.draw();
    p2.draw();
  }

  void move() {
    PVector loc = new PVector(sin(radians(i+frameCount*2))*100, cos(radians(i+frameCount*2))*100);
    p.move(new PVector(loc.x+sin(radians(i))*50, loc.y+cos(radians(i))*50));
    p2.move(new PVector(loc.x-sin(radians(i))*50, loc.y-cos(radians(i))*50));
  }
}

class Particle {
  ArrayList<PVector> points = new ArrayList<PVector>();
  
  void draw() {
    stroke(30);
    for (int i = points.size()-1; i > 0; i--) {
      PVector l = points.get(i);
      PVector l2 = points.get(i-1);
      strokeWeight(map(i, 0, points.size(), 0, 20));
      line(l.x, l.y, l2.x, l2.y);
    }
    
    for (int i = points.size()-1; i > 0; i--) {
      PVector l = points.get(i);
      PVector l2 = points.get(i-1);
      stroke(map(i, points.size()-1, 0, 255, 0), 50, 100);
      strokeWeight(map(i, 0, points.size(), 0, 10));
      line(l.x, l.y, l2.x, l2.y);
    }
  }

  void move(PVector loc) {
    points.add(loc.get());

    if (points.size() > 60) {
      points.remove(0);
    }
  }
}
