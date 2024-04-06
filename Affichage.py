


def recup_info(nom_txt):
    with open(nom_txt,"r") as f:
        contenu = f.readlines()

    nbr_lettre = int(contenu[0])
    nbr_etat = int(contenu[1])

    etat_init = []
    for i in range(int(contenu[2][0])):
        etat_init.append(contenu[2][2+i*2])

    etat_terminaux =[]
    for i in range(int(contenu[3][0])):
        etat_terminaux.append(contenu[3][2+i*2])

    nbr_transition = int(contenu[4][0])
    Etat = []
    for i in range(5, 5+nbr_transition): # Ressortir les Etats depuis les transitions
        lettre = contenu[i][0]
        if lettre not in Etat :
            Etat.append(lettre)
        lettre = contenu[i][2]
        if lettre not in Etat:
            Etat.append(lettre)

    Alphabet = []
    for i in range(5, 5 + nbr_transition): # Ressortir l'alphabet depuis les transitions
        lettre = contenu[i][1]
        if lettre not in Alphabet:
            Alphabet.append(lettre)


    tableau = [[' ']]

    for i in range(nbr_etat):
        tableau.append([Etat[i]])


    for i in range(nbr_lettre):
        tableau[0].append(Alphabet[i])
        for j in range(nbr_etat):
            tableau[j+1].append('')

    for i in range(int(contenu[3][0])):
        for j in range(nbr_etat):
            if Etat[j] == contenu[3][2 + i*2]:
                tableau[j+1][0] = "S-" + tableau[j+1][0]
                break


    for i in range(int(contenu[2][0])):
        for j in range(nbr_etat):
            if Etat[j] == contenu[2][2 + i*2]:
                tableau[j+1][0] = "E-" + tableau[j+1][0]
                break


    for i in range(nbr_etat): # Remplir le tabeleau
        for j in range(nbr_lettre):
            for k in range(5, 5 + nbr_transition):
                if contenu[k][1] == Alphabet[j] and Etat[i] == contenu[k][0]:
                    tableau[i+1][j+1] = tableau[i+1][j+1] + contenu[k][2]


    return tableau



def is_Complet(tab):
    for i in range(1,len(tab)): # Etat Poubelle
        for j in range(1,len(tab[0])):
            if tab[i][j] == '':
                return False
    return True


def Completion(tab):
    for i in range(1,len(tab)): # Etat Poubelle
        for j in range(1,len(tab[0])):
            if tab[i ][j] == '':
                tab[i][j] = 'P'
    tab.append(['P']*len(tab[0]))
    return tab


def les_entrees(nom_txt):
    with open(nom_txt,"r") as f:
        contenu = f.readlines()
    Entrees =[]
    for i in range(int(contenu[2][0])):
        e = contenu[2][2+i*2]
        Entrees.append(e)
    return Entrees


def les_sorties(nom_txt):
    with open(nom_txt,"r") as f:
        contenu = f.readlines()
    Sorties = []
    for i in range(int(contenu[3][0])):
        e = contenu[2][2+i*2]
        Sorties.append(e)
    return Sorties


def is_Standart(tab,entrees):

    for i in range(1,len(tab)):
        for j in range(1,len(tab[0])):
            if tab[i][j] in entrees:
                return False
    return True


def Standardisation(tab,entrees):
    tab.append(['E-I'])
    k=0
    for elt in entrees:
        for i in range(1,len(tab)):
            if elt in tab[i][0]:
                if k==0:
                    for j in range(1,len(tab[0])):
                        tab[len(tab)-1].append(tab[i][j])
                        k+=1
                else:
                    for j in range(1,len(tab[0])):
                        tab[len(tab)-1][j] = tab[len(tab)-1][j] + tab[i][j]

    for i in range(1,len(tab)-1):
        if 'E' in tab[i][0]:
            tab[i][0] = tab[i][0][2:]
    return tab


def is_Determinist(tab,entrees) :
    if len(entrees) > 1 :
        return False
    for i in range(1,len(tab)):
        for j in range(1,len(tab[0])):
            if len(tab[i][j]) >1: # Pbm si on a des états n°10 Regarder si y'a un tiret dans le str (ça sera plus simple que de demandé à Théo ce bouffon
                return False
    return True



def Determinisation(tab,entrees,sorties): # Pas FINI
    new_tab = []
    etat = []
    new_tab.append(tab[0])
    new_tab.append([''.join([str(elem) for elem in entrees])])
    tab_interm = []
    etat.append(new_tab)

    for elt in entrees : # L'unique entrée
        for i in range(1,len(tab)):
            if elt in tab[i][0] :
                tab_interm.append(tab[i])
    new_tab[1].extend(tab_interm[0][1:])

    for i in range(1,len(tab_interm)):
        for j in range(1,len(new_tab[0])):
            new_tab[1][j] = new_tab[1][j] + tab_interm[i][j]
        if new_tab[1][i] not in etat:
            etat.append(tab_interm[i])
            new_tab.append([new_tab[1][i]])




    return new_tab









