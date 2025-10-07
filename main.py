from random import random
import eel
from pokemon import *
from attaque import *
from soin import *
from ia import Weakness
from utils import CalculDegats
from classe import *

# Dossier où se trouvent tes fichiers HTML/JS/CSS
eel.init('web')

# --- EEL EXPOSED FUNCTIONS ---
@eel.expose
def Fight_eel():
    result = Combat(Evoli, Pikachu)
    return result




# --- POKEMON COMBAT LOGIC ---

Evoli.ajouter_attaque(Charge)
Evoli.ajouter_attaque(Surf)
Evoli.ajouter_attaque(Telluriforce)
Evoli.ajouter_attaque(Picpic)
Evoli.heal.append(potion)

Pikachu.ajouter_attaque(Éclair)
Pikachu.ajouter_attaque(Charge)
Pikachu.ajouter_attaque(Tonnerre)
Pikachu.ajouter_attaque(BecVrille)
Pikachu.heal.append(potion)

def fight():
    pass

def Combat(poke1, poke2):
    logs = []  # on stocke les messages ici
    
    if poke1.vitesse == poke2.vitesse:
        choix = random.randint(0, 1)
        if choix == 1:
            poke1, poke2 = poke2, poke1
    elif poke1.vitesse < poke2.vitesse:
        poke1, poke2 = poke2, poke1

    logs.append(f"{poke1.nom} commence le combat contre {poke2.nom} !")

    max_tours = 100
    tour = 0

    while poke1.vie > 0 and poke2.vie > 0 and tour < max_tours:
        tour += 1
        logs.append(f"--- Tour {tour} ---")

        if poke1.vie <= poke1.pv_max/2 and poke1.heal:
            logs.append(poke1.utiliser_soin())
        else:
            choix_att_poke1 = Weakness(poke1, poke2)
            dgt = CalculDegats(poke1, poke2, poke1.attaques[choix_att_poke1[0]], choix_att_poke1[1])
            poke2.PerdVie(dgt[0])
            logs.append(f"{poke1.nom} utilise {poke1.attaques[choix_att_poke1[0]]} sur {poke2.nom} et lui inflige {dgt[0]} PV.")
            if poke2.vie <= 0:
                logs.append(f"{poke2.nom} est K.O !")
                break

        if poke2.vie <= poke2.pv_max/2 and poke2.heal:
            logs.append(poke2.utiliser_soin())
        else:
            choix_att_poke2 = Weakness(poke2, poke1)
            dgt = CalculDegats(poke2, poke1, poke2.attaques[choix_att_poke2[0]], choix_att_poke2[1])
            poke1.PerdVie(dgt[0])
            logs.append(f"{poke2.nom} contre-attaque avec {poke2.attaques[choix_att_poke2[0]]} et inflige {dgt[0]} PV.")
            if poke1.vie <= 0:
                logs.append(f"{poke1.nom} est K.O !")
                break

    return logs 


# Lancer l'application et ouvrir index.html
eel.start('test.html')
