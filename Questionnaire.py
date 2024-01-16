# Fonction demander une réponse numérique 
def demander_reponse_numerique_utilisateur(min, max):
    while True:
        reponse_str = input(f"Votre réponse (entre {min} et {max}): ")
        # Gestion d'erreur
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int
            print("ERREUR: Vous devez rentrer un nombre entre", min, "et", max)
        except ValueError:
            print("ERREUR: Veuillez entrer uniquement des nombres")
            
# Fonction Poser une question
def poser_question(question):
    # Déballer les éléments de la question
    enonce, *choix, bonne_reponse = question

    print("Question:")
    print(enonce)
    
    # Afficher les choix
    for i, option in enumerate(choix, 1):
        print(f"{i}. {option}")

    resultat_reponse_correct = False
    reponse_utilisateur = demander_reponse_numerique_utilisateur(1, len(choix))

    # Vérifier la réponse
    if choix[reponse_utilisateur - 1].lower() == bonne_reponse.lower():
        print("Bonne réponse!")
        resultat_reponse_correct = True
    else:
        print("Mauvaise réponse.")
    
    print()
    return resultat_reponse_correct

# Fonction lancer les quesstionnaire
def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Votre score est :", score, "sur", len(questionnaire))

# Définir le questionnaire
questionnaire = [
    ("Quelle est la capitale du Sénégal ?", "Ziguinchor", "Diourbel", "Dakar", "Saint-Louis", "Dakar"), 
    ("Ousmane Sonko est né en quelle année ?", "1960", "1974", "1963", "2000", "1974"),
    ("Le parti PASTEF Les Patriotes est créé en quelle année ?", "2000", "1958", "2014", "1960", "2014"),
    ("Le Sénégal a son indépendance en quelle année ?", "2014", "2007", "1780", "1960", "1960")
]

# Lancer le questionnaire
lancer_questionnaire(questionnaire)
