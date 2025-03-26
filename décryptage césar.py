clé=int(input("Entrez une clé: "))
chaine=input("Entrez une chaine: ")
def décryptage_césar(chaine,clé):
    mess_code=""
    for indice in range (0,len(chaine)):
        lettre_1= chaine[indice]
        ascii_lettre_1= ord(lettre_1)
        ascii_lettre_décodée= ascii_lettre_1 - clé     
        if ascii_lettre_décodée < ord('a') : 
            ascii_lettre_décodée+=26
        elif ascii_lettre_décodée > ord ('z'):
            ascii_lettre_décodée-=26

        nouvelle_lettre= chr(ascii_lettre_décodée)
        mess_code=mess_code + nouvelle_lettre
    return mess_code
print(décryptage_césar(chaine,clé))