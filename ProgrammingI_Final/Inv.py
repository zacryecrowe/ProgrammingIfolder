
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Inv(Form):
	def __init__(self, my parent):
		self.InitializeComponent()
		self.myparent = myparent	
		
		#Flags 
		self.delFlag = False 
		
		
		#Key 
		"""
		XBX = Bandage 
		}|> = Morphine 
		/-/ = Splint		
		"""
		#____________________ Inv Lists ___________________________
		self.Shelf1 = ["XBX", "XBX", "XBX"]
		self.Shelf2 = ["}|>","}|>" ,"}|>"]
		self.Shelf3 = ["/-/","/-/","/-/"]
		
	
	def InitializeComponent(self):
		self.Name = "Inv"
		self.Text = "Inv"
		
	#REQUESTS FUNCTIONS 
	
	def BandageRequest 


	def MorphineRequest 
	
	
	def 
		
		


	def Timer1Tick(self, sender, e):
		pass