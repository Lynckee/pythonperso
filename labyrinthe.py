#pour installer pygame :  Python\Python37-32\python.exe -m pip install pygame
import random
import pygame
import pygame.gfxdraw


"""
**********************
Mode textuel
**********************
"""




"""
nom de la fonction:ListeLabyrinthe
but: creer une liste vide de de coordonées sauf pour le contour du labyrinthe
entrées: x_max et y_max
sortie : la tableau du labyrinthe
"""

def ListeLabyrinthe(x_max, y_max):
    t = []
    for x in range (x_max):
        col = []
        for y in range (y_max):
            if (y == 0) or (y == y_max - 1) or (x == 0) or (x == x_max - 1):
                col.append(1)
            else:
                col.append(0)
        t.append(col)
    return t



"""
nom de la fonction : InitialisationPrefabs
but : creer une liste de 5 par 5 de mini labyrinthe, pour pouvoir assembler plus tard tout ces mini labyrinthe dans le plus gros 
entrée : nb_prefab_max
sortie : liste_prefab
"""

def InitialisationPrefabs(nb_prefab_max):
    " première partie, tableau vide de prefab"
    liste_prefab = []
    for nb_prefab in range (nb_prefab_max):
        x_prefab = []
        for x in range (5):
            y_prefab = []
            for y in range (5):
                y_prefab.append(0)
            x_prefab.append(y_prefab)
        liste_prefab.append(x_prefab)


    "deuxième partie, création de prefab"

    "prefab 1"
    liste_prefab[0][0][0] = 1
    liste_prefab[0][1][0] = 1
    liste_prefab[0][2][0] = 1
    liste_prefab[0][3][0] = 1
    liste_prefab[0][4][0] = 1
    
    "prefab 2"
    liste_prefab[0][1][0] = 1
    liste_prefab[0][1][1] = 1
    liste_prefab[0][1][2] = 1
    liste_prefab[0][1][3] = 1
    liste_prefab[0][1][4] = 1
    
    
    "prefab 3"
    liste_prefab[2][0][0] = 1
    liste_prefab[2][1][1] = 1
    liste_prefab[2][2][2] = 1
    liste_prefab[2][3][3] = 1
    liste_prefab[2][4][4] = 1
    "prefab 4"
    liste_prefab[3][0][0] = 1
    liste_prefab[3][0][1] = 1
    liste_prefab[3][0][2] = 1
    liste_prefab[3][0][3] = 1
    liste_prefab[3][0][4] = 1
    liste_prefab[3][1][0] = 1
    liste_prefab[3][2][0] = 1
    liste_prefab[3][3][0] = 1
    liste_prefab[3][4][0] = 1
    liste_prefab[3][4][1] = 1
    liste_prefab[3][4][2] = 1
    liste_prefab[3][4][3] = 1
    liste_prefab[3][4][4] = 1

    
    return liste_prefab
        
    

"""
nom de la fonction : ConstructionChemin
but : contruire un chemin aléatoire qui ira de l'entrée du labyrinthe jusqu'a sa sortie. Sur les coordonées de celui-ci, les blocs seront effacés
entrée :abyrinthe,x_max, y_max
sortie : rien, modifie directement le tableau du labyrinthe
"""

def ConstructionChemin(labyrinthe,x_max, y_max):
    position_random_depart = random.randint(1, y_max - 2)
    labyrinthe[0][position_random_depart] = 2
    x_laby = 0
    y_laby = position_random_depart
    global y_position_joueur_depart
    y_position_joueur_depart = y_laby
    while (labyrinthe[x_max - 1][y_laby] != 2):
        random_direction = random.random()
        if (random_direction <= 0.20):
            # gauche
            if (labyrinthe[x_laby - 1][y_laby] != 1):
                x_laby = x_laby -1
        if (random_direction >= 0.20) and (random_direction <= 0.40):
            #haut
            if (labyrinthe[x_laby][y_laby - 1] != 1):
                y_laby = y_laby -1
        elif (random_direction >= 0.40) and (random_direction <= 0.60):
            #bas
            if (labyrinthe[x_laby][y_laby + 1] != 1):
                y_laby = y_laby  +1
        else:
            #droite
            x_laby = x_laby  + 1
        labyrinthe[x_laby][y_laby] = 2

        

