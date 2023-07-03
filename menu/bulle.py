from systeme.FondMarin import *

class Bulle:
    def __init__(self, couleurFond: Color) -> None:
        self.couleurFond = couleurFond
        self.espaces = [int(xf*0.01), int(yf*0.01)]
        self.tailleTexte = yf*0.03
        self.largeurMin = int(xf*0.05)
        self.setTexte("0")

    def dessine(self, x: int, y: int) -> None:
        if self.getContact(x, y):
            draw_rectangle_rounded([x, y, self.largeur, self.hauteur], 0.3, 300, self.couleurFond)
        draw_text_ex(police1, self.texte, (int(x+self.largeur/2-self.tt.x/2), int(y+self.espaces[1])), self.tailleTexte, 0, BLACK)

    def setTexte(self, texte: str) -> None:
        self.texte = texte
        self.tt = measure_text_ex(police1, self.texte, self.tailleTexte, 0)
        if self.tt.x+self.espaces[0]*2 >= self.largeurMin:
            self.largeur = self.tt.x+self.espaces[0]*2
        else:
            self.largeur = self.largeurMin
        self.hauteur = self.tt.y+self.espaces[1]*2

    def getDims(self) -> tuple[int]:
        return (self.largeur, self.hauteur)
    
    def getContact(self, x: int, y: int) -> bool:
        """Vérifie si le curseur est sur le bouton.

        Returns:
            bool: True si le curseur est sur le bouton, False dans le cas contraire.
        """
        rep = False
        px = get_mouse_x()
        py = get_mouse_y()
        if px >= x and px <= x+self.largeur:
            if py >= y and py <= y+self.hauteur:
                rep = True
        return rep