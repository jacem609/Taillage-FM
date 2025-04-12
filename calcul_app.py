
import streamlit as st
import math
from itertools import permutations

st.set_page_config(page_title="Calcul Engrenage", layout="centered")
st.title("Calcul de diamètre & Recherche de combinaison")
st.markdown("**Application développée par JACEM**")

# === Partie 1 : Calcul de diamètre extérieur ===
st.header("1. Calcul du diamètre extérieur")

M = st.number_input("Module M", value=1.0, step=0.1)
Alpha_degrees = st.number_input("Angle alpha (en degrés)", value=20.0, step=0.5)
z = st.number_input("Nombre de dents Z", value=20, step=1)

if st.button("Calculer le diamètre"):
    Alpha_radians = math.radians(Alpha_degrees)
    result = 7.9577 * math.sin(Alpha_radians) / M
    diam_ext = (M / math.cos(Alpha_radians) * z) + 2 * M

    st.success(f"Diamètre extérieur : {round(diam_ext, 4)} mm")
    st.success(f"Résultat (7.9577 × sin(alpha) / M) = {round(result, 4)}")

# === Partie 2 : Recherche de combinaison ===
st.header("2. Recherche de combinaison (A/B × C/D)")

valeur_utilisateur = st.number_input("Entrez une valeur cible (ex : 1.2345)", value=1.2345, format="%.4f")
tolerance = st.number_input("Tolérance", value=0.0001, format="%.5f")
limite_resultats = st.slider("Nombre max de résultats", 1, 50, 20)

liste_chiffres = [30, 32, 35, 36, 40, 43, 45, 49, 50, 51, 52, 52, 53, 54, 55, 55, 55, 59,
                  61, 62, 64, 65, 67, 68, 70, 70, 80, 120]

if st.button("Chercher les combinaisons"):
    combinaisons_uniques = set()
    resultats_proches = []

    for A, B, C, D in permutations(liste_chiffres, 4):
        resultat = A / B * C / D
        ecart = abs(resultat - valeur_utilisateur)
        if ecart <= tolerance:
            combinaison = tuple(sorted([A, B, C, D]))
            if combinaison not in combinaisons_uniques:
                combinaisons_uniques.add(combinaison)
                resultats_proches.append((combinaison, round(resultat, 4), ecart))

    resultats_proches.sort(key=lambda x: x[2])

    if resultats_proches:
        st.success(f"{len(resultats_proches)} combinaison(s) trouvée(s) (max {limite_resultats}) :")
        for combinaison, res, ecart in resultats_proches[:limite_resultats]:
            A, B, C, D = combinaison
            st.write(f"A = {A}, B = {B}, C = {C}, D = {D} → Résultat = {res}")
    else:
        st.warning("Aucune combinaison trouvée.")
