#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# la grille de jeu virtuelle est composée de 10 x 10 cases
# une case est identifiée par ses coordonnées, un tuple (no_ligne, no_colonne)
# un no_ligne ou no_colonne est compris dans le programme entre 1 et 10,
# mais pour le joueur une colonne sera identifiée par une lettre (de 'A' à 'J')

valid_coord = False
shot_coord = None  # pour éviter un avertissement ("can be undefined")
GRID_SIZE = 10

# détermination de la liste des lettres utilisées pour identifier les colonnes :
LETTERS = "ABCDEFGHIJ"

# chaque navire est constitué d'un dictionnaire dont les clés sont les
# coordonnées de chaque case le composant, et les valeurs correspondantes
# l'état de la partie du navire correspondant à la case
# (True : intact ; False : touché)

# les navires suivants sont disposés de façon fixe dans la grille :
#      +---+---+---+---+---+---+---+---+---+---+
#      | A | B | C | D | E | F | G | H | I | J |
#      +---+---+---+---+---+---+---+---+---+---+
#      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
# +----+---+---+---+---+---+---+---+---+---+---+
# |  1 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  2 |   | o | o | o | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  3 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  4 | o |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  5 | o |   | o |   |   |   |   | o | o | o |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  6 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  7 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  8 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  9 |   |   |   |   | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# | 10 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
aircraft_carrier = {(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True}    # porte_avion en B2
cruiser = {(4, 1):True, (5, 1): True, (6, 1): True, (7, 1): True}  # croiseur en A4
destroyer = {(5, 3): True, (6, 3):True, (7, 3):True}  # contre_torpilleur en C5
submarine = {(5, 8):True, (5,9):True,(5,10):True}  # sous_marin en H5
torpedo_boat = {(9,5):True, (9,6):True}  # torpilleur en E9
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

SEA, MISSED_SHOT, HIT_SHOT, SUNK_SHOT = 0, 1, 2, 3
# l'embryon de notre jeu consiste à demander à l'infini au joueur les coordonnées
# d'un tir, puis à indiquer si ce tir touche un navire (en mémorisant les conséquences
# de ce tir, indiquant si le navire est coulé à la suite de plusieurs tirs convergents,
# et si la partie est finie lorsque le dernier navire est coulé)

#Génération du plateau de jeu


#Fonction qui crée une grille, avec des caractères pour représenter chaque case.

def create_board(GRID_SIZE):
    board = []
    for _ in range(GRID_SIZE):
        row = ["[]"] * GRID_SIZE
        board.append(row)
    return board


#Fonction qui affiche une grille.
def display_board(board):
    for row in board:
        print(" ".join(row))
        letter = LETTERS[x]
        print(' {}  '.format(letter), end='')
    return board


#Fonction qui permet de demander à l'utilisateur une coordonnée pour tirer..
def ask_coord():

    is_valid = False
    shot = None

    player_coord = input("Entrez les coordonnées de votre tir (ex. : 'A1', 'H8') : ")

    # ex. d'entrée attendue : 'A1'
    if 2 <= len(player_coord) <= 3:

        letter, number = player_coord[0], player_coord[1:]
        letter = letter.upper()

        try:
            # détermination de line_no et column_no (comptés à partir de 1)
            line_no = int(number)
            column_no = ord(letter) - ord('A') + 1

            if 1 <= line_no <= GRID_SIZE and letter in LETTERS:
                is_valid = True
                shot = (line_no, column_no)
        except ValueError:
            print(f"Erreur : coordonnées invalides ou en dehors de la grille.")
        return shot, is_valid


def ship_is_hit(ship, shot_coord):
    if shot_coord in ship:

        print('Un navire a été touché par votre tir !')
        # on mémorise ce tir
        ship[shot_coord] = False

    return shot_coord


def ship_is_sunk(ship):
    if True not in ship.values():
        is_sunk = False
        print('Le navire touché est coulé !!')
        # le navire est supprimé de la flotte
        ships_list.remove(ship)
        return is_sunk

#create_board()
#display_board()


while ships_list:

    # on demande des coordonnées au joueur tant qu'il n'en fournit pas de valides
    # (ex. : 'A1', 'H8'), puis on les transforme en des coordonnées du programme :
    # tuple (no_ligne, no_colonne)

    while not valid_coord:

        ask_coord()

    # on regarde à présent si le tir en coord_tir touche un navire
        for ship in ships_list:

            ship_is_hit(ship, shot_coord)
            ship_is_sunk(ship)

            break
        else:
            print("Votre tir est tombé dans l'eau")

    print('Bravo, vous avez coulé tous les navires')
    break

#Partie 2 : se focaliser sur les fonctions et les itérables.