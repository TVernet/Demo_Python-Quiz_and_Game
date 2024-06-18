# Le projet

Dans le processus de ma reconversion, "Quiz and Game" fut le premier projet créé pour appréhender la programmation.
L'objectif de ce projet était de me permettre de tester quelques notions de base d'un langage interprété comme celui-ci.

Ce script prévoit une interaction utilisateur en interface de ligne de commande pouvant conduire à expérience de jeu de type "personnage dont vous êtes le héros" ou une expérience de quiz portant sur 10 questions de type "Vrai ou Faux".

## Son arborescence :  

- Le répertoire `Game` comprend l'ensemble des données nécessaire au choix utilisateur "jeu"  
    - Le fichier `game_dict` est le dictionnaire qui stock les données et actions des personnages     
    - Le fichier `gameplay` gère l'arborescence des actions du joueur
- Le répertoire `Quiz` comprend l'ensemble des données nécessaire au choix utilisateur "quiz"  
    - Le fichier `quiz_dict` est le dictionnaire qui stock les données du quiz       
    - Le fichier `quizplay` gère l'itération des questions et leur validation     
- Le fichier `__main__.py` fournit l'ensemble des appels de base   
- Le fichier `redirection` gère les choix de navigation de l'utilisateur      
 
