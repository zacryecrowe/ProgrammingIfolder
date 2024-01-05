
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class store(Form):
	def __init__(self, myparent):
		self.InitializeComponent()
		self.myparent = myparent
		self.shelf1 = ["B", "B", "B"]
		self.shelf2 = ["M", "M", "M"]
		self.shelf3 = ["S", "S", "S"]
	def InitializeComponent(self):
		self.Name = "store"
		self.Text = "store"
		
	def storeupdate(self): 
		Band = len(self.shelf1[::])
		Morp = len(self.shelf2[::])
		Splint = len(self.shelf3[::])
		self.myparent.updatestore(Band, Morp, Splint)