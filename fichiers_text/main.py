import os.path, json

if not os.path.exists("Liste_Pizza"):
    os.mkdir("Liste_Pizza")

class WriteFiles:
    def __init__(self, name_file, data ):
        self.fichier =  open("Liste_Pizza/"+name_file, "w" )
        self.data = json.dumps(data)

    def Write(self):
        self.fichier.write(self.data)
        self.fichier.close()


class ReadFiles(WriteFiles):
    def __init__(self,file,data):
        self.file = os.path.join("Liste_Pizza",file)
        super().__init__(file,data)

    def ExistFiles(self) ->bool:
        if os.path.exists(self.file):
            return True
        return False
    
    def read(self)->str:
        if not self.ExistFiles():
            print("Le Fechier n'existe pas ")
            return 
        else:
            f = open(self.file,"r")
            test = f.read()
            f.close()
            return test
    
class Pizza(ReadFiles):
    def  __init__(self, file, data ):
        super().__init__( file, data)

    def JsonLoad(self):
        return  json.loads(self.read())

    def getNom(self):
        return  self.JsonLoad()[0]
    
    def getPrix(self):
         return  self.JsonLoad()[1]
        
    def getIngredient(self):
        
        return self.JsonLoad()[2]
    
    def estVeg(self):
         return  self.JsonLoad()[-1]
    
    def affiche(self):
        veg_str = ""
        if self.estVeg():
                veg_str = " - VÉGÉTARIENNE"
        print(f"PIZAA {self.getNom()} : {self.getPrix()}€" + veg_str)
        print("INGRÉDIENT:" ,", ".join(self. getIngredient()))
        print()


            
liste1 = ("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True)
liste2 = ("Hawai", 9.5, ("tomate", "ananas", "oignons"))
liste3 = ("4 saisons", 11, ("oeuf", "emmental", "tomate", "jambon", "olives", 'olive'))
liste4 = ("Végétarienne", 7.8, ("champignons", "tomate", "oignons", "poivrons"), True)



p1 = Pizza('file1.txt',liste1)
p1.Write( )
p1.read()
p1.affiche()

p2 = Pizza('file2.txt',liste2)
p2.Write( )
p2.read()
p2.affiche()

p3 = Pizza('file3.txt',liste3)
p3.Write( )
p3.read()
p3.affiche()

p4 = Pizza('file4.txt',liste4)
p4.Write( )
p4.read()
p4.affiche()
