# ceci est une application gui pour l'ensemble de mes comptes
from tkinter import *
from tkinter import ttk
import sqlite3
class Compte:
	filename = 'comptes.db'
	def __init__(self):
		self.root = root
		self.create_count() 
		self.logo()
		#self.scrolbar()
		self.tree_view()
		self.liste_des_compte()
		
		style_ttk = ttk.Style()
		style_ttk.configure("Treeview", font = ('cambria', 10,'italic'))
		style_ttk.configure("Treeview.Heading", font = ('Arial', 12,'bold'))
		#element parent des widgets 
	#fonctionnlite afficher un logo
	def logo(self):
		logo = PhotoImage(file ='logo.png')
		label = Label(image = logo)
		label.image = logo
		label.grid(row = 0 , column = 0)
		#fonctionnalite creation d'un nouveau compte
	def create_count(self):
		grand_lab = LabelFrame(self.root , text = 'Creation')
		grand_lab.grid(row = 0 , column = 1)
		self.type = Label(grand_lab , text = 'type de compte' , fg ='white' , bg = 'green')
		self.type.grid(row = 0 , column = 0 , pady = 3)
		self.champ_type = Entry(grand_lab)
		self.champ_type.grid(row = 0 , column = 1)
		self.email = Label(grand_lab , text = 'Email :' , fg = 'white' , bg = 'green')
		self.email.grid(row = 1 , column = 0 , pady = 4)
		self.champ_email = Entry(grand_lab)
		self.champ_email.grid(row = 1 , column = 1 , padx = 4)
		self.password = Label(grand_lab , text = 'Mot de passe :' , fg = 'white' , bg = 'green')
		self.password.grid(row = 2 , column = 0)
		self.champ_password = Entry(grand_lab)
		self.champ_password.grid(row = 2 , column = 1 , padx = 4)
		Valider_button = Button(grand_lab , text = 'Ajouter' , font = ('Verdanana' ,12,'italic') , command = self.save_record)
		Valider_button.grid(row = 3 , column = 2 , sticky = E ,padx = 5)


	def requete_sql(self ,requete , parametre = ()):
		connexion = sqlite3.connect(self.filename)
		curseur = connexion.cursor()
		resultat = curseur.execute(requete , parametre)
		connexion.commit()
		return resultat
	def tree_view(self):
		self.defiler = Scrollbar(orient = 'vertical')
		self.arbre = ttk.Treeview(height = 20 , columns = ('email','password'),yscrollcommand = self.defiler.set)
		self.arbre.grid(row = 5 , column = 0 , columnspan = 4, sticky = S , pady = 4)
		self.arbre.heading('#0', text = 'Type de Compte' , anchor = W)
		self.arbre.heading("email", text = 'Adresse mail' , anchor = W)
		self.arbre.heading("password", text = 'Mot de passe' , anchor = W)
		#self.defiler = Scrollbar(self.root)
		self.defiler.config(command = self.arbre.yview)
		self.defiler.grid()
	
	def liste_des_compte(self):
		#cette fonction doit affiicher mes comptes sur un treeview
		elements_tree = self.arbre.get_children()
		for element in elements_tree:
			self.arbre.delete(element)
		requete = 'SELECT * FROM mes_comptes'

		compte_password = self.requete_sql(requete)

		for infos in compte_password:
			self.arbre.insert('',0, text = infos[0] , value = (infos[1],infos[2]))
	#def scrolbar(self):
		
	def is_no_empty(self):
		typee = self.champ_type.get()
		email = self.champ_email.get()
		password = self.champ_type.get()
		valider = len(typee) != 0 and  len(email) != 0 and len(password) != 0
		return valider
	def save_record(self):
		if self.is_no_empty():
			self.new_type = self.champ_type.get()
			self.new_email = self.champ_email.get()
			self.new_password = self.champ_password.get()
			self.champ_type.delete(0 , END)
			self.champ_email.delete(0 , END)
			self.champ_password.delete(0 , END)

			requete = 'INSERT INTO mes_comptes VALUES(?,?,?)'
			parametre = (self.new_type,self.new_email,self.new_password)
			self.requete_sql(requete , parametre)
			self.liste_des_compte()



if __name__ == '__main__':
	root = Tk()
	root.title("mes comptes")
	application = Compte()
	root.mainloop()