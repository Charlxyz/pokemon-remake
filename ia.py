from random import random
from faiblesses_types import faiblesses_simple, faiblesses_double

# Fonction pour définir la faiblesse de pokémon adverse et forcer l'attaque super efficace pour l'attaquant
def Weakness(attaquant, defenseur):
    """Détermine la faibnlesse du pokemon défenseur pour renvoyer l'attaque super efficace"""
    index = -1
    tres_efficace = []
    super_efficace = []
    classique_attaque = []
    resistant = []
    tres_resistant = []
    ineficace = []
    if '/' in defenseur.type:
        type1, type2 = defenseur.type.split('/')
    for attaque in attaquant.attaques:
        resultat = WeaknessDouble(attaque.type, type1, type2)

        if resultat == 4:
            tres_efficace.append(index)
        elif resultat == 2:
            super_efficace.append(index)
        elif resultat == 1:
            classique_attaque.append(index)
        elif resultat == 0.5:
            resistant.append(index)
        elif resultat == 0.25:
            tres_resistant.append(index)
        else:
            ineficace.append(index)
        index += 1

    if tres_efficace:
        # Choisir l'attaque très super efficace avec la plus grande puissance
        idx = max(tres_efficace, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 4, f"--- L'attaque : {attaquant.attaques[idx].nom} est très super efficace ! ---"

    elif super_efficace:
        # Choisir l'attaque super efficace avec la plus grande puissance
        idx = max(super_efficace, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 2, f"--- L'attaque : {attaquant.attaques[idx].nom} est super efficace ! ---"
    
    elif classique_attaque:
        # Choisir l'attaque classique avec la plus grande puissance
        idx = max(classique_attaque, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 1, f"--- L'attaque : {attaquant.attaques[idx].nom} est normale ! ---"
    
    elif resistant:
        # Choisir l'attaque résistante avec la plus grande puissance
        idx = max(resistant, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 0.5, f"--- L'attaque : {attaquant.attaques[idx].nom} est peu efficace ! ---"
    
    elif tres_resistant:
        # Choisir l'attaque très résistante avec la plus grande puissance
        idx = max(tres_resistant, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 0.25, f"--- L'attaque : {attaquant.attaques[idx].nom} est très peu efficace ! ---"
    
    else:
        # Choisir l'attaque inefficace avec la plus grande puissance
        idx = max(ineficace, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 0, f"--- L'attaque : {attaquant.attaques[idx].nom} est inefficace ! ---"

def WeaknessDouble(type_attaque, type1, type2=None):
    """Retourne le multiplicateur de dégâts selon les types défensifs."""
    def mult_pour_type(type_def):
        if type_attaque in faiblesses_simple[type_def]['faible_contre']:
            return 2
        elif type_attaque in faiblesses_simple[type_def]['resistant_contre']:
            return 0.5
        elif type_attaque in faiblesses_simple[type_def]['inefficace_contre']:
            return 0
        return 1

    # Cas d'un type simple
    if type2 is None:
        return mult_pour_type(type1)
    
    # Cas d'un double type -> on multiplie les multiplicateurs
    return mult_pour_type(type1) * mult_pour_type(type2)
