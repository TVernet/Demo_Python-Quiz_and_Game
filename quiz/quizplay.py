import random

from quiz.quiz_dict import quiz_dict  # questions et réponses du quiz


class Quizplay:
    def __init__(self) -> str:
        pass

    # gestion aléatoire des questions/réponses
    def get_random_question(self):
        self.question = random.choice(list(quiz_dict.keys()))
        self.user_enter = input(self.question).lower()
        self.correct_answer = quiz_dict[self.question]

    # explication des règles à l'utilisateur
    def get_rules(self):
        print(
            "Bienvenue dans le quiz, il y a 10 questions et vous devez atteindre le score de 5 "
            "points pour remporter la partie. A vous de jouer ! \n"
        )

    # définition du comportement attendu  
    def play(self):
        self.get_rules(self)
        self.points = 0
        while self.points < 5:
            self.get_random_question(self)
            if self.user_enter == self.correct_answer:
                self.points += 1
                del quiz_dict[self.question]
                print(f"\nvous avez à présent {self.points} pts \n")
            else:
                print(f"\nvous avez toujours {self.points} pts \n")
        print(f"\nBravo ! vous avez {self.points} pts, vous avez gagné \n")
