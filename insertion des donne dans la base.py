#ce script a pour but de mettre tous les comptes dans la base
import sqlite3
connexion = sqlite3.connect('comptes.db')
curseur = connexion.cursor()
curseur.execute('DELETE FROM mes_comptes WHERE email = ?','zalbas2217@gmail.com')
connexion.commit()