"""
nom de la fonction : AjoutPrefabLaby
but : ajouter pour un nombre donné les prefabs au labyrinthe, sur une position aléatoire  
entrée : x_max, y_max, labyrinthe, liste_prefab, nb_prefab_max, nb_prefab_a_dessiner
sortie : rien, modifie directement la liste labyrinthe
"""
def AjoutPrefabLaby(x_max, y_max, labyrinthe, liste_prefab, nb_prefab_max, nb_prefab_a_dessiner):
    for n in range (nb_prefab_a_dessiner):
        n_prefab_random = random.randint(0, nb_prefab_max - 1 )
        x_random = random.randint(0, x_max - 3)
        y_random = random.randint(0, y_max - 3)
        for x in range (3):
            for y in range (3):
                if (liste_prefab[n_prefab_random][x][y] == 1) and ( labyrinthe[x + x_random][y + y_random] != 2):
                    labyrinthe[x + x_random][y + y_random] = 1



"""
nom de la fonction: ConstructionDuLabyrinte
but : afficher le labyrinte (1 = mur, 0=rien, 2=chemin)
entrées: labyrinthe, x_max, y_max, x_joueur, y_joueur
sortie: rien, affiche simplement le labyrinthe
"""
def AffichageDuLabyrinte(labyrinthe, x_max, y_max, x_joueur, y_joueur):            
    for y in range (y_max):
        for x in range (x_max):
            if (labyrinthe[x][y] != 1): 
                if (x != x_joueur) or (y != y_joueur): 
                    print (end=" ")
                else:
                    print (end ="J")
            else:
                print (end="*")
        print()



                    
"""
nom de la fonction: DeplacementJoueur
but : deplacer le joueur en fonction de la direction que l'on choisit
entrées: x_joueur, y_joueur, labyrinthe
sortie: le nouveau x_joueur et y_joueur
"""

def DeplacementJoueur(x_joueur, y_joueur, labyrinthe):
    choix = input("Vers ou voulez vous vous déplacer (G / D / H / B) ?")
    if (choix == "G") or (choix == 'g'):
        if (labyrinthe[x_joueur - 1][y_joueur] != 1):
            x_joueur = x_joueur - 1
    elif (choix == "D") or (choix == 'd'):
        if (labyrinthe[x_joueur + 1][y_joueur] != 1):
            x_joueur = x_joueur + 1 
    elif (choix == "H") or (choix == 'h'):
        if (labyrinthe[x_joueur][y_joueur - 1] != 1):
            y_joueur = y_joueur - 1
    elif (choix == "B") or (choix == 'b'):
        if (labyrinthe[x_joueur][y_joueur + 1] != 1):
            y_joueur = y_joueur + 1
    return (x_joueur, y_joueur)


    

"""
nom de la fonction: LongueurLabyrinthe
but : donner les longeur et largeur du labyrinthe que le joueur a choisi
entrées: rien
sortie: choix_l , choix_L
"""
def LongueurLabyrinthe():
    try:
        choix_l = int(input("choisisez la longeur de votre labyrinthe (valeur par défaut = 20)"))
        if (choix_l < 5 or choix_l > 50):
            choix_l = 20
    except:
        choix_l = 20
    try:
        choix_L = int(input("choisisez la hauteur de votre labyrinthe (valeur par défaut = 10)"))
        if (choix_L < 5 or choix_L > 50):
            choix_L = 10
    except:
        choix_L = 10
        
    return choix_l, choix_L

"""
**********************
Mode Pygame
**********************
"""



"""
nom de la fonction: AfficheDuLabyrinteGraph
but : afficher le labyrinthe grâce a des carrés fournis par pygame et des valeurs de la liste du labyrinthe
entrées: y_max, x_max, labyrinthe
sortie: le nouveau DISPLAY, l'interface de jeu 
"""


def AfficheDuLabyrinteGraph(labyrinthe, x_max, y_max):
    pygame.init()
        
    BLUE=(0,0,255)
    WHITE=(255,255,255)
    DISPLAY=pygame.display.set_mode((25 * x_max + 50, 25 * y_max + 50),0,32)

    DISPLAY.fill(WHITE)

    for x in range (x_max):
        for y in range (y_max):
            if (labyrinthe[x][y] == 1):
                pygame.draw.rect(DISPLAY,BLUE,(0 + x*25,0 + y*25, 25,25))
    pygame.display.update()
    return DISPLAY



"""
nom de la fonction: DessineJoueurNouvellePosition
but : afficher le joueur
entrées: DISPLAY, x_joueur, y_joueur, labyrinthe, x_max, y_max
sortie: rien, puisque qu'on déplace le joueur directement depuis la fonction
"""


