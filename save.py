
def Save(path_of_file, content, key):
    """
    Fonction qui permet d'enregistrer le nouveau contenu chiffré, ainsi que la clé de chiffrement.
    args:
        - path_of_file:str : chemin du fichier à chiffrer
        - content:str      : nouveau contenu chiffré à écrire dans le fichier
        - key:str          : clé de chiffrement à écrire dans un fichier key.txt
    """

    #on ouvre le fichier à chiffrer en mode écrasement pour réecrire le contenu chiffré
    file = open(path_of_file, "w") 
    file.write(content)
    file.close()

    #on ouvre ou créer le fichier key.txt en mode écrasement pour réecrire la clé chiffrée
    file = open("key.txt", "w")
    file.write(key)
    file.close()