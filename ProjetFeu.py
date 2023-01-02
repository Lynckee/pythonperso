import random
import pygame
import threading
import time
import pygame.gfxdraw
import math
#note: in faut avoir pygame installé pour faire tourner le projet ! 


"""
----------------------------------------
Nom de la Fonction: ChoixTaille
pas de paramètres
but: renvoyer la taille x et y de la carte d'arbre que le joueur à choisi
renvoie: xMax, yMax
----------------------------------------
"""
def ChoixTaille():
    try:
        # on regarde si le joueur a bien rentrer un int
        xMax =int(input("Choisissez la longueur maximum ( valeur par défaut: 30, minimum 5 )"))
        if (xMax <= 5):
            xMax = 5
    except:
        xMax = 30
    try:
        # pareil pour ici
        yMax = int(input("Choisissez la largueur maximum ( valeur par défaut: 30,  minimum 5)"))
        if (yMax <= 5):
            yMax = 5
    except:
        yMax = 30
    return xMax,yMax

"""
----------------------------------------
Nom de la Fonction: ChoiceSpeed
pas de paramètres
but: renvoyer la valeur de la vitesse que le joueur a choisi ( note: on transforme cette valeur en temps, en mini seconde)
renvoie: speed *100 
----------------------------------------
"""
def ChoiceSpeed():
    # on regarde si la valeur est bien de type float 
    try:
        speed = float(input("Choissez la vitesse de propagation(le temps que met pygame a s'afficher) (valeur par défaut: 0.3, minimum supérieur à 0, maximum inférieur a 10)"))
        if (speed <= 0 or speed >= 10):
            speed = 0.3
    except:
        speed = 0.3
    # on renvoi la vitesse, ici le temps en minisecondes + on le transforme en int 
    return (int(speed *1000))
        

"""
----------------------------------------
Nom de la Fonction: ChoicePourcent
pas de paramètres
but: renvoyer la valeur du pourcent que le joueur a choisi pour l'apparition des arbres
renvoie: pourcent
----------------------------------------
"""
def ChoicePourcent():
    # on regarde si la valeur est bien de type int 
    try:
        pourcent = int(input("Choisissez le pourcentage de chance d'apparition des arbres (valeur par défaut: 65, minimum supérieur à 0, maximum 100)"))
        if (pourcent <= 0 or pourcent >100):
            pourcent = 65
    except:
        pourcent = 65
    return pourcent
    
"""
----------------------------------------
Nom de la Fonction: ConstructionTableauVide
paramètres: maxX,maxY -> la taille max de la carte
but: renvoyer une liste a deux dimensions correspondant aux coordonées vides de la carte
renvoie: tableauCoo
----------------------------------------
"""
def ConstructionTableauVide(maxX,maxY):
    global VIDE
    tableauCoo = []
    for x in range (maxX):
        colonne = []
        for y in range (maxY ):
            colonne.append(VIDE)
        tableauCoo.append(colonne)
    return tableauCoo



"""
----------------------------------------
Nom de la Fonction: ConstructionArbreAleatoire
paramètres: tableauVide -> le tableau de coordonées vides fait dans ConstructionTableauVide
but: renvoyer une liste a deux dimensions avec des arbres en plus générés aléatoirement
renvoie: tableauVide ( qui n'est plus vide )
----------------------------------------
"""
def ConstructionArbreAleatoire(tableauVide,pourcent):
    global ARBRE
    for x in range (len(tableauVide)):
        for y in range (len(tableauVide[x])):
            arbreRandom = random.randint(0,100)
            if (arbreRandom <= pourcent):
                # pour dire qu'une case est un arbre
                tableauVide[x][y] = ARBRE
                global nbArbreTotal
                # on regarde combien on a générés d'abres au total, pour pouvoir s'en servir plus tard, dans une variable globale
                nbArbreTotal = nbArbreTotal + 1
    return tableauVide



"""
----------------------------------------
Nom de la Fonction: Start
paramètres: tableauArbre,xMax,yMax -> le tableau d'arbres remplis dans ConstructionArbreAleatoire et la taille x et y max choisis par le joueur
but: afficher graphiquement grâce à pygame les arbres et les cases vides
elle affiche les arbres mais elle renvoie aussi DISPLAY, qui servira a afficher d'autres cases plus tard
----------------------------------------
"""
def Start(tableauArbre,xMax,yMax):
    global ARBRE
    pygame.init()
    
    GREEN=(0,255,0)
    WHITE=(255,255,255)
    #on définie DISPLAY, la taille de la fenetre avec la taille max
    DISPLAY=pygame.display.set_mode((25 * (xMax - 2)  + 50, 25 * (yMax - 2)  + 50),0,32)
    pygame.RESIZABLE
    # on remplie dans un premier temps toute la fenêtre de blanc
    DISPLAY.fill(WHITE)
    for x in range (xMax):
        for y in range (yMax):
            # si il y a un arbre 
            if (tableauArbre[x][y] == ARBRE):
                # on remplie cette case de vert 
                pygame.draw.rect(DISPLAY,GREEN,(0 + x*25,0 + y*25, 25,25))
    # rafraîchissement de pygame pour montrer les cases construites 
    pygame.display.update()
    return DISPLAY


