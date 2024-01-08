
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Patient(Form):
	def __init__(self, name, rank, visible_wounds, hidden_wounds, hp, myparent):
		self.InitializeComponent()
		self.name = name 
		self.rank = rank 
		self.visible_wounds = pdsad
	
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
#Visible Wounds 
#Hidden HP Value 


"""