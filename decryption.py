def decrypt(path_of_file, path_of_key, letters, numbers, decalage_cesar):
    """
    Fonction permettant de déchiffrer le fichier choisi, en se servant de la clé de chiffrement.
    args:
        - path_of_file:str,   chemin du fichier à déchiffrer
        - path_of_key:str,    chemin du fichier contenant la clé de chiffrement
        - letters:list,       liste permettant d'appliquer un décalage inverse au contenu du fichier à déchiffrer
        - numbers:list,       liste permettant d'appliquer un décalage inverse à la clé de chiffrement
        - decalage_cesar:int, valeur déterminant le décalage inverse à appliquer sur la clé de chiffrement
    """

    #on ouvre le fichier contenant la clé de chiffrement en mode lecture pour recupérer le contenu
    file = open(path_of_key, "r") 
    key = file.read()
    file.close() 

    #on ouvre le fichier contenant la clé de chiffrement en mode écrasement pour supprimer le contenu
    file = open(path_of_key, "w") 
    file.write("")
    file.close()

    #on ouvre le fichier à déchiffrer en mode lecture pour récuperer le contenu
    file = open(path_of_file, "r")
    content = file.read() 
    file.close

    #on ouvre le fichier à déchiffrer en mode écrasement pour pouvoir réecrire le contenu déchiffrer à l'intérieur
    file = open(path_of_file, "w")

    #variables permettant d'effectuer les calculs de déchiffrement
    decal = 0        #contient le décalage 'final' à appliquer au caractère
    new_letter = ""  #contient la nouvelle lettre déchiffrée à ajouter au contenu déchiffrer
    tot_content = "" #contient le contenu déchiffré à réecrire dans le fichier
    index_of_key = 0 #contient l'index de la clé de chiffrement

    #on déchiffre la clé
    new_key = ""

    for number in key:
        if number not in numbers: #si ce n'est pas un chiffre (donc un '/'), on le laisse
            new_key = new_key + number
        elif numbers.index(number) - decalage_cesar < 0: #si le décalage est trop grand on fait un calcul pour
            decal = decalage_cesar - numbers.index(number) #retrouver son 'vrai' décalage
            new_key = new_key + numbers[-decal]
        else: #sinon on applique simplement le décalage inverse
            new_key = new_key + numbers[numbers.index(number) - decalage_cesar]

    #on déchiffre maintenant le contenu du fichier chiffré

    for letter in content:
        if new_key[index_of_key] == "/": #si c'est un caractère non traitable on ne le change pas
            new_letter = letter
        elif letters.index(letter) - int(new_key[index_of_key]) < 0: #si le decalage est trop grand on fait un
            decal = int(new_key[index_of_key]) - letters.index(letter) #calcul pour retrouver le 'vrai' décalage
            new_letter = letters[-decal]
        else: #sinon on applique simplement le décalage inverse
            new_letter = letters[letters.index(letter) - int(new_key[index_of_key])]
        
        tot_content = tot_content + new_letter #on ajoute le nouveau caractère au contenu déchiffré
        index_of_key += 1 #on augmente l'index de 1, pour avancer dans la clé
        
    #on écrit le fichier totalement déchiffré dans le fichier
    file.write(tot_content)
    file.close()