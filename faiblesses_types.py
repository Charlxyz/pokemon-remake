# Table de Loi des Types 
faiblesses_simple = {
    'Normal': {
        'faible_contre': ['Combat'],
        'resistant_contre': [],
        'inefficace_contre': ['Spectre']
    },
    'Feu': {
        'faible_contre': ['Eau', 'Sol', 'Roche'],
        'resistant_contre': ['Feu', 'Plante', 'Glace', 'Insecte', 'Acier', 'Fée'],
        'inefficace_contre': []
    },
    'Eau': {
        'faible_contre': ['Électrik', 'Plante'],
        'resistant_contre': ['Feu', 'Eau', 'Glace', 'Acier'],
        'inefficace_contre': []
    },
    'Plante': {
        'faible_contre': ['Feu', 'Glace', 'Poison', 'Vol', 'Insecte'],
        'resistant_contre': ['Eau', 'Électrik', 'Plante', 'Sol'],
        'inefficace_contre': []
    },
    'Électrik': {
        'faible_contre': ['Sol'],
        'resistant_contre': ['Électrik', 'Vol', 'Acier'],
        'inefficace_contre': []
    },
    'Glace': {
        'faible_contre': ['Feu', 'Combat', 'Roche', 'Acier'],
        'resistant_contre': ['Glace'],
        'inefficace_contre': []
    },
    'Combat': {
        'faible_contre': ['Vol', 'Psy', 'Fée'],
        'resistant_contre': ['Insecte', 'Roche', 'Ténèbres'],
        'inefficace_contre': []
    },
    'Poison': {
        'faible_contre': ['Sol', 'Psy'],
        'resistant_contre': ['Plante', 'Combat', 'Poison', 'Fée', 'Insecte'],
        'inefficace_contre': []
    },
    'Sol': {
        'faible_contre': ['Eau', 'Plante', 'Glace'],
        'resistant_contre': ['Poison', 'Roche'],
        'inefficace_contre': ['Électrik']
    },
    'Vol': {
        'faible_contre': ['Électrik', 'Glace', 'Roche'],
        'resistant_contre': ['Plante', 'Combat', 'Insecte'],
        'inefficace_contre': ['Sol']
    },
    'Psy': {
        'faible_contre': ['Insecte', 'Spectre', 'Ténèbres'],
        'resistant_contre': ['Combat', 'Psy'],
        'inefficace_contre': []
    },
    'Insecte': {
        'faible_contre': ['Feu', 'Vol', 'Roche'],
        'resistant_contre': ['Plante', 'Combat', 'Sol'],
        'inefficace_contre': []
    },
    'Roche': {
        'faible_contre': ['Eau', 'Plante', 'Combat', 'Sol', 'Acier'],
        'resistant_contre': ['Normal', 'Feu', 'Poison', 'Vol'],
        'inefficace_contre': []
    },
    'Spectre': {
        'faible_contre': ['Spectre', 'Ténèbres'],
        'resistant_contre': ['Poison', 'Insecte'],
        'inefficace_contre': ['Normal', 'Combat']
    },
    'Dragon': {
        'faible_contre': ['Glace', 'Dragon', 'Fée'],
        'resistant_contre': ['Feu', 'Eau', 'Électrik', 'Plante'],
        'inefficace_contre': []
    },
    'Ténèbres': {
        'faible_contre': ['Combat', 'Insecte', 'Fée'],
        'resistant_contre': ['Spectre', 'Ténèbres'],
        'inefficace_contre': ['Psy']
    },
    'Acier': {
        'faible_contre': ['Feu', 'Combat', 'Sol'],
        'resistant_contre': ['Normal', 'Plante', 'Glace', 'Vol', 'Psy', 'Insecte', 'Roche', 'Dragon', 'Acier', 'Fée'],
        'inefficace_contre': ['Poison']
    },
    'Fée': {
        'faible_contre': ['Poison', 'Acier'],
        'resistant_contre': ['Combat', 'Insecte', 'Ténèbres'],
        'inefficace_contre': ['Dragon']
    }
}
