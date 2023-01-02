import random

"""
la classe Pion correspond a chaque pion qu'on mettre dans une liste
"""
class Pion:

    """
    C'est le constructeur de la classe Pion
    Quand on ajoute un pion, on lui donne un nom d'équipe pour pouvoir l'identifier 
    """
    def __init__(self, new_team):
        self.equipe = new_team


    """
    Retourne le nom de l'équipe du pion
    """
    def get_team(self):
        return self.equipe


    """
    Methode qui renvoi X ou O selon l'équipe
    On n'utilise pas str() car on veut renvoyer un str, pas l'afficher
    """
    def printPion(self):
        if self.equipe == "team1":
            return "O"
        else:
            return "X"



            



"""
La classe PilePion contient une liste de pion, correspondant a une colonne du puissance 4
"""
class PilePion:

    def __init__(self):
        # on défitinit la liste de pion
        self.liste_pion = []
    

    """
    Cette Methode sert à copier en mémoire la liste
    """
    def copieListePion(self):
        # on créer une nouvelle classe PilePion
        result = PilePion()
        for i in self.liste_pion:
            # on ajoute tout les éléments de la pile actuelle
            result.push(i.equipe)
        return result

    
    """
    Methode classique d'une pile
    Elle renvoie en plus d'ajouter un pion, si on a pu l'ajouter ou non, sous forme de bool 
    """
    def push(self, nom_equipe):
        new_pion = Pion(nom_equipe)
        if (not self.verif_top()):
            return False
        self.liste_pion.append(new_pion)
        return True

    
    """
    Methode classique d'une pile
    """
    def pop(self):
        if self.liste_pion != []:
            self.liste_pion.pop()
    

    """
    Methode permettant de savoir si on ne peut plus ajouter de pion.
    """
    def verif_top(self):
        if (len(self.liste_pion) == 6):
            return False
        return True


    def get_pile(self):
        return self.liste_pion


    """
    Methode permettant de vérifier si le y est dans la liste ou non
    """
    def verif_inList(self, index):
        if (index < 0):
            return False
        return index <= len(self.liste_pion) - 1


    """
    Methode pour obtenir le pion tout en haut
    """
    def get_top_value(self):
        return self.liste_pion[len(self.liste_pion) - 1]


    def get_liste_len(self):
        return len(self.liste_pion) - 1


    def is_empty(self):
        if len(self.liste_pion) == 0:
            return True
        return False


    """
    Methode qui renvoi le pion à cet index
    """
    def get_pion_value(self, index):
        return (self.liste_pion[index].printPion())


    """
    Methode qui renvoi le nom de l'équipe à cet index
    """
    def get_pion_team(self, index):
        return (self.liste_pion[index].get_team())

    """
    printListePion est une fonction de Debug, permettant d'afficher en une ligne tout les pions de la liste
    """    
    def printListePion(self):
        for i in range (len(self.liste_pion)):
            print(self.liste_pion[i].printPion(), end="")



