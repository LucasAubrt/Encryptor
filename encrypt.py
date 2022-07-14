from random import randint
from tkinter import *
from plyer import notification

letters = [
	"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
	"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

def save(path_of_file, text, code="/"):
	fichier = open(f"{path_of_file}", "a")
	fichier.write(text) #on enregistre la lettre encode
	fichier.close()
	fichier = open("key.txt", "a")
	fichier.write(code) #on enregistre le decalage permettant de retrouver la lettre dans un fichier appeler key.txt
	fichier.close()

def encrypt(path_of_file):
	fichier = open(f"{path_of_file}", "r")
	content = fichier.read() #on recupere le contenu du fichier dans la variable content 
	fichier.close()
	fichier = open(f"{path_of_file}", "w")
	fichier.write("") #on supprime le contenu du fichier pour pouvoir reecrire dedans
	fichier.close()
	random_nbr = 0

	for letter in content:
		if letter == " "  or letter not in letters:
			save(path_of_file, letter) #si le caractere s'agit d'un espace ou que ce n'est pas une lettre, on l'enregistre sans la crypte et sans code pour la retrouver
		else:
			random_nbr = randint(1,9)
			decal = letters.index(letter) + random_nbr
			if decal > 51:
				decal = decal - 51 - 1
			letter = letters[decal] #a == 1 + 5 == 6 == f
			save(path_of_file, letter, str(random_nbr)) #on enregistre la lettre encrypter ainsi que le code dans un autre fichier pour la retrouver

	notification.notify(
		title = "Encryptor",
		message = "Processus terminé !" ,
		timeout = 3
	)


def decrypt(path_of_file, key):
	fichier = open(f"{path_of_file}", "r")
	content = fichier.read() #on recupere le contenu du fichier crypte
	fichier.close()
	fichier = open(f"{path_of_file}", "w")
	fichier.write("") #on supprime le contenu du fichier crypte pour pouvoir ensuite reecrire dedans
	fichier.close()
	fichier = open(f"{key}", "r")
	cle = fichier.read() #on recupere le contenu de la cle nous permettant de decoder le fichier
	fichier.close()
	fichier = open(f"{key}", "w")
	fichier.write("") #on supprime le contenu du fichier pour potentiellement reeecrire dedans par la suite
	fichier.close()
	fichier = open(f"{path_of_file}", "a")
	clef = []
	for i in cle:
		clef.append(i)
	i = 0
	for letter in content:
		if clef[i] == "/":
			fichier.write(letter)
		else:
			decal = letters.index(letter) - int(clef[i])
			letter = letters[decal]
			fichier.write(letter)
		i = i + 1
	fichier.close()
	notification.notify(
		title = "Encryptor",
		message = "Processus terminé !" ,
		timeout = 2
	)

def btn_encrypt():
	encrypt(entr_file_crypt.get())

def btn_decrypt():
	decrypt(entr_file_crypt.get(), entr_file_code.get())


#programme de base qui va se lancer obligatoirement

window = Tk()
window.title("Encryptor")
window.geometry("300x300")
window.resizable(height=False, width=False)

btn_encrypt = Button(window, text="Encrypter", command=btn_encrypt)
btn_encrypt.pack()

btn_decrypt = Button(window, text="Decrypter", command=btn_decrypt)
btn_decrypt.pack()

lb_file_crypt = Label(window, text="Chemin du fichier à crypter :")
lb_file_crypt.pack()

entr_file_crypt = Entry(window)
entr_file_crypt.pack()

lb_file_code = Label(window, text="Chemin du fichier contenant la clé :")
lb_file_code.pack()

entr_file_code = Entry(window)
entr_file_code.pack()

window.mainloop()