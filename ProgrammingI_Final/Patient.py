
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Patient(Form):
	def __init__(self, name, rank, wounds):
		self.InitializeComponent()
		self.name = name
        self.rank = rank
        self.wounds = wounds
	
	def InitializeComponent(self):
		self.SuspendLayout()
		# 
		# Patient
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Name = "Patient"
		self.Load += self.PatientLoad
		self.ResumeLayout(False)

	def getRandomRank():
		ranks = ["Private", "Corporal","Sergeant","PFC.","W.O."]
		return random.choice(ranks)

	def getRandomWounds():
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
      

	def createRandomPatient():
		name = Patient.getRandomName()
        rank = Patient.getRandomRank()
        wounds = Patient.getRandomWounds()
      #  return Patient(name, rank, wounds,)




#### TEST STUFF###
#num_patients = 4
#patients = []

#for _ in range(num_patients):
 #   patients.append(Patient.createRandomPatient())



#for patient in patients:
   # print(f"Name: {patient.getName()}, Rank: {patient.getRank()}, Wounds: {patient.getWounds()}")
		

	def PatientLoad(self, sender, e):
		pass