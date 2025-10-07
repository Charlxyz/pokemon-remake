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

class Soin:
    def __init__(self, power, name):
        self.soin_power = power
        self.nom_soin = name

    def description(self):
        return f"{self.nom_soin} | PUISSANCE : {self.soin_power}"
    
    def heal(self, pokemon):
        pokemon.vie = min(pokemon.vie + self.soin_power, pokemon.pv_max)
        return f"--- {pokemon.nom} a été soigné | PV : {pokemon.vie}/{pokemon.pv_max} ---"
