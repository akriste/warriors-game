
import turtle
import random
import time

delka_okna = 900
vyska_okna = 650
wn = turtle.Screen()
wn.setup(delka_okna, vyska_okna)
wn.bgcolor("grey11")
wn.title("Warriors")
t = turtle.Turtle()
t.hideturtle()
t.speed = 0
wn.tracer(0) 

for i in range(8):
    wn.register_shape(f"img/v{i}.gif")
    wn.register_shape(f"img/f{i}.gif")

je_pauza = False

def aktivuj_pauzu():
    global je_pauza
    if je_pauza == True:
        je_pauza = False
    else:
        je_pauza = True

class Hrac(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pu()
        self.goto(-350, 0)
        self.shape("img/v7.gif")
        self.dy = 0 # rychlost nahoru a dolů, delta-y
        self.dx = 0 # rychlost doleva a doprava, delta-x
        
    def nahoru(self):
        self.dy = 0.5

    def dolu(self):
        self.dy = -0.5 

    def doprava(self):
        self.dx = 0.5

    def doleva(self):
        self.dx = -0.5

    def stop(self):
        self.dy = 0
        self.dx = 0

    def pohyb(self):
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)

        # hranicí neprojdeš 
        if self.ycor() > 340:
            self.sety(340)
            self.dy = 0

        elif self.ycor() < -350:
            self.sety(-350)
            self.dy = 0
        
        elif self.xcor() > 440:
            self.setx(440)
            self.dx = 0

        elif self.xcor() < -780:
            self.setx(-780)
            self.dx = 0

