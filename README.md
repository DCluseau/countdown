# Le compte est bon - Countdown

## Sommaire

- [Principe du programme](#principe-du-programme)
- [Règles du jeu](#règles-du-jeu)
- [Manuel d'utilisation](#manuel-d-utilisation)

## Principe du programme

Le programme permet à l’utilisateur de jouer à ce jeu célèbre. Il tire au sort un nombre à obtenir entre 101 et 999, ainsi que 6 plaques – portant un nombre – tirés parmi 24 réparties ainsi : chaque nombre de 1 à 10 est présent 2 fois, et les nombres 25, 50, 75 et 100 sont présents en un seul exemplaire.
A chaque tour de jeu, l’utilisateur sélectionne une opération (addition, soustraction, multiplication, division) et 2 nombres parmi les plaques restantes et les nombres (restants) obtenus lors des opérations précédentes. L’opération appliquée à ces nombres (qui ne sont alors plus utilisables) fournit alors un nouveau nombre.
L’utilisateur peut, quand il estime ne pas pouvoir se rapprocher davantage du nombre à obtenir, indiquer qu’il souhaite arrêter le jeu (en indiquant si besoin quel nombre parmi ceux obtenus et restants est le nombre qu’il a obtenu), celui-ci s’arrêtant également lorsqu’il ne reste plus de plaque disponible et un seul nombre résultant d’opérations.
Le programme indique alors à l’utilisateur si « le compte est bon » (le nombre à obtenir a été atteint) ou s’il n’a obtenu qu’un nombre approchant le nombre à obtenir.

## Déroulement du jeu

- Le programme génère six nombres aléatoires (de 1 à 10, ils peuvent être en double, et 25, 50, 75 et 100 sont uniques).
- Le programme génère un nombre entre 101 et 999.
- Le programme affiche le nombre à calculer et la liste des nombres tirés
- Lors du premier tour, le programme demande deux fois au joueur de sélectionner un nombre dans les nombres tirés puis il demande de sélectionner l'opérateur.
- Le programme calcule l'opération à faire, affiche le résultat et enlève les chiffres utilisés de la liste
- Pour les tours suivants, le programme demande dans quelle liste le joueur veut utiliser un nombre, deux fois, ainsi que l'opérateur, puis calcule et affiche le nouveau résultat, toujours en supprimant les chiffres utilisés.
- Le programme demande au joueur si il veut continuer. Si oui, il continue en boucle l'opération précédente jusqu'à ce que le joueur indique qu'il veut arrêter.
- Si il ne reste plus qu'un nombre ou si le joueur indique qu'il veut arrêter, le programme affiche le résultat calculé ainsi que le nombre qu'il fallait calculer.
- Si le nombre calculé est égal à celui qu'il fallait calculer, le programme félicite le joueur. Sinon, il écrit "Presque !"

## Manuel d'utilisation

- Installez Python 3
- Lancer le fichier countdown.py dans la console
- Attendre les instructions du programme
- Lorsque le programme demande au joueur d'entrer quelque chose, il faut bien suivre les indications :
  - Saisir 1 ou 2 quand on doit choisir entre deux listes ou pour continuer ou non le jeu.
  - Saisir un nombre qui existe dans les listes présentées.
  - Saisir un opérateur comme ceux présentés par le programme.
- Appuyez sur la touche Entrée pour valider votre saisie