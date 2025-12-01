import Tic_Tac_Toe
import Tic_Tac_Toe_Neu

while True:
    while True:
        try:
            print("Welche Version?")
            print("Version 1: klassisch oder Version 2: Neu")
            wahl = int(input("Deine Wahl: "))

        except ValueError:
            print("Bitte eine Zahl")
            continue

        if wahl == 1:
            Tic_Tac_Toe.basic_tic_tac_toe()
            break

        elif wahl == 2:
            Tic_Tac_Toe_Neu.tic_tac_toe_neu()
            break

        else:
            print("Falsche Eingabe")

    neue_runde = input("Nochmal spielen? (j/n)")
    if neue_runde == "n":
        print("Danke fürs spielen")
        break
    elif neue_runde == "j":
        print("Neue Runde")
    else:
        print("Eingabe Falsch; Bitte nur (j/n) antworten")
