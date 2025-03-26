texte_chiffre = input("Entrez le texte chiffré: ")
cle = input("Entrez la clé: ")
def decryptage_vigenere(texte_chiffre, cle):
    texte_decrypte = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    for caractere in texte_chiffre:
        if caractere in alphabet:
            decalage = ord(cle[i]) - ord('a')
            caractere_decrypte = chr((ord(caractere) - ord('a') - decalage) % 26 + ord('a')) 
            texte_decrypte += caractere_decrypte
            i += 1
            if i == len(cle):
                i = 0
        else:
            texte_decrypte += caractere
    return texte_decrypte
print(decryptage_vigenere(texte_chiffre, cle))