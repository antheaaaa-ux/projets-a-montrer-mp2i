clé=int(input("Entrez une clé: "))               
chaine=input("Entrez une chaine: ")
def césar(chaine,clé):                            
    mess_code=""                                  
    for i in range (0,len(chaine)):                
        lettre_1= chaine[i]                       
        ascii_lettre_1= ord(lettre_1)             
        ascii_lettre_codée= ascii_lettre_1 + clé  
        if ascii_lettre_codée < ord('a') :        
            ascii_lettre_codée+=26               
        elif ascii_lettre_codée > ord ('z'):      
            ascii_lettre_codée-=26                

        nouvelle_lettre= chr(ascii_lettre_codée)  
        mess_code=mess_code + nouvelle_lettre     
    return mess_code                              
print(césar(chaine,clé))                          