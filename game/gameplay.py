from game.game_dict import game_dict


class Gameplay:
    def __init__(self) -> str:
        # choix du personnage
        self.character = input(
            "\nBienvenue dans Tif World ! Choisissez votre personnage : \n* le renard : "
            "pouvoir, boules de feu - faiblesse, tendance à s'endormir faute d'énergie \n* "
            "le poulpe : pouvoir, vitesse supersonique - faiblesse, tendance à glisser en "
            "se blessant \n* l'opossum : pouvoir, distorsion du temps - faiblesse, tendance"
            " à se perdre dans le temps \n"
        ).lower()
        if "renard" in self.character:
            self.renard()
        elif "poulpe" in self.character:
            self.poulpe()
        elif "opossum" in self.character:
            self.opossum()

    # personnage du renard
    def renard(self):
        print(game_dict["intro"])
        input(game_dict["renard_char"]).lower()
        if "utilis" in game_dict["renard_char"]:
            input(game_dict["renard_use"]).lower()
            if "prend" in game_dict["renard_use"]:
                print(game_dict["renard_take"])
                pass
            elif "assum" in game_dict["renard_use"]:
                print(game_dict["renard_assume"])
                pass
            else:
                return game_dict["renard_use"]
        elif "attend" in game_dict["renard_char"]:
            input(game_dict["renard_waits"]).lower()
            if "sieste" in game_dict["renard_waits"]:
                print(game_dict["renard_sieste"])
                pass
            elif "continu" in game_dict["renard_waits"]:
                print(game_dict["renard_continued"])
                pass
            else:
                return game_dict["renard_waits"]
        else:
            return game_dict["renard_char"]

    # personnage du poulpe
    def poulpe(self):
        print(game_dict["intro"])
        input(game_dict["poulpe_char"]).lower()
        if "utilis" in game_dict["poulpe_char"]:
            input(game_dict["poulpe_use"]).lower()
            if "nargu" in game_dict["poulpe_use"]:
                print(game_dict["poulpe_taunt"])
                pass
            elif "concentr" in game_dict["poulpe_use"]:
                print(game_dict["poulpe_concentrate"])
                pass
            else:
                return game_dict["poulpe_use"]
        elif "attend" in game_dict["poulpe_char"]:
            input(game_dict["poulpe_waits"]).lower()
            if "activ" in game_dict["poulpe_waits"]:
                print(game_dict["poulpe_activate"])
                pass
            elif "continu" in game_dict["poulpe_waits"]:
                print(game_dict["poulpe_continued"])
                pass
            else:
                return game_dict["poulpe_waits"]
        else:
            return game_dict["poulpe_char"]

    # personnage de l'opossum
    def opossum(self):
        print(game_dict["intro"])
        input(game_dict["opossum_char"]).lower()
        if "teleport" in game_dict["opossum_char"]:
            print(game_dict["opossum_teleportation"])
            pass
        elif "téléport" in game_dict["opossum_char"]:
            print(game_dict["opossum_teleportation"])
            pass
        elif "envo" in game_dict["opossum_char"]:
            input(game_dict["opossum_send"]).lower()
            if "ralent" in game_dict["opossum_send"]:
                print(game_dict["opossum_slow_down"])
                pass
            elif "savour" in game_dict["opossum_send"]:
                print(game_dict["opossum_enjoy"])
                pass
            else:
                return game_dict["opossum_send"]
        else:
            return game_dict["opossum_char"]
