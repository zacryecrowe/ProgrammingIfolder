
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Patient:
    def __init__(self, name, rank, id, wounds, hp, myparent):
        self.name = name
        self.rank = rank
        self.wounds = wounds
        id = 0 
    def InitializeComponent(self):
     	
    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def getWounds(self):
        return self.wounds

    def getRandomName():
        names = ["S.Franciszek", "Y.Dor","N.Jozef","S.Edmund","G.Gallagher","H.Iago",
                 "A.Vitaliy","O.Langdon","E.Bertrand","I.Dayton","J.Osborne","R.Herschel",
                 "O.Wright","T.Graciano","J.Goodwin","M.Hallsteinn","M.O'Bren"]
        return random.choice(names)

    def getRandomRank():
        ranks = ["Private", "Corporal","Sergeant","PFC.","W.O."]
        return random.choice(ranks)

    def getRandomWounds():
      ### Possible Wounds 
      Gunshot = ["Gunshot-","Band",7] 
      Shrapnel = ["Shrapnel","Band",5]
      Scrapes = ["Scrapes","Band",3]
      Shock = ["Shock","Morp",7]
      Fractures = ["Fractures","Spli",2]
      Broken_Bones = ["Broken_Bones","Spli",5]
      Mangled_Limb = ["Mangled_Limb","Surg",10]
      Wounds = [] 
      Pos = [Gunshot, Shrapnel,Scrapes,Shock,Fractures,Broken_Bones,Mangled_Limb]
      Rand = [1,2,3,4,5] 
      num = random.choice(Rand)
      for i in range (num): 
        Wounds.append(random.choice(Pos))
      return Wounds

    def createRandomPatient():
#        name = Patient.getRandomName()
        rank = Patient.getRandomRank()
        wounds = Patient.getRandomWounds()
        id = self.id
        return Patient(name, rank, id, wounds, hp)
        self.id += 1

	def spawnPatient():
		 patients.append(Patient.createRandomPatient())
		 
	def RequestInfo(id):
		for patient in patients: 
			if id in patient: 
				return(patient)
	def update

patients = []



#for patient in patients:
   # print(f"Name: {patient.getName()}, Rank: {patient.getRank()}, Wounds: {patient.getWounds()}")
		
	