"""
la classe Grille est la classe qui gère l'ajout de pions, l'affichage de la grille, les choix du joueur et de l'Ia
"""
class Grille:

    """
    Constructeur de la classe, c'est la ou on créer les 7 collones du puissance 4, représenter par une liste de Classe PilePion
    """
    def __init__(self):
        # la liste de pile
        self.liste_pile = []
        # ici on choisit aléatoirement quel joueur va jouer en premier
        """
        rng = random.randint(0, 1)
        if (rng == 0):
            self.current_player = "team1"
        else:
            self.current_player = "team2"
        """
        for i in range (7):
            new_pile = PilePion()
            self.liste_pile.append(new_pile)
        """
        self.liste_pile[1].push("team1")
        self.liste_pile[1].push("team2")
        self.liste_pile[1].push("team1")
        self.liste_pile[3].push("team2")
        self.liste_pile[3].push("team1")
        self.liste_pile[4].push("team1")
        self.liste_pile[4].push("team1")
        self.liste_pile[5].push("team1")
        self.liste_pile[5].push("team1")
        self.liste_pile[6].push("team2")
        self.liste_pile[6].push("team2")
        self.liste_pile[6].push("team1")
        """
        #self.liste_pile[3].push("team1")
        #self.liste_pile[4].push("team1")   
        #self.liste_pile[3].push("team2")     
        #self.liste_pile[3].push("team2")
        #self.liste_pile[2].push("team1")
        
        self.current_player = "team2"
        self.printGrille(self.liste_pile)
        self.choix_jeu()

    """
    C'est la méthode qui copie toute la grille en mémoire
    """
    @staticmethod
    def copieListPile(listePile):
        result = []
        for i in listePile:
            result.append(i.copieListePion())
        return result


    """
    choix_jeu est la méthode permettant de demander au joueur si on veut jouer avec un joueur ou un IA
    """
    def choix_jeu(self):
        # ce bool sert a looper tant que le joueur n'a pas choisi une réponse correcte 
        can_choose = False
        choix = -1
        while can_choose == False:
            try:
                choix = int(input("Voulez vous jouer avec une IA ou avec un joueur ? (0 pour PVP et 1 pour IA)"))
            except ValueError:
                print("Veuillez choisir un nombre")
            if choix == 0 or choix == 1:
                can_choose = True
            else:
                print("Veuillez choisir un nombre entre 0 et 1")
        # on apelle ensuite cette méthode permettant de jouer au jeu
        self.place_pion(choix)


    """
    Methode permettant de placer des pions 
    """
    def place_pion(self, choix_jeu):
        print("full normal")
        if self.full(self.liste_pile):
            # plus d'espace pour placer des pions 
            print("MATCH NULL")
            self.end_game()
            return
        choix = -1
        if choix_jeu == 0:
            #les joueur jouent tout par tour
            choix = self.place_pion_joueur()
        else:
            # joueur contre IA
            if self.current_player == "team1":
                # au joueur de jouer
                choix = self.place_pion_joueur()
            elif self.current_player == "team2":
                # a l'IA de jouer
                choix1 = self.place_pion_IA(self.liste_pile, 1)
                print(choix1)
                choix = choix1[0]
                print("choix de l'IA = ", choix)
                self.liste_pile[choix].push("team2")
                self.printGrille(self.liste_pile)
                
        # test pour savoir si un des deux joueurs a gagner 
        if (self.verif_win(choix, self.liste_pile[choix].get_liste_len(), self.current_player, self.liste_pile)):
            joueur_name = ""
            if (self.current_player == "team1"):
                joueur_name = "équipe 1"
            else:
                joueur_name = "équipe2"
            print("JEU TERMINER, le joueur gagnant est l'",joueur_name)
            if self.end_game() == True:
                # on veut rejouer
                play()
            else:
                # on veut arrêter :(
                return 

        #personne n'a gagner, on change le joueur et in rapelle la meme fonction récursivement 
        self.current_player = self.verif_joueur(self.current_player)
        self.place_pion(choix_jeu)


    """
    Methode qui sert à demander si on veut rejouer ou non
    """
    def end_game(self):
        can_choose = False
        choix = -1
        while can_choose == False:
            try:
                choix = int(input("voulez vous rejouer ? (0 pour oui et 1 pour non)"))
            except ValueError:
                print("Veuillez choisir un nombre entre 0 et 1")
            if choix == 0 or choix == 1:
                can_choose = True
            else:
                print("Veuillez choisir un nombre entre 0 et 1")
        if (can_choose == 0):
            return True
        else:
            return False


    """
    Methode qui renvoi le choix du joueur sur la colonne sur laquelle il veut jouer
    il ajoute le pion directement dans la fonction, mais renvoi le choix pour d'autre méthode
    """
    def place_pion_joueur(self):
        canPlay = False
        choix = -10
        joueur_name = ""
        if (self.current_player == "team1"):
            joueur_name = "équipe 1"
        else:
            joueur_name = "équipe2"
        print("le joueur qui joue en premier est l'",joueur_name)
        while canPlay == False:
            try:
                choix = int(input("On a demander la flotte ?"))
            except ValueError:
                print("Veuiller choisir un nombre")
            if 0 <= choix < 7:
                # la coordonée est bonne, on l'ajoute dans la liste QUE SI On ne se trouve pas au sommet
                canPlay = self.liste_pile[choix].push(self.current_player)
            else:
                print("Choisir une coordonées possible (entre 0 et 6)")
        #on affiche la grille
        self.printGrille(self.liste_pile)
        return choix


    def place_pion_IA(self, listeGrille, profondeur):
        liste_copie = self.copieListPile(listeGrille)
        #if (profondeur == 3):
        #    self.printGrille(liste_copie)
        coups_perdants = []
        coups_gagnants = []
        #print(profondeur)
        """
        __________________________
        PREMIERE PARTIE 
        __________________________
        """
        for choix_ordi in range (7):
            if (liste_copie[choix_ordi].push("team2")):
                # on peut le placer ( et on le fait !)
                # dans un premier temps on regarde si on peut gagner au prochain coup
                if (self.verif_win(choix_ordi, liste_copie[choix_ordi].get_liste_len(), "team2",  liste_copie)):
                    # on peut gagner :))
                    #print("WIN")
                    # self.printGrille(liste_copie)
                    liste_copie[choix_ordi].pop()
                    return choix_ordi, [], "WIN"
                # on ne peut pas gagner, on va donc regarder si en faisant notre coup, le joueur pourra gagner au prochain tour
                liste_copie[choix_ordi].pop()

        
        """
        __________________________
        DEUXIEME PARTIE 
        __________________________
        """
        nbr_coup_possible = 7
        liste_coup_possible = []
        liste_coup_non_perdant = []
        for choix_ordi in range (7):
            #(liste_copie[choix_ordi].printListePion())
            if (liste_copie[choix_ordi].push("team2")):
                liste_coup_possible.append(choix_ordi)
                for choix_player in range (7):
                    if (liste_copie[choix_player].push("team1")):
                        if (self.verif_win(choix_player, liste_copie[choix_player].get_liste_len(), "team1",  liste_copie)):
                            # la joueur va gagner si on joue ici
                            # # on essai donc un autre endroit  
                            if (choix_ordi not in coups_perdants):
                                coups_perdants.append(choix_ordi)
                                if (choix_ordi in liste_coup_non_perdant):
                                    liste_coup_non_perdant.remove(choix_ordi)
                            liste_copie[choix_player].pop()
                            nbr_coup_possible -= 1
                            break
                        else:
                            if (choix_ordi not in liste_coup_non_perdant and choix_ordi not in coups_perdants):
                                # parce que selon le choix joueur, il peut gagner ou perdre
                                liste_coup_non_perdant.append(choix_ordi)
                        # on enleve ce pion pour tester d'autre choix
                        liste_copie[choix_player].pop()
                liste_copie[choix_ordi].pop()

            else:
                #print("pas possible")
                nbr_coup_possible -= 1
        if (liste_coup_possible == []):
            print("None", liste_coup_possible)
            return (None, None, None)
        if (nbr_coup_possible == 0):
            #print("Config Lost", coups_perdants, profondeur)
            return (coups_perdants[random.randint(0,len(coups_perdants) - 1)], coups_perdants, "LOST")
        if (nbr_coup_possible == 1):
            #return (liste_coup_possible[0], coups_perdants, "NEXT")
            return (liste_coup_non_perdant[0], coups_perdants, "NEXT")

        #3eme phase
        if (profondeur == 3):
            if (len(liste_coup_non_perdant) > 0):
                
                meilleur_coup = -1
                index_meilleur_coup = -1
                for i in range(len(liste_coup_non_perdant)):
                    possible_coup = self.best_choice_IA(liste_coup_non_perdant[i],liste_copie[i].get_liste_len(), liste_copie)
                    if possible_coup > meilleur_coup:
                        index_meilleur_coup = liste_coup_non_perdant[i]
                        meilleur_coup = possible_coup


                #print("__________________________________   cas 1")
                #self.printGrille(liste_copie)
                #print("index_meilleur_coup = ", index_meilleur_coup, liste_coup_non_perdant)
                #print("__________________________________")

                return (index_meilleur_coup, coups_perdants, "NEXT") 
            return (liste_coup_possible[random.randint(0, len(liste_coup_possible)-1)] , coups_perdants, "NEXT") 
        


        """
        __________________________
        TROISIEME PARTIE 
        __________________________
        """
        liste_bof = []
        if (len(liste_coup_non_perdant) > 7):
            print((liste_coup_non_perdant))
        #if (profondeur == 1):

        # print(liste_coup_non_perdant, profondeur)
        #self.printGrille(liste_copie)
        #print("test de la grille")
        for choix_ordi in (liste_coup_non_perdant):
            # on rapelle la fonction récursivement pour les coups ou on ne perds pas
            liste_copie[choix_ordi].push("team2")
            for choix_player in range(7):
                liste_copie[choix_player].push("team1")
                #if (choix_ordi == 4):
                    #print("test coup ordi ", choix_ordi)
                    #self.printGrille(liste_copie)
                resultat = self.place_pion_IA(liste_copie, profondeur + 1)
                # if (profondeur == 1):
                    # print ("RESULT PREM APPEL", choix_ordi, choix_player, resultat)
                if (resultat[2] == "WIN"):
                    liste_copie[choix_player].pop()
                    #liste_copie[choix_ordi].pop()
                    #return (choix_ordi, coups_perdants, "WIN")
                    # On ajoute aux coups gagant a condition que ce coup ne donne pas une defaite
                    if (choix_ordi not in coups_gagnants and choix_ordi not in coups_perdants):
                        coups_gagnants.append(choix_ordi)

                elif (resultat[2] == "LOST"):
                    liste_copie[choix_player].pop()
                    if (choix_ordi not in coups_perdants):
                        coups_perdants.append(choix_ordi)
                    if (choix_ordi in liste_bof):
                        # on retire quelque chose
                        liste_bof.remove(choix_ordi)
                    if (choix_ordi in coups_gagnants):
                        coups_gagnants.remove(choix_ordi)
                    break
                else:
                    liste_copie[choix_player].pop()
                    if (choix_ordi not in coups_perdants and choix_ordi not in liste_bof):
                        liste_bof.append(choix_ordi) 
                        #if (choix_ordi == 2):
                            #print("append du choix BOGF 2 =============================", liste_bof)
            liste_copie[choix_ordi].pop()

        if (coups_gagnants != []):
            meilleur_coup_gagnant = -1
            index_meilleur_coup_gagnant = -1
            for i in range (len(coups_gagnants)):
                possible_coup = self.best_choice_IA(coups_gagnants[i],liste_copie[i].get_liste_len(), liste_copie)
                if possible_coup > meilleur_coup_gagnant:
                    meilleur_coup_gagnant = possible_coup
                    index_meilleur_coup_gagnant = coups_gagnants[i]
            return (index_meilleur_coup_gagnant, coups_perdants, "NEXT")

        if (liste_bof != []):
            #print("choix parmio un bof", liste_bof, coups_perdants)
        
            meilleur_coup_bof = -1
            index_meilleur_coup_bof = -1
            for i in range (len(liste_bof)):
                possible_coup = self.best_choice_IA(liste_bof[i],liste_copie[i].get_liste_len(), liste_copie)
                if possible_coup > meilleur_coup_bof:
                    meilleur_coup_bof = possible_coup
                    index_meilleur_coup_bof = liste_bof[i]
            #print("__________________________________  cas 2")
            #self.printGrille(liste_copie)
            #print("index_meilleur_coup_bof = ", index_meilleur_coup_bof)
            #print("__________________________________")
            return (index_meilleur_coup_bof, coups_perdants, "NEXT")
        else:
            # on a que du LOST
            #print("que du lost ")
            return (coups_perdants[random.randint(0, len(coups_perdants) - 1)], coups_perdants, "LOST")
                    

    """
    Methode qui renvoi le score de cette coordonée
    """
    def best_choice_IA(self, x, y, listeGrille):
        vert, score1 = self.verification_ligne(x, y, 0, 1, "team2", listeGrille)
        horizon, score2 = self.verification_ligne(x, y, 1, 0, "team2", listeGrille) 
        diago1, score3 = self.verification_ligne(x, y, 1, 1, "team2", listeGrille)
        diago2, score4 = self.verification_ligne(x, y, 1, -1, "team2", listeGrille)
        return score1 + score2 + score3 + score4
            

    """
    Methode qui renvoi True ou False si le pion de l'équipe "team" a gagner (paramètre)
    """
    def verif_win(self, x_pos, y_pos, team, listePile):
        #print(x_pos, y_pos, team)
        vert, score1 = self.verification_ligne(x_pos, y_pos, 0, 1, team, listePile)
        horizon, score2 = self.verification_ligne(x_pos, y_pos, 1, 0, team, listePile) 
        diago1, score3 = self.verification_ligne(x_pos, y_pos, 1, 1, team, listePile)
        diago2, score4 = self.verification_ligne(x_pos, y_pos, 1, -1, team, listePile)
        if (vert or horizon or diago1 or diago2):
            # une des quatres direction est alignée
            return True


    def verification_ligne(self, x, y, moveX, moveY, team, listePile):
        #print("pos originaux = ", x, y, "direction = ",moveX, moveY)
        direction_x = moveX
        direction_y = moveY
        nbPion = 1
        all_pion = 1
        nbPossible = 1
        score = 0
        pos_x = x
        pos_y = y
        espace = False
        for i in range (10):
            pos_x += direction_x
            pos_y += direction_y
            #print(pos_x, pos_y)
            if self.verif_pos_in_list(pos_x, pos_y):
                if listePile[pos_x].verif_inList(pos_y) :
                    #print("inList")
                    if (listePile[pos_x].get_pion_team(pos_y) == team):
                        # c'est un pion allié
                        if (not espace):
                            nbPion += 1 
                        all_pion += 1        
                        nbPossible += 1
                        #print("nbPions =", nbPion)
                        #if (nbPion == 4):
                        #    return True
                    elif direction_x == moveX and direction_y == moveY:
                        #nbPion = 1
                        direction_x = direction_x * -1
                        direction_y = direction_y * -1
                        pos_x = x
                        pos_y = y
                        #print("Changement de sens, new X =", direction_x, "nouveau Y = ", direction_y)
                    else:
                        #print("fin des haricots")
                        break
                elif direction_x == moveX and direction_y == moveY:
                    nbPossible += 1
                    espace = True
                    #print("changemtn de sens car vide")
                    #nbPion = 1
                    #direction_x = direction_x * -1
                    #direction_y = direction_y * -1
                    #pos_x = x
                    #pos_y = y
                else:
                    # changement de sens + espace
                    espace = True
                    nbPossible += 1
                    #break
            elif direction_x == moveX and direction_y == moveY:
                    #print("changemtn de sens car fin tableau")
                    #nbPion = 1
                    espace = False
                    direction_x = direction_x * -1
                    direction_y = direction_y * -1
                    pos_x = x
                    pos_y = y
            else:
                break
        if (nbPossible >= 4):
            score = 100
        score += 1 * (10 ** (nbPion - 1))
        score += all_pion
        if (nbPion >= 4):
            return True, score
        return False, score


    """
    Methode qui vérifie si la grille est remplie 
    """
    def full(self, listeGrille):
        for i in listeGrille:
            # on vérifie chaque colonne
            if (i.verif_top()):
                return False
        return True

    """
    vérifie si on ne dépasse pas du tableau, avec x et y les coordonées testée 
    """
    def verif_pos_in_list(self, x, y):
        if (0 <= x < len(self.liste_pile) and 0 <= y < 6):
            return True
        return False


    """
    Methode qui échange le joueur actuelle avec l'autre
    """
    @staticmethod
    def verif_joueur(joueur_name):
        inter_name = joueur_name
        if (inter_name == "team1"):
            inter_name = "team2"
        elif (inter_name == "team2"):
            inter_name = "team1"
        return inter_name


    """
    Methode qui affiche la grille
    """
    def printGrille(self, grille):
    # on parcourt la liste
        for y in range (6):
            for x in range(len(grille)):
                # c'est pour obtenir le contraintre de l'index
                index = 5 - y
                if (grille[x].verif_inList(index)):
                    # DANS LA LISTE
                    pionValue = grille[x].get_pion_value(index)
                    print(pionValue, end="") 
                else:
                    # PAS DANS LE LISTE
                    print(" ", end="")
            # saut de ligne
            print("")
        
        # construction du repère de position
        for i in range (7):
            print(i,end="")
        print("")
        print("___________________________")
        




def play():
    # instation de grile
    print("_____________________________________________")
    print(" BIENVENUE DANS LE PUISSANCE 4 PYTHON EDITION")
    print("_____________________________________________")
    grille = Grille()

play()
