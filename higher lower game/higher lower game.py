score = 0
utilisateur = True
while utilisateur:
    pays1, pays2 = liste_dico_alea(liste_pays)
    
    print ("En 2021, le score de la qualité de l'air (0=mauvais/100=excellent) à ", pays1["City"], "du pays: ", pays1["Country"], "était de ", pays1["AirQuality"],)
    
    choix = input ("Est-ce-que la même année, le score de la qualité de l'air à "+ pays2["City"] + " du pays: " + pays2["Country"] + " était mieux ? (moins si la qualité de l'air était moins bonne/plus si la qualité de l'air était meilleure)")
    
    correct = (choix == "plus" and compare_dico(pays2, pays1, "AirQuality")) or (choix == "moins" and compare_dico(pays1, pays2, "AirQuality"))
    
    if correct:
        score = score+1
        print("Bien joué ! Votre score est:", score)
    else:
        utilisateur = False
        
print("Dommage, vous avez atteint le score de" ,score)