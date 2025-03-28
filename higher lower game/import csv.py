import csv

with open('airquality - cities_air_quality_water_pollution.18-10-2021 (1).csv','r') as fic_musique:
    csv_reader = csv.DictReader(fic_musique)
    liste_pays = [ligne for ligne in csv_reader]

for ligne in liste_pays :
    for k,v in ligne.items():
        print(k, "->", v, end=" | ")
    print("\n")