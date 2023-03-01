import customtkinter #importation du module graphique
from tkinter import filedialog as fd #importation du fialdialog en tant que fd
import decryption #importation de la fonction de chiffrement
import encryption #importation de la fonction de déchiffrement

#liste contenant tous les caractères chiffrables (peut être étendu à l'infini sauf au "/")
letters = [
	"a", "b", "c", "d", "e", "é", "è", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
	"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    ".", "?", "!", ":", ";"
]

#on vérifie le type de toutes les variables contenues dans la liste 'letters'
for i in letters:
    assert type(i) == str, "letters doit contenir uniquement que des strigs"

#liste contenant tous les chiffres contenus dans la clé de chiffrement
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#on vérifie le type de toutes les variables contenues dans la liste 'numbers'
for i in numbers:
    assert type(i) == int, "numbers doit contenir que des integers"

def choose_file_encrypt(label):
    """
    Fontion permettant de choisir le fichier que l'on veut chiffrer, quand le bouton qui lui est relié sera cliqué.
    args:
        - label:widget, label à modifier pour indiquer quel fichier a été choisi.
    """

    filetypes = (('text files', '*.txt'), ('All files', '*.*')) #prise en charge uniquement des .txt

    filename = fd.askopenfilename(
        title = 'Ouvrir le fichier a chiffrer',
        initialdir = '/', #on se place dans le répertoire racine
        filetypes = filetypes
    )

    global path_file_encrypt #on récupère la variable globale afin de lui assigner le chemin du fichier à chiffrer
    path_file_encrypt = filename

    filename = filename.split('/') #permet de créer une liste en séparant le chemin  tous les "/""
    filename = filename[-1] #permet de sélectionner le dernier élément de la liste sans connaître son index

    label.configure(text=f"{filename}") #changer le text du label en fontion du path du fichier choisi

def choose_file_key(label):
    """
    Fontion permettant de choisir le fichier contenant la clé de chiffrement lorsque le bouton qui lui est relié
    sera cliqué.
    args:
        - label:widget, label à modifier pour indiquer quel fichier a été choisi.
    """

    filetypes = (('text files', '*.txt'), ('All files', '*.*')) #prise en compte uniquement des .txt

    filename = fd.askopenfilename(
        title = 'Ouvrir le fichier cle',
        initialdir = '/', #on se place dans le répertoire racine
        filetypes = filetypes
    )

    global path_file_key #on recupère la variable globale afin de lui assigner le chemin de la clé de chiffrement
    path_file_key = filename

    filename = filename.split('/') #permet de créer une liste en séparant le chemin tous les "/"
    filename = filename[-1] #permet de sélectionner le dernier élément de la liste sans connaître son index

    label.configure(text=f"{filename}") #changer le text du label en fontion du path du fichier choisi

def maj_label(slider, label):
    """
    Fonction permettant de mettre à jour le texte du label en fonction de la valeur du slider.
    args :
        - label:widget, label qui affichera la valeur du slider
        - slider:widget, slider où l'utilisateur détermine une valeur
    """

    assert 1 <= slider.get() <= 9, "Le slider doit contenir une valeur entre 1 et 9"

    label.configure(text=f"Décalage : {int(slider.get())}") #on met à jour le label avec la valeur du slider


#proprietés de la fenêtre
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("Encryptor")
app.resizable(height=False, width=False)
app.geometry("500x300")

#variables globales permettant de recupérer le path du fichier à chiffrer et de la clé de chiffrement
path_file_encrypt = ""
path_file_key = ""

#label permettant d'afficher le fichier à chiffrer choisi
label_file_encrypt = customtkinter.CTkLabel(master=app, text="")
label_file_encrypt.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)

#bouton permettant d'importer le fichier à chiffrer
btn_file_encrypt = customtkinter.CTkButton(master=app, text="Importer le fichier à chiffrer", command=lambda:choose_file_encrypt(label_file_encrypt))
btn_file_encrypt.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)

#label permettant d'afficher le fichier choisi contenant la clé de chiffrement
label_file_key = customtkinter.CTkLabel(master=app, text="")
label_file_key.place(relx = 0.77, rely=0.2, anchor=customtkinter.CENTER)

#bouton permettant d'importer le fichier qui contient la clé de déchiffrement
btn_file_key = customtkinter.CTkButton(master=app, text="Importer la clef de déchiffrement", command=lambda:choose_file_key(label_file_key))
btn_file_key.place(relx=0.77, rely=0.1, anchor=customtkinter.CENTER)

#slider permettant de sélectionner le décalage choisi lors du chiffrement de clé de chiffrement
slider = customtkinter.CTkSlider(master=app, from_=1, to=9, number_of_steps=9)
slider.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    
#label permettant d'afficher le décalage sélectionner dans le slider
label_decalage = customtkinter.CTkLabel(master=app, text=f"Décalage : {int(slider.get())}", width=120, height=25, corner_radius=8)
label_decalage.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

#bouton permettant de lancer la fonction de chiffrement
btn_encrypt = customtkinter.CTkButton(master=app, text="Chiffrer", command=lambda:encryption.encrypt(path_file_encrypt, letters, numbers, int(slider.get())))
btn_encrypt.place(relx=0.2, rely=0.8, anchor=customtkinter.CENTER)

#bouton permettant de lancer la fonction de déchiffrement
btn_decrypt = customtkinter.CTkButton(master=app, text="Déchiffrer", command=lambda:decryption.decrypt(path_file_encrypt, path_file_key, letters, numbers, int(slider.get())))
btn_decrypt.place(relx=0.80, rely=0.8, anchor=customtkinter.CENTER)

#Evenement permettant de mettre constamment à jour la valeur du slider
app.bind('<Motion>', lambda event:maj_label(slider, label_decalage))

app.mainloop() #affichage en boucle de la fenêtre