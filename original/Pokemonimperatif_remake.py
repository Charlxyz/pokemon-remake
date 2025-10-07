import random

# Table de Loi des Types
faiblesses = {
    'Feu': {'faible_contre': ['Eau', 'Roche', 'Sol'], 'resistant_contre': ['Feu', 'Plante', 'Glace']},
    'Eau': {'faible_contre': ['Électrik', 'Plante'], 'resistant_contre': ['Feu', 'Eau', 'Glace']},
    'Plante': {'faible_contre': ['Feu', 'Glace', 'Poison'], 'resistant_contre': ['Eau', 'Électrik', 'Plante']},
    'Normal': {'faible_contre': ['Combat'], 'resistant_contre': []}
}

# Classe permettant de définir le pokémons ajouter leur attaque, leur nombre de soin, enlever leur vie...
class Pokemon:
    def __init__(self, nom, pv, att, dfs, att_spe, def_spe, vit, typ):
        self.nom = nom
        self.vie = pv
        self.pv_max = pv
        self.attaque = att 
        self.defense = dfs
        self.attaque_special = att_spe
        self.defense_special = def_spe
        self.vitesse = vit
        self.type = typ
        self.attaques = []
        self.heal = []

    def ajouter_attaque(self, attaque):
        if len(self.attaques) <= 3:
            self.attaques.append(attaque)
        else:
            return print(f"Le pokémon {self.nom} as déjà 4 attaques")
    
    def DonneEtat(self):
        return self.vie
    
    def PerdVie(self,nbpoints):
        self.vie=self.vie-nbpoints
        if self.vie < 0:
            self.vie = 0

    def utiliser_soin(self):
        if self.heal:
            soin = self.heal[0]
            message = soin.heal(self)
            self.heal.pop(0)
            return message

    def afficher_stat(self):
        return print(f"{self.nom} (PV : {self.vie} | ATT : {self.attaque} | DEF : {self.defense} | VIT : {self.vitesse})")

# Classe Attaque permettant de définir les attaques des pokémons
class Attaque:
    def __init__(self, name, type, power, type_attaque):
        self.nom = name
        self.type = type
        self.puissance = power
        self.categorie = type_attaque

    def description(self):
        return f"{self.nom} | TYPE : {self.type} | PUISSANCE : {self.puissance} | CATEGORIE : {self.categorie}"

    def __str__(self):
        return f"{self.nom}"

# Classe permettant l'initialisation des soins  
class Soin:
    def __init__(self, power, name):
        self.soin_power = power
        self.nom_soin = name

    def description(self):
        return f"{self.nom_soin} | PUISSANCE : {self.soin_power}"
    
    def heal(self, pokemon):
        pokemon.vie = min(pokemon.vie + self.soin_power, pokemon.pv_max)
        return f"--- {pokemon.nom} a été soigné | PV : {pokemon.vie}/{pokemon.pv_max} ---"

# Fonction pour définir la faiblesse de pokémon adverse et forcer l'attaque super efficace pour l'attaquant
def Weakness(attaquant, defenseur):
    """Détermine la faibnlesse du pokemon défenseur pour renvoyer l'attaque super efficace"""
    index = -1
    super_efficace = []
    classique_attaque = []
    resistant = []
    for attaque in attaquant.attaques:
        index += 1

        if attaque.type in faiblesses[defenseur.type]['faible_contre'] and attaquant.type == attaque.type:
            super_efficace.append(index)
        
        elif attaque.type in faiblesses[defenseur.type]['faible_contre']:
            super_efficace.append(index)
        
        elif attaque.type in faiblesses[defenseur.type]['resistant_contre']:
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

# Fonction culculant les dégats a efféctué sur le pokmemon adversaire en prennant en compte sa défense et autre facteur 
def CalculDegats(attaquant, defenseur, attaque, multiplicateur: float) -> int:
    """Calcule le nombre de dégat en prenant compte des coups critiques, stab, multiplicateur de résistance ou d'efficacité."""
    degat = (((2 * 25 / 5 + 2) * attaque.puissance * attaquant.attaque / defenseur.defense) / 50) + 2

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

