import sqlite3

connexion = sqlite3.connect("entreprise.db")
curseur = connexion.cursor()

curseur.execute("""CREATE TABLE personne (
    personne_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR,
    prenom VARCHAR,
    nmr_identiter INTEGER,
    date_naissance DATE
    );""")

curseur.execute("""CREATE TABLE salaire (
    salaire_id INTEGER NOT NULL PRIMARY KEY, 
    montant FLOAT,
    date_payement DATE
    );""")


curseur.execute("""CREATE TABLE etudiant (
    etudiant_id INTEGER NOT NULL PRIMARY KEY, 
    personne_id INTEGER REFERENCES personne,
    salaire_id INTEGER REFERENCES salaire
    );""")


curseur.execute("""CREATE TABLE retraiter (
    retraiter_id INTEGER NOT NULL PRIMARY KEY, 
    personne_id INTEGER REFERENCES personne,
    salaire_id INTEGER REFERENCES salaire
    );""")


curseur.execute("""CREATE TABLE policier (
    policier_id INTEGER NOT NULL PRIMARY KEY, 
    personne_id INTEGER REFERENCES personne,
    salaire_id INTEGER REFERENCES salaire
    );""")


curseur.execute('INSERT INTO personne (nom, prenom, nmr_identiter, date_naissance ) VALUES ("Maurice", "Traore", 2123456, \'1995-01-01\');') 
p1_id = curseur.lastrowid

curseur.execute('INSERT INTO personne (nom, prenom, nmr_identiter, date_naissance ) VALUES ("Marie", "Dupont", 18964545, \'1991-01-01\');') 
p2_id = curseur.lastrowid

curseur.execute('INSERT INTO personne (nom, prenom, nmr_identiter, date_naissance ) VALUES ("Fabien", "Leboeuf", 124526737, \'1998-01-01\');') 
p3_id = curseur.lastrowid


curseur.execute('INSERT INTO  salaire ( montant,  date_payement ) VALUES ( 1000.30, \'2023-01-01\');') 
s1_id = curseur.lastrowid


curseur.execute('INSERT INTO  salaire ( montant,  date_payement ) VALUES (2000.30, \'2023-01-01\');') 
s2_id = curseur.lastrowid

curseur.execute('INSERT INTO  salaire ( montant,  date_payement ) VALUES ( 3000.30, \'2023-01-01\');') 
s3_id = curseur.lastrowid


curseur.execute('INSERT INTO etudiant (personne_id, salaire_id) VALUES (' + str(p1_id) + ', '+ str(s3_id ) +');')

curseur.execute('INSERT INTO retraiter (personne_id, salaire_id) VALUES (' + str(p2_id) + ', '+ str(s1_id ) +');')


curseur.execute('INSERT INTO policier (personne_id, salaire_id) VALUES (' + str(p3_id) + ', '+ str(s2_id ) +');')

etudiant =curseur.execute('SELECT  nom, prenom, date_naissance, montant, date_payement FROM personne p JOIN etudiant e ON p.personne_id = e.personne_id JOIN  salaire s ON s.salaire_id = e.salaire_id  ').fetchall()
print("infos Étudiant",etudiant)



connexion.commit()
connexion.close()