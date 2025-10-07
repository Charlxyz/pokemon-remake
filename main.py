from random import random
import eel

# Dossier où se trouvent tes fichiers HTML/JS/CSS
eel.init('web')

# --- EEL EXPOSED FUNCTIONS ---
@eel.expose
def attaque(nom):
    print(f"{nom} attaque !")
    return f"{nom} a attaqué !"




# --- POKEMON COMBAT LOGIC ---

def fight():
    pass


# Lancer l'application et ouvrir index.html
eel.start('test.html')