class Zbran(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pu()
        self.color("firebrick2")
        self.shape("circle")
        self.shapesize(0.1, 1, 0) 
        self.speed(9)
        self.dx = 0  
    
    def strely(self):
        self.goto(hrac.xcor(), hrac.ycor() + 35)
        self.dx = 9
        
    def strilej(self):
        self.setx(self.xcor() + self.dx)

class Nepritel(turtle.Turtle):
    def __init__(self, tvar):
        turtle.Turtle.__init__(self, shape=tvar)
        self.pu()
        self.goto( 430, random.randint(-320, 320) )
        self.speed(0)
        self.dx = -0.4 # rychlost nepřítele
        self.skore = 0
        self.frame = 0
        self.frames = ["img/f0.gif", "img/f1.gif", "img/f2.gif", "img/f3.gif", 
                       "img/f4.gif", "img/f5.gif", "img/f6.gif", "img/f7.gif"]
      
    def pohyb(self):
        self.setx(self.xcor() + self.dx)

        # přes hranici neprojdou
        if self.xcor() <= -800:
            self.goto( 440, random.randint(-320, 320) )
     
    def promen_vojaka(self):
        tvary = ["img/v0.gif", "img/v1.gif", "img/v2.gif", 
                 "img/v3.gif", "img/v4.gif", "img/v5.gif"]
        self.shape( random.choice(tvary) )

    def predstav_vojaky(self):
        army = "Armáda:"
        self.goto(580, 110)
        self.color("darkslategray")
        self.write( army, font=("Arial", 18, "normal") )

        self.pensize(4)
        self.color("darkslategray")
        self.pu()
        self.goto(600, -450)

        for strana in range(2):
            self.pd()
            self.fd(260)
            self.circle(60, 90)
            self.fd(420)
            self.circle(60, 90)
            self.ht()
            
    def animuj_vojaky(self):
        self.goto(740, -200)
        self.frame += 1
        
        if self.frame >= len(self.frames):
            self.frame = 0

        self.shape( self.frames[self.frame] )
        
        wn.ontimer(self.animuj_vojaky, 3000) # milisekundy

class Stit(Nepritel):
    def __init__(self, tvar):
        Nepritel.__init__(self, tvar)
        self.pu()
        self.goto( 300, random.randint(-350, 300) )
        self.speed(6) 
        self.dx = -0.3 
        self.shape("img/v6.gif")
        self.skore = 0

class Castecky(turtle.Turtle):
    def __init__(self, tvar, barva, startx, starty):
        turtle.Turtle.__init__(self, tvar)
        self.pu()
        self.shapesize(stretch_wid=0.1, stretch_len=0.2, outline=None)
        self.goto(-1000, -1000) # buď mimo obrazovku
        self.frame = 0

    def exploduj(self, startx, starty):
        bum = ["black", "red2"]
        self.color( random.choice(bum) )
        self.goto(startx, starty)
        self.setheading( random.randint(0, 350) )
        self.frame = 1
       
    def pohyb_exp(self):
        if self.frame > 0:
            self.fd(6)
            self.frame += 1
           
        if self.frame > 40:
            self.frame = 0
            self.goto(-1000, -1000) # pryč z dohledu
            
        self.penup()

class Cara(turtle.Turtle):
    def __init__(self, tvar, startx, starty):
        turtle.Turtle.__init__(self, tvar)
        self.color("darkslategray")
        self.shape("circle")
        self.pensize(1)
        self.ht()
        self.pu()
        self.goto(-865, -390)
        self.pd()
        self.dot()
        self.left(90)
        self.fd(780)
        self.dot()       
    
class Hra():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.delka_okna = delka_okna
        self.vyska_okna = vyska_okna
        self.skore = 0
        
    def hraci_plocha(self):
        self.pen.color("navy")
        self.pen.pensize(4)
        self.pen.pu()
        self.pen.goto(-820, -450)

        for strana in range(2):
            self.pen.pd()
            self.pen.fd(delka_okna * 1.4)
            self.pen.circle(60, 90) 
            self.pen.fd(vyska_okna * 1.2)
            self.pen.circle(60, 90)
            self.pen.ht()
            self.pen.pd() # tohle je tu jen pro undo které hned následuje, načítá se tak skore
        
    def kresli_skore(self):
        self.pen.undo()
        msg = "Skóre: %s" % (self.skore)
        self.pen.pu()
        self.pen.goto(580, 380)
        self.pen.color("darkslategray")
        self.pen.write( msg, font=("Arial", 18, "normal") )
        
hrac = Hrac()
hra = Hra()
hra.hraci_plocha()
hra.kresli_skore()
zbran = Zbran()
nepritel = Nepritel("img/v1.gif")
stitak = Stit("img/v6.gif")
animace = Nepritel("img/f0.gif")
animace.animuj_vojaky()
predstaveni = Nepritel("circle")
predstaveni.predstav_vojaky()
cara = Cara("circle", 0, 0)

castecky = []
for i in range(35):
    castecky.append( Castecky("circle", "red", 0, 0) )

wn.listen()
wn.onkeypress(hrac.nahoru, "Up")
wn.onkeypress(hrac.dolu, "Down")
wn.onkeypress(hrac.doprava, "Right")
wn.onkeypress(hrac.doleva, "Left")
wn.onkeypress(hrac.stop, "s")
wn.onkeypress(zbran.strely, "space")
wn.onkeypress(aktivuj_pauzu, "p")

while True:
    if not je_pauza:
        wn.update()
        hrac.pohyb()
        zbran.strilej()
        nepritel.pohyb()
        stitak.pohyb()
        for castecka in castecky:
            castecka.pohyb_exp()

        # zasažení nepřítele
        if nepritel.distance(zbran) < 50: # distance je default
            nepritel.promen_vojaka()
            nepritel.goto( 440, random.randint(-350, 350) )
            zbran.goto(0, delka_okna)
            hra.skore += 1
            hra.kresli_skore()

        # elif nepritel.distance(hrac) < 50:
        #     print("Game ouvrrr, chytili Tě!")
        #     exit()
       
        elif stitak.distance(zbran) < 70:
            stitak.backward(-40)
            zbran.goto(0, delka_okna)
            for castecka in castecky:
                castecka.exploduj(stitak.xcor() - 45, stitak.ycor() + 45)
            hra.skore += 1
            hra.kresli_skore()

        if nepritel.xcor() <= -799.9:
            hra.skore -= 1
            hra.kresli_skore()

        elif stitak.xcor() <= -799.8:
            hra.skore -= 1
            hra.kresli_skore()        
            
    else:
        wn.update()
        
  