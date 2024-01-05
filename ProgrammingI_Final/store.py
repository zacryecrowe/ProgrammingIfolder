
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
		
	#______________Return Function, reliant on heldcheck then will select appropriate from below______________
	
	def heldreturn(self):
		held = self.heldcheck()
		if held == "Band":
			self.band_return()			 
		elif held == "Morp":
			self.morp_return()
		elif held == "Spli": 
			self.spli_return()
		else:
			self.myparent.storeerror("You are not holding anything to return!")
	
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
		self.shelf1.append("B")
		self.playerinv = ["X"]
		pass 
	
	#______________Morphine Updates______________
	
	def morp_to_player(self):
		inv = self.heldcheck()
		if inv == "empty": 
			del self.shelf2[-1]
			self.playerinv = ["M"]
		else:
			self.myparent.storeerror("You are already holding something!")
			
	def morp_return(self):
		self.shelf2.append("M")
		self.playerinv = ["X"]
	
	#______________Splint Updates Updates______________
	
	def spli_to_player(self):
		inv = self.heldcheck()
		if inv == "empty": 
			del self.shelf3[-1]
			self.playerinv = ["S"]
		else:
			self.myparent.storeerror("You are already holding something!")
			
	def spli_return(self):
		self.shelf3.append("S")
		self.playerinv = ["X"]