# reduction.py - version avec fonction (bonus 4.3)

def calcul_reduction(prix, etudiant, fidelite):
    """Retourne la réduction totale (en €) pour un prix donné."""
    reduction = 0.0
    if etudiant:
        reduction += prix * 0.10
    if fidelite >= 5:
        reduction += prix * 0.15
    if prix > 100:
        reduction += 5.0
    return reduction


def prix_final(prix, etudiant, fidelite):
    """Retourne le prix après réduction, jamais inférieur à 0."""
    return max(0.0, prix - calcul_reduction(prix, etudiant, fidelite))


if __name__ == "__main__":
    try:
        prix = float(input("Prix du produit (€) : "))
        if prix <= 0:
            raise ValueError
        etudiant = input("Êtes-vous étudiant ? (o/n) ").strip().lower() == "o"
        fidelite = int(input("Fidélité (en années) : "))
    except ValueError:
        print("Saisie invalide.")
        exit(1)

    print(f"Réduction totale : {calcul_reduction(prix, etudiant, fidelite):.2f} €")
    print(f"Prix final : {prix_final(prix, etudiant, fidelite):.2f} €")
