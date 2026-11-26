class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def est_recent(self, annee_seuil=2020):
        """Retourne True si le document est récent (année >= seuil)."""
        return self.annee >= annee_seuil

    def afficher(self):
        print(f"{self.titre} ({self.annee})")


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")


class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")


class Bibliotheque:
    def __init__(self, documents=None):
        self.documents = list(documents) if documents is not None else []

    def ajouter_document(self, doc):
        self.documents.append(doc)

    def rechercher(self, titre):
        """Recherche les documents dont le titre correspond (insensible à la casse)."""
        titre_recherche = titre.strip().lower()
        return [doc for doc in self.documents if titre_recherche in doc.titre.lower()]


# Test initial (sortie conservée à l'identique)
docs = [
    Livre("1984", 1949, "George Orwell"),
    Magazine("Science & Vie", 2023, 456),
    Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
]

for d in docs:
    d.afficher()

# Tests supplémentaires pour est_recent() et Bibliotheque.rechercher()
print("\n--- Tests extensions ---")
for d in docs:
    print(f"{d.titre} est récent (>= 2020) ? {d.est_recent()}")

biblio = Bibliotheque(docs)
resultats = biblio.rechercher("1984")
print("Résultats de recherche pour '1984' :")
for r in resultats:
    r.afficher()