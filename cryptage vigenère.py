clé=input("Entrez une clé: ")
chaine=input("Entrez une chaine: ")         
def vigenere(chaine, clé):
    texte_chiffré = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i=0
    for caractère in chaine:
        if caractère in alphabet:
            decalage = ord(clé[i]) - ord('a')
            caractère_chiffré = chr((ord(caractère) - ord('a') + decalage) % 26 + ord('a'))
            texte_chiffré = texte_chiffré+caractère_chiffré
            i+=1
            if i == len(clé):          
                i=0
        else:
            texte_chiffré = texte_chiffré+caractère
    return texte_chiffré    

print(vigenere(chaine,clé)) 