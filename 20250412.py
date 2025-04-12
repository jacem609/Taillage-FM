import math
from itertools import permutations

# === Partie calcul du diamètre ===
M = float(input("Entrez la valeur du module M : "))
Alpha_degrees = float(input("Entrez la valeur de l'angle alpha en degré : "))
z = float(input("Entrez Z le nombre de dents : "))

Alpha_radians = math.radians(Alpha_degrees)
result = 7.9577 * math.sin(Alpha_radians) / M
diam_ext = (M / math.cos(Alpha_radians) * z) + 2 * M

print(f"\nLe diamètre extérieur est : {round(diam_ext, 4)}")
print(f"Le résultat (ratio cible) est : {round(result, 4)}")

# === Partie recherche de combinaison ===
liste_chiffres = [30, 32, 35, 36, 40, 43, 45, 49, 50, 51, 52, 52, 53, 54, 55, 55, 55, 59, 61, 62, 64, 65, 67, 68, 70, 70, 80, 120]
valeur_utilisateur = result  # Assignation automatique
tolerance = 0.0001
limite_resultats = 20

# === Étape 1 : A / B ===
print("\n--- Recherche de combinaisons simples A / B ---")
combinaisons_simples = set()
resultats_simples = []

for A, B in permutations(liste_chiffres, 2):
    if B != 0:
        resultat = A / B
        ecart = abs(resultat - valeur_utilisateur)
        if ecart <= tolerance:
            combinaison = tuple(sorted([A, B]))
            if combinaison not in combinaisons_simples:
                combinaisons_simples.add(combinaison)
                resultats_simples.append((A, B, round(resultat, 4), ecart))

resultats_simples.sort(key=lambda x: x[3])

if resultats_simples:
    for A, B, res, ecart in resultats_simples[:limite_resultats]:
        print(f"A = {A}, B = {B} => Résultat = {res}")
else:
    print("Aucune combinaison simple trouvée.")

# === Étape 2 : A / B * C / D ===
print("\n--- Recherche de combinaisons complexes A / B × C / D ---")
combinaisons_complexes = set()
resultats_complexes = []

for A, B, C, D in permutations(liste_chiffres, 4):
    if B != 0 and D != 0:
        resultat = A / B * C / D
        ecart = abs(resultat - valeur_utilisateur)
        if ecart <= tolerance:
            combinaison = tuple(sorted([A, B, C, D]))
            if combinaison not in combinaisons_complexes:
                combinaisons_complexes.add(combinaison)
                resultats_complexes.append((A, B, C, D, round(resultat, 4), ecart))

resultats_complexes.sort(key=lambda x: x[5])

if resultats_complexes:
    for A, B, C, D, res, ecart in resultats_complexes[:limite_resultats]:
        print(f"A = {A}, B = {B}, C = {C}, D = {D} => Résultat = {res}")
else:
    print("Aucune combinaison complexe trouvée.")

print("\nBy JACEM")
