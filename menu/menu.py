from systeme.FondMarin import *
from ui.bouton.bouton import Bouton
from menu.bulle import Bulle
from random import randint

class Menu:
    def __init__(self) -> None:
        self.alea()
        # Boutons
        self.btHasard = Bouton(TB1o, BTV, "Nouveau", '', [self.alea])
        # Bulles
        self.rouge = Bulle(RED)
        self.vert = Bulle(GREEN)
        self.bleu = Bulle(BLUE)
        # Images
        """bn = load_image('images/menu/bn.png')
        ratio = yf*0.3/bn.height
        image_resize(bn, int(bn.width*ratio), int(bn.height*ratio))
        self.ibn = load_texture_from_image(bn)
        unload_image(bn)
        j1 = load_image('images/menu/j1.png')
        image_resize(j1, int(j1.width*ratio), int(j1.height*ratio))
        self.ij1 = load_texture_from_image(j1)
        unload_image(j1)"""
        # Between the worlds
        self.play = False
        self.message = ""
        self.lu = True

    def dessine(self):
        # Affichage couleur
        y = 0
        draw_rectangle(0, y, xf, int(yf*0.4), self.couleur)
        y = int(yf*0.4)
        draw_rectangle_gradient_v(0, y, xf, int(yf*0.05), self.couleur, WHITE)
        y = int(yf*0.43)
        espace = int(xf*0.02)
        # RGB
        self.rouge.setTexte(str(self.couleur[0]))
        self.vert.setTexte(str(self.couleur[1]))
        self.bleu.setTexte(str(self.couleur[2]))
        self.rouge.dessine(int(xf/2-self.rouge.getDims()[0]-espace-self.vert.getDims()[0]/2), y)
        self.vert.dessine(int(xf/2-self.vert.getDims()[0]/2), y)
        self.bleu.dessine(int(xf/2+espace+self.vert.getDims()[0]/2), y)
        # options
        self.btHasard.dessine(int(xf/2), int(yf*0.70))
        # numéro de version
        taille = int(yf*0.03)
        tv = measure_text_ex(police3i, version, taille, 0)
        draw_text_pro(police2i, f"v{version}", (int(xf*0.009), int(yf-tv.y*1.1)), 
                    (0, 0), 0, taille, 0, GRAY)
        if is_key_pressed(32):
            self.alea()

    def dessineValeur(self, x: int, y: int, valeur: str) -> tuple[int]:
        largeur = int(xf*0.35)
        taille = int(xf*0.045)
        tt = measure_text_ex(police2, valeur, taille, 0)
        draw_rectangle_lines(x, y, largeur, int(tt.y*1.6), BLACK)
        draw_text_ex(police2, valeur, (int(x+largeur*0.03), int(y+tt.y*0.3)), taille, 0, BLACK)
        return (largeur, int(tt.y*1.6))

    def alea(self) -> None:
        self.couleur = [randint(0, 255), randint(0, 255), randint(0, 255), 255]

    # Between the worlds
    def portailBoreal(self) -> None:
        i = 0
        v = False
        while i < len(self.opt) and not v:
            if self.opt[i][0].getContact():
                v = True
                self.nouveauMessage(self.opt[i][1])
            else:
                i += 1

    def nouveauMessage(self, message: str) -> None:
        self.message = message
        self.lu = False