def DessineJoueurNouvellePosition(DISPLAY, x_joueur, y_joueur, labyrinthe, x_max, y_max):
    RED=(255,0,0)
    WHITE=(255,255,255)
    
    try:
        while 1:
            event = pygame.event.wait()
            pygame.draw.rect(DISPLAY,RED, (0 + x_joueur*25,0 + y_joueur*25, 25,25))
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if (labyrinthe[x_joueur + 1][y_joueur] != 1):
                        x_joueur = x_joueur + 1
                        pygame.draw.rect(DISPLAY,RED, (0 + x_joueur*25,0 + y_joueur*25, 25,25))
                        pygame.draw.rect(DISPLAY,WHITE,(0 + (x_joueur - 1)*25,0 + (y_joueur)*25, 25,25))
                if event.key == pygame.K_LEFT:
                    if (labyrinthe[x_joueur - 1][y_joueur] != 1):
                        x_joueur = x_joueur - 1
                        pygame.draw.rect(DISPLAY,RED,(0 + x_joueur*25,0 + y_joueur*25, 25,25))
                        pygame.draw.rect(DISPLAY,WHITE,(0 + (x_joueur + 1)*25,0 + (y_joueur)*25, 25,25))
                if event.key == pygame.K_UP:
                    if (labyrinthe[x_joueur][y_joueur - 1] != 1):
                        y_joueur = y_joueur - 1
                        pygame.draw.rect(DISPLAY,RED,(0 + x_joueur*25,0 + y_joueur*25, 25,25))
                        pygame.draw.rect(DISPLAY,WHITE,(0 + (x_joueur)*25,0 + (y_joueur + 1)*25, 25,25))
                if event.key == pygame.K_DOWN:
                    if (labyrinthe[x_joueur][y_joueur + 1] != 1):
                        y_joueur = y_joueur + 1
                        pygame.draw.rect(DISPLAY,RED,(0 + x_joueur*25,0 + y_joueur*25, 25,25))
                        pygame.draw.rect(DISPLAY,WHITE,(0 + (x_joueur)*25,0 + (y_joueur - 1)*25, 25,25))
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
                
                
            pygame.display.update()
            if (x_joueur >= x_max -1):
                is_out = True
                print ("")
                print ("")
                print ("bravo ! vous êtes sorti du labyrinthe!")
                
                break
                
    finally:
        pygame.quit()

"""
Initialisation des variables 
"""

x_max = 20
y_max = 10
x_joueur = 0
y_joueur = 0
nb_prefab_max = 4
nb_prefab_a_dessiner = 35
is_out = False


print ("************************************************")
print ("            WELCOME TO THE LABYRINTH            ")
print ("************************************************")


"""
appel des fonctions
"""

x_max, y_max = LongueurLabyrinthe()
nb_prefab_a_dessiner = round((x_max * y_max) / 4)
labyrinthe = ListeLabyrinthe(x_max, y_max)
liste_prefab = InitialisationPrefabs(nb_prefab_max)
ConstructionChemin(labyrinthe,x_max, y_max)
y_joueur = y_position_joueur_depart
AjoutPrefabLaby(x_max, y_max, labyrinthe, liste_prefab, nb_prefab_max, nb_prefab_a_dessiner)


choix = (input("Voullez vous choisir la version pygame ou textuel ?"))
if (choix == "pygame") or (choix == "Pygame"):
    modePyGame = True
    print ("pour se déplacer, utilisez les flèches directionnelles. Pour quitter le jeu appuyez sur q")
else:
    modePyGame = False

    
if (modePyGame):
    DISPLAY = AfficheDuLabyrinteGraph(labyrinthe, x_max, y_max)
    DessineJoueurNouvellePosition(DISPLAY, x_joueur, y_joueur, labyrinthe, x_max, y_max)    

else:
    AffichageDuLabyrinte(labyrinthe, x_max, y_max, x_joueur, y_joueur)
    while (x_joueur != x_max -1):
        (x_joueur, y_joueur) = DeplacementJoueur(x_joueur, y_joueur, labyrinthe)
        AffichageDuLabyrinte(labyrinthe, x_max, y_max, x_joueur, y_joueur)
    is_out = True
    
    
    
if (is_out):
    print ("")
    print ("")
    print ("bravo ! vous êtes sorti du labyrinthe!")


pygame.quit()
    




     
