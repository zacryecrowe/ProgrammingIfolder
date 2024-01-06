
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
		self.counter = 0
		self.delivertime = 30 
		self.requestFlag = False
		self.requesttype = 0 
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._trequest = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# trequest
		# 
		#self._trequest.Enabled = True
		#self._trequest.Tick += self.TrequestTick
		# 
		# store
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Name = "store"
		self.Text = "store"
		self.ResumeLayout(False)
		
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
	
	def bandrequest(self):
		self.shelf1.append("B")
		self.shelf1.append("B")
		self.shelf1.append("B")
	
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
		
	def morprequest(self):
		self.shelf2.append("M")
		self.shelf2.append("M")
		self.shelf2.append("M")
	
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
		
	def splirequest(self):
		self.shelf3.append("S")
		self.shelf3.append("S")
		self.shelf3.append("S")
		
	#______________Timer Requests______________

	"""def TrequestTick(self, sender, e):
		if self.requestFlag == True:
			self.myparent.storeerror("Timer Recieved Request")
			self.counter += 1
			if self.counter >= self.delivertime:
				self.counter = 0
				if self.requesttype == 1:
					self.bandrequest()
				elif self.requesttype == 2: 
					self.morprequest()
				elif self.requesttype == 3: 
					self.splirequest()
				self.requestFlag = False
			else: 	
				pass 														
		else: 
			pass 
		pass
	"""