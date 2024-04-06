import Affichage as a



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nom_txt = "A8-1.txt"
    tableau = a.recup_info(nom_txt) #Créer le tableau de base

    for ligne in tableau: #Affichage
        print(ligne)
    print("\n\n")


    if(not a.is_Complet(tableau)): # Détermine si c'est pas complet et le complete
        a.Completion(tableau)


    for ligne in tableau: #Affichage
        print(ligne)


    entrees = a.les_entrees(nom_txt) # Prends les entrées
    sorties = a.les_entrees(nom_txt)

    if (not a.is_Standart(tableau, entrees)):
        tab = a.Standardisation(tableau, entrees)
    print("\n\n")
    for ligne in tableau:  # Affichage
        print(ligne)


    print("\n\n")
    for ligne in tableau: #Affichage
        print(ligne)
    print(entrees)
    print(a.is_Determinist(tableau,entrees))

    print(a.Determinisation(tableau,entrees,sorties))

    """
    print(a.is_Standart(tableau,entrees)) # Détermine si c'est standardisé

    if(not a.is_Standart(tableau,entrees)):
        tab = a.Standardisation(tableau, entrees)

    """