"""
----------------------------------------
Nom de la Fonction: MouseChoice
paramètres: tableauArbre,RED,xMax,yMaxn,DISPLAY -> le tableau d'arbres remplis dans ConstructionArbreAleatoire,la couleur rouge,
la taille x et y max choisis par le joueur et DISPLAY donné dans Start
but: renvoyer la position x et y de la souris pour la bruler, avec un test pour regarder si il y a un arbre
renvoie: un taleau x et y de la position de la souris ou None ( si il n'y a pas d'arbre)
----------------------------------------
"""
def MouseChoice(tableauArbre,RED,xMax,yMaxn,DISPLAY):
    pygame.event.clear()
    global ARBRE
    # tant qu'on a pas cliquer, on attend que le joueur clique sur un arbre
    asChoiced = False
    while asChoiced == False:
        event = pygame.event.wait()
        pygame.display.update()
        # test pour savoir si le joueur a cliquer 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # on récupère la position de la souris (en pixel!)
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                asChoiced = True
    # ici on transforme x et y ( en pixel ) en position puis en arrodissant à la partie entière 
    Mouse_x = math.floor(Mouse_x/ 25)
    Mouse_y = math.floor(Mouse_y/ 25)
    # on regarde si il y a un arbre à la position choisie 
    if (tableauArbre[Mouse_x][Mouse_y] == ARBRE):
        # si oui on renvoi une liste de tuple
        return [(Mouse_x,Mouse_y)]
    else:
        # sinon on ne renvoi rien
        print("pas d'arbre a l'emplacement choisi")
        return None 
            

"""
----------------------------------------
Nom de la Fonction: ChangeArbre
paramètres:
    tableauPositions -> les nouvelles cases à faire changer d'état 
    tableauArbre -> le tableau complet d'arbre
    DISPLAY
    COLOR
    STATEPROPAGE
    STATEAFTER
but: Grâce à une liste donné, elle regarde au tour de chaqsue positions si l y a une case pour se propager (STATEPROPAGE) et remplace cette case
par un autre état (STATEAFTER) 
elle renvoie aussi la nouvelle liste de positions à bruler et se rapelle elle même 
----------------------------------------
"""
def ChangeArbre(tableauPositions,tableauArbre,DISPLAY,COLOR,STATEPROPAGE,STATEAFTER):
    

    newPosition = []
    positionChange = False
    global nbArbreBrule
    # pour toutes les nouvelles cases
    for i in range (len(tableauPositions)):
        # on récupère les positions x et y de chaques cases une par unes 
        (position_x,position_y) = tableauPositions[i]
        pygame.draw.rect(DISPLAY,COLOR, ((position_x)*25,0 + position_y*25, 25,25))

        tableauArbre[position_x][position_y] = STATEAFTER

        # on regarde à droite si il y a une case pour se propager 
        if (position_x < len(tableauArbre) - 1 and tableauArbre[position_x + 1][position_y] == STATEPROPAGE):
            newPosition.append([position_x + 1,position_y])
            tableauArbre[position_x + 1][position_y] = STATEAFTER
            
            positionChange = True
            if (COLOR == (255,0,0)):
                nbArbreBrule = nbArbreBrule + 1
        # on regarde en haut si il y a une case pour se propager 
        if (position_y < len(tableauArbre[position_x]) - 1 and tableauArbre[position_x][position_y + 1] == STATEPROPAGE):    
            tableauArbre[position_x][position_y + 1] = STATEAFTER
            newPosition.append([position_x,position_y + 1])
            positionChange = True
            if (COLOR == (255,0,0)):
                nbArbreBrule = nbArbreBrule + 1
        # on regarde à gauche si il y a une case pour se propager 
        if (position_x > 0 and tableauArbre[position_x - 1][position_y] == STATEPROPAGE):
            tableauArbre[position_x - 1][position_y] = STATEAFTER
            newPosition.append([position_x - 1,position_y])
            positionChange = True
            if (COLOR == (255,0,0)):
                nbArbreBrule = nbArbreBrule + 1
        # on regarde en bas si il y a une case pour se propager 
        if (position_y > 0 and tableauArbre[position_x][position_y - 1] == STATEPROPAGE):
            tableauArbre[position_x][position_y - 1] = STATEAFTER
            newPosition.append([position_x,position_y - 1])
            positionChange = True
            if (COLOR == (255,0,0)):
                nbArbreBrule = nbArbreBrule + 1
    # test pour vérifier si on a bien changer quelque chose
    if (positionChange == True):
        return newPosition
    else:
        return False
        

            

