# BatailleNavalePython

Jeu de bataille navale : un joueur, joue contre l'ordinateur, et doit faire en sorte de toucher, puis couler les navires. La partie s'arrête lorsqu'il a coulé tous les navires.

Le jeu comportera une grille de 10x10 cases sur lesquelles les bateaux seront placés.

V1.0

Pas de grille : le joueur joue, en tentant de trouver les coordonnées des bateaux placés par l'ordinateur (sans aléatoire).
Les coordonnées consistent en des dictionnaires python, contenant en clé les coordonnées, et en valeur, l'état de la case (coordonnée) correspondante.
Par défaut, l'état de la case est paramétré à False. Si elle contient un navire, elle passe a True.
Lorsque le joueur tire, deux cas possibles :

- soit la case est déjà False = tir manqué,
- Soit la case est en True = alors le navire est touché

Le joueur coule un navire dès lors que toutes les cases adjacentes passent de True à False. Il gagne la partie dès lors qu'il n'existe plus de case marquée "True".

Objectif : gagner en un minimum de tirs possuble.

