import random

# Fonction culculant les dégats a efféctué sur le pokmemon adversaire en prennant en compte sa défense et autre facteur 
def CalculDegats(attaquant, defenseur, attaque, multiplicateur: float) -> int:
    """Calcule le nombre de dégat en prenant compte des coups critiques, stab, multiplicateur de résistance ou d'efficacité."""
    degat = (((2 * 100 / 5 + 2) * attaque.puissance * attaquant.attaque / defenseur.defense) / 50) + 2

    # Facteur aléatoire (entre 0.85 et 1.00)
    facteur_random = random.uniform(0.85, 1.0)

    stab = 1.2 if attaquant.type == attaque.type else 1

    if random.random() < 0.1:  # 10 % de chance de critique
        critique = 1.5
        message = "--- Coup Critique ! ---"
    else:
        critique = 1
        message = ""

    modificateur = stab * multiplicateur * critique * facteur_random
    dgt = degat * modificateur

    return round(dgt), message
