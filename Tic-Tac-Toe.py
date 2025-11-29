Spielfeld = ["", "", "",
             "", "", "",
             "", "","" ]

aktueller_spieler = "X"




def spieler_zieht():
    try:
        feld = int(input("In welches Feld von 1 - 9?"))
    except ValueError:
        print("Bitte eine Zahl")
        spieler_zieht()
    if feld in range(1, 10):
        if Spielfeld[feld-1] == "":
            Spielfeld[feld-1] = aktueller_spieler

        else:
            print("Feld belegt")
            spieler_zieht()
    else:
        print("Feld existiert nicht")
        spieler_zieht() 





def spieler_wechsel():

    global aktueller_spieler

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
            print(f"Aktueller Spieler {a} gewinnt")
            return a



def zeige_Spielfeld():

    print(Spielfeld[0] + " | " + Spielfeld[1] + " | " + Spielfeld[2])
    print("--------------------------------")
    print(Spielfeld[3] + " | " + Spielfeld[4] + " | " + Spielfeld[5]) 
    print("--------------------------------")   
    print(Spielfeld[6] + " | " + Spielfeld[7] + " | " + Spielfeld[8])         

   




while True:
    spieler_zieht()
    zeige_Spielfeld()
    gewinn = spieler_gewinnt()
    if gewinn == "X" or gewinn == "O":
        print(f"Spieler {gewinn} hat gewonnen")
        break
    elif gewinn is None and "" not in Spielfeld:
        print("Unentschieden")
        break
    spieler_wechsel()