"""
----------------------------------------
Nom de la Fonction: onEnd
paramètres: pas de paramètres 
but: Afficher les statistiques du joueur et relancer le jeu si le joueur le souhaite.
----------------------------------------
"""
def onEnd():
    global nbArbreTotal
    global nbArbreBrule
    print("---------STATISTIQUE---------")
    print("Arbre Qu'il y avait au départ au total : ",nbArbreTotal)
    print("Arbre Brulé au total : ",nbArbreBrule)
    score = round((nbArbreBrule / nbArbreTotal) * 100)
    print("Votre Score est",score,"(le maximimum est 100)")
    if (score <= 10):
        print("Bravo! Vous avez sauvé la forêt !")
    if (score >= 90):
        print("Bravo! Vous avez détruit la forêt!")
    PlayerChoice()
    
"""
----------------------------------------
Nom de la Fonction: PlayerChoice
paramètres: pas de paramètres 
but: demandez si le joueur veut rejouer ou non, si oui rapellez la fonction Main
----------------------------------------
"""
def PlayerChoice():
    try:
        choix = str(input("Voulez vous rejouez? ( O / N) "))
        if (choix == "O"):
            Main()
        else:
            if (choix == "N"):
                print("Merci d avoir joué !")
            else:
                print("Veuillez rentrer O ou N pour faire votre choix")
                PlayerChoice()
    except:
            print("Veuillez rentrer O ou N pour faire votre choix")
            PlayerChoice()
        

"""
----------------------------------------
Nom de la Fonction: Main
paramètres: pas de paramètres 
but: executez toutes les fonctions et ainsi permettre de relancer le jeu
----------------------------------------
"""
def Main():
    print("---------------------------------------------BIENVENUE DANS SIMULATION DE FEU DE FORET!---------------------------------------------")
    print("Pour jouer, rentrez d'abbord la taille de la carte, puis cliquez avec la souris pour mettre le feu à un arbre")
    print("puis à la forêt! Votre but est de détruite le plus d'arbre possible! Choisissez donc bien ou commencer à mettre le feu")
    print("------------------------------------------------------------------------------------------------------------------------------------")



    global nbArbreTotal, nbArbreBrule, VIDE, ARBRE, CENDRE
    nbArbreTotal = 0
    nbArbreBrule = 0

    # les choix du joueur
    xMax,yMax = ChoixTaille()
    speed = ChoiceSpeed()
    pourcent = ChoicePourcent()

    # construction des talbleaux et de pygame  
    tableauVide = ConstructionTableauVide(xMax,yMax)
    tableauArbre = ConstructionArbreAleatoire(tableauVide,pourcent)
    DISPLAY = Start(tableauArbre,xMax,yMax)

    # position de la souris
    positionPremierArbre = None
    positionPremierArbre = MouseChoice(tableauArbre,(255,0,0),xMax,yMax,DISPLAY)
    while positionPremierArbre == None:
        # tant qu'on a pas de position de souris correcte ( ou il y a un arbre ) on ré execute la fonction 
        positionPremierArbre = MouseChoice(tableauArbre,(255,0,0),xMax,yMax,DISPLAY)

    # c'est ici qu'on régule le temps d'attente entre chaque cases qui changent d'état 
    fin = False
    # on récupère la première position de la souris 
    newPosFeu = positionPremierArbre
    newPosCendre = positionPremierArbre
    newPosBlanc = positionPremierArbre
    # ici step permet d'executer la fonction ChangeArbre pour brule, cendre et vide avec un temps de décalage entre chaque une  
    step = 0
    # le tout premier arbre qu'on brule 
    nbArbreBrule = nbArbreBrule + 1
    while fin == False:
        # on redonne a chaque fois les nouvelles cases a faire changer d'état 
        if (newPosFeu != False):
            newPosFeu = ChangeArbre(newPosFeu,tableauArbre,DISPLAY,(255,0,0),ARBRE,BRULE)
        if (newPosCendre != False and step > 0):
            newPosCendre = ChangeArbre(newPosCendre,tableauArbre,DISPLAY,(152,152,152),BRULE,CENDRE)
        if (newPosBlanc != False and step > 1):
            newPosBlanc = ChangeArbre(newPosBlanc,tableauArbre,DISPLAY,(255,255,255),CENDRE,VIDE)
        step = step + 1
        # c'est cette fonction qui permet d'attendre 
        pygame.time.wait(speed)
        pygame.event.pump()
        pygame.display.update()
        # la fin du programme
        if (newPosBlanc == False):
            fin = True
    onEnd()   


#0 = vide
#1 = arbre
#2 = bruler
#3 = cendre
VIDE = 0
ARBRE = 1
BRULE = 2
CENDRE = 3
# appel de la fonction principale 
Main()


