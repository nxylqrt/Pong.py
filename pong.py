import pyxel
import random
import time 

class Jeu:
    def __init__(self):
        
        pyxel.init(256,128,title="✮⋆˙PONG✮⋆˙")
        
        self.joueur1_x = 25
        self.joueur1_y = 45
        self.joueur2_x = 224
        self.joueur2_y = 45
        self.balle_x = 128
        self.balle_y = 64
        self.droite = True
        self.directiony = random.choice([True,False])
        self.compt = 0
        self.speed = 3
        self.degres = 3
        self.points = [0,0]
        self.en_reapparition = False
        self.pause = False
        pyxel.run(self.update, self.draw)
    
    def toggle_pause(self):
        self.pause = not self.pause
        
        
    def joueur1_xy(self):
        """Déplacement du Joueur 1"""
        if pyxel.btn(pyxel.KEY_Q) and self.joueur1_y > 3:
            self.joueur1_y -= 4
            
        if pyxel.btn(pyxel.KEY_S) and self.joueur1_y < 96:
            self.joueur1_y += 4
            
    def joueur2_xy(self):
        """Déplacement du Joueur 2"""
        if pyxel.btn(pyxel.KEY_RIGHT) and self.joueur2_y > 3:
            self.joueur2_y -= 4
            
        if pyxel.btn(pyxel.KEY_DOWN) and self.joueur2_y < 96:
            self.joueur2_y += 4
            
            
    def deplacement_horizontal(self):
        """Déplacement de la balle sur l'axe x"""
        if self.droite == True:
            self.balle_x += self.speed
        else:
            self.balle_x -= self.speed
            
        if self.planche_touchee() and self.droite == True: 
            self.droite = False
            
        elif self.planche_touchee() and self.droite == False:
            self.droite = True
        
        
    def deplacement_vertical(self):
        """Déplacement de la balle sur l'axe y"""
        if self.directiony == True:
            self.balle_y -= self.degres
        else:
            self.balle_y += self.degres
            
        if self.bord_touche_h() and self.directiony == True:
            self.directiony = False
            
        elif self.bord_touche_h() and self.directiony == False:
            self.directiony = True
            
    
    def planche_touchee(self):
        if self.balle_y in range(self.joueur1_y , (self.joueur1_y + 30)) and self.balle_x <= 34 and self.balle_x > 25 :
            return True    
        
        elif self.balle_y in range(self.joueur2_y , (self.joueur2_y + 30)) and self.balle_x >= 220 and self.balle_x < 230 :
            return True

        else:
            return False
        
    def bord_touche_h(self):
        if self.balle_y >= 124 or self.balle_y <= 2:
            return True     
        else:
            return False

    def bord_touche_v(self):
        if self.balle_x >= 254 or self.balle_x <= 2 :
            return True
        
        else:
            return False
        
    def vitesse_balle(self):
        """Augmente la vitesse de la balle au fil de la partie"""
        if self.planche_touchee() == True: 
            self.compt += 1
            
        elif self.compt >= 5:
            self.speed += 1
            self.compt = 0
            
            
    def reapparition(self):
        if self.bord_touche_v() and not self.victoire():
            self.en_reapparition = True
            self.balle_x = 128
            self.balle_y = 64
            self.joueur1_x = 25
            self.joueur1_y = 45
            self.joueur2_x = 224
            self.joueur2_y = 45
            self.speed = 0
            self.degres = 0
              
        elif self.balle_x == 128 and self.balle_y == 64 and self.en_reapparition:
            time.sleep(3)
            self.en_reapparition = False
            self.speed = 3
            self.degres = 3
            
            
    def comptage_points(self):
        if self.speed <= 3:
            if self.balle_x <= 5:
                self.points[1] += 1
            
            elif self.balle_x >= 251:
                self.points[0] += 1
        else:
            if self.balle_x <= 9:
                self.points[1] += 1
            
            elif self.balle_x >= 249:
                self.points[0] += 1
                
    def victoire(self):
        if self.points[0] >= 3:
            pyxel.text(100,60,'Joueur 1 Gagne!',7)
            return True  
        elif self.points[1] >= 3:
            pyxel.text(100,60,'Joueur 2 Gagne!',7)
            return True
        else:
            return False
            
        
            
            
    def draw(self):
        pyxel.cls(3)
        if not self.victoire():
            pyxel.rect(self.joueur1_x, self.joueur1_y, 5, 30, 11)
            pyxel.rect(self.joueur2_x, self.joueur2_y, 5, 30, 11)
            pyxel.circ(self.balle_x, self.balle_y, 2, 7)
            pyxel.text(119,7,f'{self.points[0]} - {self.points[1]}',7)
        if self.pause == True :
            pyxel.rect(275, 25,15,50,7)
            pyxel.rect(305, 25,15,50,7)
            pyxel.text(50, 120,'Le jeu est en pause',7)
            
        
    def update(self):
        if not self.pause:
            self.joueur1_xy()
            self.joueur2_xy()
            self.deplacement_horizontal()
            self.deplacement_vertical()
            self.vitesse_balle()
            self.reapparition()
            self.comptage_points()
            self.victoire()
            
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.toggle_pause()

Jeu()