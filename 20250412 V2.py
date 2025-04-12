import streamlit as st
import math
from itertools import permutations

st.title("Calcul de diamètre et recherche de combinaison")
st.markdown("**By JACEM**")

# === Entrées utilisateur ===
M = st.number_input("Module M", min_value=0.0001, format="%.4f")
alpha_deg = st.number_input("Angle alpha (en degrés)", min_value=0.0, max_value=90.0, format="%.2f")
z = st.number_input("Nombre de dents Z", min_value=1, step=1)

if M and alpha_deg and z:
    # === Calculs ===
    alpha_rad = math.radians(alpha_deg)
    result = 7.9577 * math.sin(alpha_rad) / M
    diam_ext = (M / math.cos(alpha_rad) * z) + 2 * M

    st.subheader("Résultats de calcul")
    st.write(f"**Diamètre extérieur :** {round(diam_ext, 4)} mm")
    st.write(f"**Résultat (ratio cible) :** {round(result, 4)}")

    valeur_cible = result
    tolerance = 0.0001
    limite_resultats = 20
    liste_chiffres = [30, 32, 35, 36, 40, 43, 45, 49, 50, 51, 52, 52, 53, 54, 55, 55, 55, 59, 61, 62, 64, 65, 67, 68, 70, 70, 80, 120]

    # === Recherche A / B ===
    st.subheader("Combinaisons simples (A / B)")
    combinaisons_simples = set()
    resultats_simples = []

    for A, B in permutations(liste_chiffres, 2):
        if B != 0:
            val = A / B
            ecart = abs(val - valeur_cible)
            if ecart <= tolerance:
                combinaison = tuple(sorted([A, B]))
                if combinaison not in combinaisons_simples:
                    combinaisons_simples.add(combinaison)
                    resultats_simples.append((A, B, round(val, 4), ecart))

    resultats_simples.sort(key=lambda x: x[3])
    if resultats_simples:
        for A, B, val, _ in resultats_simples[:limite_resultats]:
            st.write(f"A = {A}, B = {B} → Résultat = {val}")
    else:
        st.write("Aucune combinaison simple trouvée.")

    # === Recherche A / B × C / D ===
    st.subheader("Combinaisons complexes (A / B × C / D)")
    combinaisons_complexes = set()
    resultats_complexes = []

    for A, B, C, D in permutations(liste_chiffres, 4):
        if B != 0 and D != 0:
            val = A / B * C / D
            ecart = abs(val - valeur_cible)
            if ecart <= tolerance:
                combinaison = tuple(sorted([A, B, C, D]))
                if combinaison not in combinaisons_complexes:
                    combinaisons_complexes.add(combinaison)
                    resultats_complexes.append((A, B, C, D, round(val, 4), ecart))

    resultats_complexes.sort(key=lambda x: x[5])
    if resultats_complexes:
        for A, B, C, D, val, _ in resultats_complexes[:limite_resultats]:
            st.write(f"A = {A}, B = {B}, C = {C}, D = {D} → Résultat = {val}")
    else:
        st.write("Aucune combinaison complexe trouvée.")
