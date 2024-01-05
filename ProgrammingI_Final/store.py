
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class store(Form):
	def __init__(self, myparent):
		self.InitializeComponent()
		self.myparent = myparent
		self.shelf1 = ["B", "B","B"]
		self.shelf2 = ["M", "M", "M"]
		self.shelf3 = ["S", "S", "S"]
		self.playerinv = ["X"]
	def InitializeComponent(self):
		self.Name = "store"
		self.Text = "store"
		
	def storeupdate(self): 
		Band = len(self.shelf1[::])
		Morp = len(self.shelf2[::])
		Splint = len(self.shelf3[::])
		inv = self.playerinv[0]
		self.myparent.updatestore(Band, Morp, Splint, inv)
		
	#______________Player Inv Checker______________
	
	def heldcheck(self): 
		held = self.playerinv[0]
		if held == "X":
			return "empty"
		elif held == "B": 
			return "Band" 
		elif held == "M":
			return "Morp"
		elif held == "S": 
			return "Spli"
	
	# ______________Bandage Updates______________
	def band_to_shelf(self):
		pass 
	def band_to_player(self):
		inv = self.heldcheck()
		if inv == "empty": 
			del self.shelf1[-1]
			self.playerinv = ["B"]
		else:
			self.myparent.storeerror("You are already holding something!")
			
		pass 
	def band_return(self):
		pass 
	
	#______________Morphine Updates______________
	
	#______________Splint Updates Updates______________