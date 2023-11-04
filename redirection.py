from game.gameplay import Gameplay
from quiz.quizplay import Quizplay

# options de redirection de l'utilisateur
def redirection():
    options = ["quitter", "jeu", "quiz"]
    user_choice = input(
        "\nQue voulez-vous faire ?\n* Quitter \n* Faire le jeu\n* Faire " "le quiz \n"
    ).lower()
    while not user_choice in options:
        user_choice = input(
            "\nQue voulez-vous faire ?\n* Quitter \n* Faire le jeu\n* "
            "Faire le quiz\n"
        ).lower()

    # option fin
    if "quitter" in user_choice:
        print(
            f"""
                    FIN 
                    Merci pour votre participation et à bientôt !
                """
        )
        exit()

    # option jeu
    elif "jeu" in user_choice:
        G = Gameplay()
        G
        return redirection()

    # option quiz
    elif "quiz" in user_choice:
        Q = Quizplay
        Q.play(self=Q)
        return redirection()