# Fonction pour lancer le combat entre les pokémons en appelant toute les autre fonction du code
def Combat(poke1, poke2):
    # Détermine qui attaque en premier
    if poke1.vitesse == poke2.vitesse:
        choix = random.randint(0,1)
        if choix == 1:
            poke1, poke2 = poke2, poke1
    elif poke1.vitesse < poke2.vitesse:
        poke1, poke2 = poke2, poke1

    poke1.afficher_stat()
    poke2.afficher_stat()

    max_tours = 100
    tour = 0

    while poke1.vie > 0 and poke2.vie > 0 and tour < max_tours:
        tour += 1
        print(f"\n--- Tour {tour} ---")

        # Verrification si utilisation de potion possible
        if poke1.vie <= poke1.pv_max/2 and len(poke1.heal) != 0:
            print(poke1.utiliser_soin())
        
        else:
            choix_att_poke1 = Weakness(poke1, poke2)

            dgt = CalculDegats(poke1, poke2, poke1.attaques[choix_att_poke1[0]], choix_att_poke1[1])
            poke2.PerdVie(dgt[0])

            print(f"--- {poke1.nom} utilise : {poke1.attaques[choix_att_poke1[0]]} sur {poke2.nom} qui perds : {dgt[0]} pv ---")

            if poke2.vie <= 0:
                print(f"--- {poke2.nom} a été vaincu par {poke1.nom} ---")
                return
            else:
                print(f"--- {poke2.nom} a : {poke2.vie} pv ---")

            if choix_att_poke1[2] != "": print(choix_att_poke1[2])
            if dgt[1] != "": print(dgt[1])

        print("") # --- Tour du Pokémon 2---

        # Verrification si utilisation de potion possible

        if poke2.vie <= poke2.pv_max/2 and len(poke2.heal) != 0:
            print(poke2.utiliser_soin()) 
        
        else:
            choix_att_poke2 = Weakness(poke2, poke1)

            dgt = CalculDegats(poke2, poke1, poke2.attaques[choix_att_poke2[0]], choix_att_poke2[1])
            poke1.PerdVie(dgt[0])

            print(f"--- {poke2.nom} utilise : {poke2.attaques[choix_att_poke2[0]]} sur {poke1.nom} qui perds : {dgt[0]} pv ---")

            if poke1.vie <= 0:
                print(f"--- {poke1.nom} a été vaincu par {poke2.nom} ---")
                return
            else:
                print(f"--- {poke1.nom} a : {poke1.vie} pv ---")

            if choix_att_poke2[2] != "": print(choix_att_poke2[2])
            if dgt[1] != "": print(dgt[1])

# Initialisation des Pokémons
Carapuce = Pokemon('Carapuce', 314, 214, 241, 209, 251, 196, 'Eau')
Evoli = Pokemon('Evoli',314,209,199,189,251,229,'Normal')

# Soin
potion = Soin(15, 'Potion')

# Attaque
pistolet_a_eau = Attaque('Pistolet A Eau', 'Eau', 40, 'Physique')
tacle = Attaque('Tacle', 'Normal', 40, 'Physique')
griffe = Attaque('Griffe', 'Normal', 40, 'Physique')
lance_flamme = Attaque('Lance Flamme', 'Feu', 90, 'Speciale')
surf = Attaque('Surf', 'Eau', 90, 'Speciale')

# Initialisation Attauqe Evoli
Evoli.ajouter_attaque(pistolet_a_eau)
Evoli.ajouter_attaque(tacle)
Evoli.ajouter_attaque(griffe)
Evoli.ajouter_attaque(lance_flamme)

# Initialisation Attauqe Carapuce
Carapuce.ajouter_attaque(surf)
Carapuce.ajouter_attaque(pistolet_a_eau)
Carapuce.ajouter_attaque(tacle)
Carapuce.ajouter_attaque(griffe)

# Ajouter une potion a chaque Pokémon
Evoli.heal.append(potion)
Carapuce.heal.append(potion)

# Lancement du Combat
Combat(Evoli, Carapuce)
