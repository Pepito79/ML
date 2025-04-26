from collections import Counter
from gensim.models import word2vec
import math

def calculate_tf(chaine: str, word: str):
    """
    Normalise all the words by removing the "-"
    """
    words = chaine.lower().split()  # Liste des mots
    words_normalise = [w.replace("-", "") for w in words]
    words_count = Counter(words_normalise)  # Compte la fréquence des mots normalisés
    tf = words_count[word.lower().replace("-", "")] / len(words_count)  # TF pour un mot donné
    print(words_normalise)
    print(f"TF for {word}: {tf}")
    return tf

def calculate_idf(liste: list, word: str):
    """
    Calculer le IDF pour un mot donné à travers tous les documents.
    """
    number_docs = len(liste)
    num_docs_with_word = sum(1 for texte in liste if word.lower() in texte.lower())
    if num_docs_with_word == 0:
        return 0  # éviter division par zéro si le mot n'existe pas dans les documents
    val = math.log((number_docs / num_docs_with_word)) + 1
    print(f"IDF for {word}: {val}")
    return val

def tf_idf(doc: list):
    """
    Calcule le TF-IDF pour chaque mot dans une liste de documents.
    """
    dico = {}
    for d in doc:
        for word in d.split():  # Parcours les mots de chaque document
            word_normalised = word.lower().replace("-", "")  # Normalise le mot
            if word_normalised not in dico:
                tf = calculate_tf(d, word)
                idf = calculate_idf(doc, word)
                dico[word_normalised] = tf * idf  # Calcul du TF-IDF
            else:
                # Si le mot est déjà dans le dictionnaire, on accumule sa valeur
                tf = calculate_tf(d, word)
                idf = calculate_idf(doc, word)
                dico[word_normalised] += tf * idf  # On ajoute la valeur du TF-IDF

    print("TF-IDF Dictionary: ", dico)
    return dico

# Exemple d'utilisation
tf_idf(["Coucou Saad es faIT tu du coca-cola", "Saad tu es monstrueux"])
