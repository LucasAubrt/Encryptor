from random import randint #importation de la fonction randint qui va servir à générer un décalage aléatoirement
import save #importation de la fonction save afin de sauvegarder la clé et le contenu chiffré

def encrypt(path_of_file, letters, numbers, decal_cesar):
    """
    Fonction permettant de chiffrer le fichier choisi, et de créer une clé de chiffrement.
    args:
        - path_of_file:str,   chemin du fichier à chiffrer
        - letters:list,       liste permettant d'appliquer un décalage au contenu du fichier à chiffrer
        - numbers:list,       liste permettant d'appliquer un décalage à la clé de chiffrement
        - decalage_cesar:int, valeur déterminant le décalage à appliquer sur la clé de chiffrement

    """

    #on ouvre le fichier à chiffrer en mode lecture pour récuperer son contenu.
    file = open(path_of_file, "r")
    content = file.read()
    file.close()

    #variables permettant d'effectuer les calculs de déchiffrement
    new_letter = ""  #contient la nouvelle lettre chiffrée à rajouter à la clé
    new_content = "" #contient le nouveau contenu chiffré à écrire dans le fichier choisi
    tot_decal = ""   #contient l'entièreté de la clé à écrire dans un fichier key.txt

    #chiffrement du fichier choisi

    for letter in content:
        decal = randint(0,9)
        print(letter, decal)
        if letter not in letters: #si c'est un caractère qu'on ne traite pas, on le laisse
            new_content = new_content + letter
            decal = "/" #et on écrit un '/' dans la clé de chiffrement
        elif letters.index(letter) + decal > len(letters) - 1: #si l'index devient trop grand on effectue un calcul
            new_letter = (letters.index(letter) + decal) - (len(letters) - 1) #pour retrouver son 'vrai' décalage
            new_content = new_content + letters[new_letter - 1]
        else: #sinon on applique simplement le décalage
            new_content = new_content + letters[letters.index(letter) + decal]
        
        tot_decal = tot_decal + str(decal) #on ajoute un chiffre ou un '/' à la clé
    
    #chiffrement de la clé

    #variables permettant d'effectuer les calculs de chiffrement de la clé
    new_key = "" #contient la nouvelle clé chiffrée
    new_decal = "" #contient le nouveau chiffre ou '/' chiffré à rajourer à la clé

    for number in tot_decal:
        if number not in numbers: #si c'est un '/' on ne fait rien
            new_key = new_key + number
        elif numbers.index(number) + decal_cesar > len(numbers) - 1: #si le décalage est trop grand on fait un
            new_decal = (numbers.index(number) + decal_cesar) - (len(numbers) - 1) #calcul pour retrouver le 'vrai décalage'
            new_key = new_key + numbers[new_decal - 1]
        else: #sinon on applique simplement le cécalage
            new_key = new_key + numbers[numbers.index(number) + decal_cesar]
    
    #on enregistre le nouveau contenu chiffré et la clé chiffrée aussi
    save.Save(path_of_file, new_content, new_key)