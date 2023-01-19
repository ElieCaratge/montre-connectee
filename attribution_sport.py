import numpy as np
import random

def initialisation_probas(matrice_sports, sport_initial):
    """matrice_sports est un numpy array, sport_inital est un int lié à la liste des sports du fichier sports.py
    renvoie des plages de valeur entre 0 et 1 qui correspond à la probabilité de chaque sport d'être choisi"""
    array_probas = np.array([])
    nb_sports = np.shape(matrice_sports)[0]
    for i in range(nb_sports):
        if i != (sport_initial):
            array_probas = np.append(
                array_probas, matrice_sports[sport_initial][i])
    array_probas = np.cumsum(array_probas)/array_probas.sum()
    return(array_probas)


def attribution_sport(array_probas, liste_sports_restants):
    """on choisit un nombre aléatoire et on regarde quel sport a été sélectionné"""
    x = random.random()
    i = 0
    while array_probas[i] < x:
        i += 1
    return(i, liste_sports_restants[i])


def modification_liste_sports(array_probas, sport_choisi, rang_sport_choisi, liste_sports_restants, sports_deja_choisis):
    "On rajoute le sport sélectionné à la liste des sports déjà choisis et on l'enlève de la liste des sports disponibles"
    sports_deja_choisis.append(sport_choisi)
    liste_sports_restants = np.delete(liste_sports_restants, rang_sport_choisi)
    "On enlève la plage de valeur qui correspond au sport choisi"
    if (rang_sport_choisi == 0):
        proba_enlevee = array_probas[rang_sport_choisi]
    else:
        proba_enlevee = array_probas[rang_sport_choisi] - array_probas[rang_sport_choisi-1]
    for i in range(rang_sport_choisi, len(array_probas)):
        array_probas[i] = array_probas[i] - proba_enlevee
    np.delete(array_probas, rang_sport_choisi)
    "On renormalise la plage de valeurs"
    array_probas = array_probas/(1-proba_enlevee)
    return(array_probas, sports_deja_choisis, liste_sports_restants)


def fct_principale(matrice_sports, sport_initial):
    nb_sports = np.shape(matrice_sports)[0]
    sports_deja_choisis = []
    liste_sports_restants = np.array([i for i in range(0, nb_sports)])
    liste_sports_restants = np.delete(liste_sports_restants, sport_initial)
    array_probas = initialisation_probas(matrice_sports, sport_initial)
    (rang_sport_choisi, sport_choisi) = attribution_sport(
        array_probas, liste_sports_restants)
    while len(liste_sports_restants) > 1:
        (array_probas, sport_deja_choisis, liste_sports_restants) = modification_liste_sports(
            array_probas, sport_choisi, rang_sport_choisi, liste_sports_restants, sports_deja_choisis)
        (rang_sport_choisi, sport_choisi) = attribution_sport(
            array_probas, liste_sports_restants)
        print(sports_deja_choisis, liste_sports_restants)
    sports_deja_choisis.append(sport_choisi)
    return(sports_deja_choisis)

