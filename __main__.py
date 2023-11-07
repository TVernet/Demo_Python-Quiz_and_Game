from redirection import redirection
from game.gameplay import Gameplay
from quiz.quizplay import Quizplay


if __name__ == "__main__":
    # récupération du nom de l'utilisateur
    user_identity = input("Bonjour ! \nQuel est votre nom ? \n").lower()
    if user_identity == "":
        user_identity = input("Vous devez saisir votre nom, recommencez : ").lower()
    else:
        print(f"Bienvenue {user_identity}, commençons ! \n")

    # choix entre lancement du jeu ou lancement du quiz
    user_selec = input(
        f"Que voulez-vous faire {user_identity} ? Vous choisissez le jeu ou le quiz : \n"
    ).lower()
    if "jeu" in user_selec:
        G = Gameplay()
        G
    elif "quiz" in user_selec:
        Q = Quizplay
        Q.play(self=Q)

    # options de redirection de l'utilisateur
    redirection()

    print("Bonne journée !")
    quit()
