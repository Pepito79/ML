tickets = [
"""{
  "magasin": 12345,
  "timestamp": "2015-06-10 09:37:55",
  "client": 7654321,
  "promotions_emises": [34567, 1233],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coke",
      "categorie": "boisson",
      "prix_unitaire": 1.25,
      "quantite": 6
    },
    {
      "produit": "poulet",
      "categorie": "viande",
      "prix_unitaire": 8.99,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-06-11 10:15:22",
  "client": 7654322,
  "promotions_emises": [45678],
  "promotions_utilisees": [45678],
  "articles": [
    {
      "produit": "cola",
      "categorie": "boisson gazeuse",
      "prix_unitaire": 1.30,
      "quantite": 2
    },
    {
      "produit": "steak haché",
      "categorie": "viande",
      "prix_unitaire": 5.67,
      "quantite": 3
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-06-12 11:23:45",
  "client": 7654323,
  "promotions_emises": [56789, 2345],
  "promotions_utilisees": [2345],
  "articles": [
    {
      "produit": "coca",
      "categorie": "soda",
      "prix_unitaire": 1.20,
      "quantite": 4
    },
    {
      "produit": "lait",
      "categorie": "produit laitier",
      "prix_unitaire": 0.99,
      "quantite": 2
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-06-13 14:45:12",
  "client": 7654324,
  "promotions_emises": [],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca-Cola",
      "categorie": "boisson",
      "prix_unitaire": 1.35,
      "quantite": 1
    },
    {
      "produit": "pain",
      "categorie": "boulangerie",
      "prix_unitaire": 1.10,
      "quantite": 3
    }
  ]
}""",
"""{
  "magasin": 12348,
  "timestamp": "2015-06-14 16:30:18",
  "client": 7654325,
  "promotions_emises": [67890],
  "promotions_utilisees": [67890],
  "articles": [
    {
      "produit": "coca light",
      "categorie": "soda light",
      "prix_unitaire": 1.40,
      "quantite": 2
    },
    {
      "produit": "oeufs",
      "categorie": "produit frais",
      "prix_unitaire": 2.50,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-06-15 17:12:33",
  "client": 7654326,
  "promotions_emises": [78901, 3456],
  "promotions_utilisees": [3456],
  "articles": [
    {
      "produit": "Pepsi",
      "categorie": "soda",
      "prix_unitaire": 1.25,
      "quantite": 3
    },
    {
      "produit": "yaourt",
      "categorie": "produit laitier",
      "prix_unitaire": 0.45,
      "quantite": 8
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-06-16 18:05:47",
  "client": 7654327,
  "promotions_emises": [89012],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "cola zero",
      "categorie": "boisson",
      "prix_unitaire": 1.30,
      "quantite": 2
    },
    {
      "produit": "fromage",
      "categorie": "produit laitier",
      "prix_unitaire": 2.75,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-06-17 19:22:19",
  "client": 7654328,
  "promotions_emises": [90123, 4567],
  "promotions_utilisees": [4567],
  "articles": [
    {
      "produit": "Coke zero",
      "categorie": "soda light",
      "prix_unitaire": 1.45,
      "quantite": 1
    },
    {
      "produit": "jambon",
      "categorie": "charcuterie",
      "prix_unitaire": 3.20,
      "quantite": 2
    }
  ]
}""",
"""{
  "magasin": 12348,
  "timestamp": "2015-06-18 20:15:28",
  "client": 7654329,
  "promotions_emises": [1234],
  "promotions_utilisees": [1234],
  "articles": [
    {
      "produit": "Coca-cola original",
      "categorie": "boisson gazeuse",
      "prix_unitaire": 1.50,
      "quantite": 1
    },
    {
      "produit": "saumon",
      "categorie": "poisson",
      "prix_unitaire": 7.80,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-06-19 09:45:36",
  "client": 7654330,
  "promotions_emises": [23456, 5678],
  "promotions_utilisees": [5678],
  "articles": [
    {
      "produit": "cola cherry",
      "categorie": "soda",
      "prix_unitaire": 1.55,
      "quantite": 1
    },
    {
      "produit": "pâtes",
      "categorie": "épicerie",
      "prix_unitaire": 1.20,
      "quantite": 2
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-06-20 10:30:42",
  "client": 7654331,
  "promotions_emises": [34567],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca",
      "categorie": "boisson",
      "prix_unitaire": 1.25,
      "quantite": 4
    },
    {
      "produit": "riz",
      "categorie": "épicerie",
      "prix_unitaire": 1.80,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-06-21 11:20:15",
  "client": 7654332,
  "promotions_emises": [45678, 6789],
  "promotions_utilisees": [6789],
  "articles": [
    {
      "produit": "Coke cherry",
      "categorie": "soda",
      "prix_unitaire": 1.60,
      "quantite": 1
    },
    {
      "produit": "thon",
      "categorie": "poisson",
      "prix_unitaire": 2.30,
      "quantite": 3
    }
  ]
}""",
"""{
  "magasin": 12348,
  "timestamp": "2015-06-22 12:35:24",
  "client": 7654333,
  "promotions_emises": [56789],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "cola vanille",
      "categorie": "boisson",
      "prix_unitaire": 1.65,
      "quantite": 1
    },
    {
      "produit": "pommes",
      "categorie": "fruit",
      "prix_unitaire": 2.10,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-06-23 13:40:33",
  "client": 7654334,
  "promotions_emises": [67890, 7890],
  "promotions_utilisees": [7890],
  "articles": [
    {
      "produit": "Pepsi Max",
      "categorie": "soda light",
      "prix_unitaire": 1.30,
      "quantite": 2
    },
    {
      "produit": "bananes",
      "categorie": "fruit",
      "prix_unitaire": 1.50,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-06-24 14:50:44",
  "client": 7654335,
  "promotions_emises": [78901],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca zero sugar",
      "categorie": "boisson light",
      "prix_unitaire": 1.45,
      "quantite": 1
    },
    {
      "produit": "carottes",
      "categorie": "légume",
      "prix_unitaire": 0.80,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-06-25 15:55:55",
  "client": 7654336,
  "promotions_emises": [89012, 8901],
  "promotions_utilisees": [8901],
  "articles": [
    {
      "produit": "Coke original",
      "categorie": "soda",
      "prix_unitaire": 1.25,
      "quantite": 3
    },
    {
      "produit": "salade",
      "categorie": "légume",
      "prix_unitaire": 1.20,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12348,
  "timestamp": "2015-06-26 16:45:12",
  "client": 7654337,
  "promotions_emises": [90123],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "cola diet",
      "categorie": "boisson light",
      "prix_unitaire": 1.35,
      "quantite": 2
    },
    {
      "produit": "tomates",
      "categorie": "légume",
      "prix_unitaire": 2.30,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-06-27 17:30:18",
  "client": 7654338,
  "promotions_emises": [12345, 9012],
  "promotions_utilisees": [9012],
  "articles": [
    {
      "produit": "Pepsi light",
      "categorie": "soda light",
      "prix_unitaire": 1.40,
      "quantite": 1
    },
    {
      "produit": "oignons",
      "categorie": "légume",
      "prix_unitaire": 1.10,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-06-28 18:20:27",
  "client": 7654339,
  "promotions_emises": [23456],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca-Cola light",
      "categorie": "boisson gazeuse light",
      "prix_unitaire": 1.50,
      "quantite": 1
    },
    {
      "produit": "pommes de terre",
      "categorie": "légume",
      "prix_unitaire": 2.00,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-06-29 19:15:39",
  "client": 7654340,
  "promotions_emises": [34567, 123],
  "promotions_utilisees": [123],
  "articles": [
    {
      "produit": "cola original",
      "categorie": "soda",
      "prix_unitaire": 1.25,
      "quantite": 4
    },
    {
      "produit": "courgettes",
      "categorie": "légume",
      "prix_unitaire": 1.40,
      "quantite": 2
    }
  ]
}""",
"""{
  "magasin": 12348,
  "timestamp": "2015-06-30 20:05:48",
  "client": 7654341,
  "promotions_emises": [45678],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca-Cola zero",
      "categorie": "boisson gazeuse light",
      "prix_unitaire": 1.55,
      "quantite": 1
    },
    {
      "produit": "aubergines",
      "categorie": "légume",
      "prix_unitaire": 1.60,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-07-01 09:50:57",
  "client": 7654342,
  "promotions_emises": [56789, 234],
  "promotions_utilisees": [234],
  "articles": [
    {
      "produit": "Pepsi max cherry",
      "categorie": "soda light",
      "prix_unitaire": 1.60,
      "quantite": 1
    },
    {
      "produit": "poivrons",
      "categorie": "légume",
      "prix_unitaire": 1.80,
      "quantite": 2
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-07-02 10:40:06",
  "client": 7654343,
  "promotions_emises": [67890],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "cola cherry zero",
      "categorie": "boisson light",
      "prix_unitaire": 1.65,
      "quantite": 1
    },
    {
      "produit": "haricots verts",
      "categorie": "légume",
      "prix_unitaire": 2.20,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-07-03 11:35:15",
  "client": 7654344,
  "promotions_emises": [78901, 345],
  "promotions_utilisees": [345],
  "articles": [
    {
      "produit": "Coke zero cherry",
      "categorie": "soda light",
      "prix_unitaire": 1.70,
      "quantite": 1
    },
    {
      "produit": "champignons",
      "categorie": "légume",
      "prix_unitaire": 1.90,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12348,
  "timestamp": "2015-07-04 12:25:24",
  "client": 7654345,
  "promotions_emises": [89012],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca-Cola cherry",
      "categorie": "boisson gazeuse",
      "prix_unitaire": 1.75,
      "quantite": 1
    },
    {
      "produit": "épinards",
      "categorie": "légume",
      "prix_unitaire": 1.30,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-07-05 13:20:33",
  "client": 7654346,
  "promotions_emises": [90123, 456],
  "promotions_utilisees": [456],
  "articles": [
    {
      "produit": "cola vanille zero",
      "categorie": "boisson light",
      "prix_unitaire": 1.80,
      "quantite": 1
    },
    {
      "produit": "brocoli",
      "categorie": "légume",
      "prix_unitaire": 1.50,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-07-06 14:15:42",
  "client": 7654347,
  "promotions_emises": [12345],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca vanille",
      "categorie": "soda",
      "prix_unitaire": 1.85,
      "quantite": 1
    },
    {
      "produit": "chou-fleur",
      "categorie": "légume",
      "prix_unitaire": 1.60,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-07-07 15:10:51",
  "client": 7654348,
  "promotions_emises": [23456, 567],
  "promotions_utilisees": [567],
  "articles": [
    {
      "produit": "Coke vanille",
      "categorie": "soda",
      "prix_unitaire": 1.90,
      "quantite": 1
    },
    {
      "produit": "poireaux",
      "categorie": "légume",
      "prix_unitaire": 1.70,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12348,
  "timestamp": "2015-07-08 16:05:00",
  "client": 7654349,
  "promotions_emises": [34567],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "cola original zero",
      "categorie": "boisson light",
      "prix_unitaire": 1.95,
      "quantite": 1
    },
    {
      "produit": "asperges",
      "categorie": "légume",
      "prix_unitaire": 2.50,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12345,
  "timestamp": "2015-07-09 17:00:09",
  "client": 7654350,
  "promotions_emises": [45678, 678],
  "promotions_utilisees": [678],
  "articles": [
    {
      "produit": "Pepsi vanilla",
      "categorie": "soda",
      "prix_unitaire": 2.00,
      "quantite": 1
    },
    {
      "produit": "artichauts",
      "categorie": "légume",
      "prix_unitaire": 2.80,
      "quantite": 1
    }
  ]
}""",
"""{
  "magasin": 12346,
  "timestamp": "2015-07-10 18:55:18",
  "client": 7654351,
  "promotions_emises": [56789],
  "promotions_utilisees": [],
  "articles": [
    {
      "produit": "Coca-Cola vanilla",
      "categorie": "boisson gazeuse",
      "prix_unitaire": 2.05,
      "quantite": 1
    },
    {
      "produit": "avocats",
      "categorie": "fruit",
      "prix_unitaire": 1.90,
      "quantite": 2
    }
  ]
}""",
"""{
  "magasin": 12347,
  "timestamp": "2015-07-11 19:50:27",
  "client": 7654352,
  "promotions_emises": [67890, 789],
  "promotions_utilisees": [789],
  "articles": [
    {
      "produit": "cola vanilla zero",
      "categorie": "boisson light",
      "prix_unitaire": 2.10,
      "quantite": 1
    }"""]