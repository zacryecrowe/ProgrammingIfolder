
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Patient(Form):
	def __init__(self, name, rank, condition, state, pain, wounds, hp, myparent):
		self.InitializeComponent()
		self.name = name 
		self.rank = rank 
		self.condition = condition
		self.state = state 
		self.pain = pain 
		self.wounds = wounds 
		self.hp = hp 
		### Chosen Names ### 
		Chosen = [pass]		
	
	def InitializeComponent(self):
		self.Name = "Patient"
		self.Text = "Patient"

""" IDEAS 

Patients[] 
Each item in list is a patient 

each patient is then a list which contains 
#Random Name 
#Random Rank
#Condition 
#State 
#Pain Rank
#Visible Wounds
	#For each wound 
	#Wound Type 
	#Severity 
	#HP Drain Per Second 
	#Treatment Status 
	#Surgical Tools Flag 
#Hidden HP Value 


"""

def getname(self):
	pass 
def getrank(self): 
	pass 
def getcondition(self):
	pass 
def getstate(self):
	pass 
def getpain(self): 
	pass 
def getwounds(self):
	pass 
def gethp(self): 
	pass 


#### Random Lists For name and Rank, These can be just lists of 
def getRandname(self):
	names = ["S.Franciszek", "Y.Dor","N.Jozef","S.Edmund","G.Gallagher","H.Iago","A.Vitaliy","O.Langdon","E.Bertrand","I.Dayton","J.Osborne","R.Herschel","O.Wright","T.Graciano","J.Goodwin","M.Hallsteinn","M.O'Bren"]
	chosen = self.Chosen 
	Avail = names - chosen
	select = random.choice(Avail) 
	self.Chosen.append(select) 
	return (select)
	pass 
def getRandrank(self): 
	ranks = ["Private", "Corporal","Sergeant","PFC.","W.O."]
	return random.choice(ranks)
	pass 

### Wound generation Nonsense ### 
def getRandwounds(self):
	wounds = [####]
	pass 

def GenSituation(self):
	Situations = ["Shot", "Wire", "Advance", "Landmine", "Artilery", "CQC", "Impact"]  	 
	
def GenWounds(self): 
	
