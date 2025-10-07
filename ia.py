from random import random
from faiblesses_types import faiblesses_simple, faiblesses_double

# Fonction pour définir la faiblesse de pokémon adverse et forcer l'attaque super efficace pour l'attaquant
def Weakness(attaquant, defenseur):
    """Détermine la faibnlesse du pokemon défenseur pour renvoyer l'attaque super efficace"""
    index = -1
    super_efficace = []
    classique_attaque = []
    resistant = []
    for attaque in attaquant.attaques:
        index += 1

        if attaque.type in faiblesses_simple[defenseur.type]['faible_contre'] and attaquant.type == attaque.type:
            super_efficace.append(index)
        
        elif attaque.type in faiblesses_simple[defenseur.type]['faible_contre']:
            super_efficace.append(index)
        
        elif attaque.type in faiblesses_simple[defenseur.type]['resistant_contre']:
            resistant.append(index)

        else:
            classique_attaque.append(index)

    if super_efficace:
        # Choisir l'attaque super efficace avec la plus grande puissance
        idx = max(super_efficace, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 2, f"--- L'attaque : {attaquant.attaques[idx].nom} est super efficace ! ---"
    
    elif classique_attaque:
        # Choisir l'attaque classique avec la plus grande puissance
        idx = max(classique_attaque, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 1, f"--- L'attaque : {attaquant.attaques[idx].nom} est normale ! ---"
    
    else:
        # Choisir l'attaque résistante avec la plus grande puissance
        idx = max(resistant, key=lambda i: attaquant.attaques[i].puissance)
        return idx, 0.5, f"--- L'attaque : {attaquant.attaques[idx].nom} est peu efficace ! ---"
