def tic_tac_toe_neu():
    Spielfeld = ["", "", "",
                 "", "", "",
                 "", "", ""]

    aktueller_spieler = "X"
    zug_liste = []
    zug = 0

    def spieler_zieht():
        nonlocal zug
        print("Aktueller Spieler:" + aktueller_spieler)
        while True:
            try:
                feld = int(input("In welches Feld von 1 - 9?"))
            except ValueError:
                print("Bitte eine Zahl")
                continue

            if feld in range(1, 10):
                if Spielfeld[feld-1] == "":
                    Spielfeld[feld-1] = aktueller_spieler
                    zug_liste.append(feld - 1)
                    zug = zug + 1
                    break

                else:
                    print("Feld belegt")

            else:
                print("Feld existiert nicht")

    def spieler_wechsel():

        nonlocal aktueller_spieler

        if aktueller_spieler == "X":
            aktueller_spieler = "O"
        else:
            aktueller_spieler = "X"

    def spieler_gewinnt():
        liste_möglichkeiten = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                               [0, 3, 6], [1, 4, 7], [2, 5, 8],
                               [0, 4, 8], [2, 4, 6]]
        for kombination in liste_möglichkeiten:
            a = Spielfeld[kombination[0]]
            b = Spielfeld[kombination[1]]
            c = Spielfeld[kombination[2]]

            if a == b == c and a != "":
                return a

    def zeige_Spielfeld():

        print(Spielfeld[0] + " | " + Spielfeld[1] + " | " + Spielfeld[2])
        print("--------------------------------")
        print(Spielfeld[3] + " | " + Spielfeld[4] + " | " + Spielfeld[5])
        print("--------------------------------")
        print(Spielfeld[6] + " | " + Spielfeld[7] + " | " + Spielfeld[8])

    while True:
        zeige_Spielfeld()
        spieler_zieht()
        gewinn = spieler_gewinnt()
        if gewinn == "X" or gewinn == "O":
            print(f"Spieler {gewinn} hat gewonnen")
            zeige_Spielfeld()
            break
        elif gewinn is None and "" not in Spielfeld:
            print("Unentschieden")
            zeige_Spielfeld()
            break

        if zug >= 6:
            Spielfeld[zug_liste[0]] = ""
            zug_liste.pop(0)
        spieler_wechsel()
