import math
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *
from Menus import * 
from Menus2 import * 
from store import * 
class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		#ToggleFlags
		self.playflagleft = False 
		self.playflagright = False
		self.playflagup = False
		self.playflagdown = False
		self.menuflag = False 
		#######Game Vars
		#distance to objects where they become interactable 
		self.intdist = 125
		#Center of Objects for Prox function. Each is first 3 letters of word with loc after
		self.cabloc = [self._Cabnet.Bottom-25, self._Cabnet.Right-50]
		self.radloc = [self._Radio.Bottom-25, self._Radio.Right-50]		
		###
		
		self.menu = Menus(self)
		self.menu2 = Menus2(self)
		self.store = store(self)

	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._label1 = System.Windows.Forms.Label()
		self._player = System.Windows.Forms.Label()
		self._tscroll = System.Windows.Forms.Timer(self._components)
		self._Shelf = System.Windows.Forms.Label()
		self._Tspawn = System.Windows.Forms.Timer(self._components)
		self._Cabnet = System.Windows.Forms.Label()
		self._Radio = System.Windows.Forms.Label()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self._DebugBox = System.Windows.Forms.Label()
		self._Shelf2 = System.Windows.Forms.Label()
		self._Shelf3 = System.Windows.Forms.Label()
		self._UpdateTimer = System.Windows.Forms.Timer(self._components)
		self._playerinv = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Location = System.Drawing.Point(580, 648)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(42, 52)
		self._label1.TabIndex = 0
		# 
		# player
		# 
		self._player.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._player.Location = System.Drawing.Point(426, 320)
		self._player.Name = "player"
		self._player.Size = System.Drawing.Size(28, 67)
		self._player.TabIndex = 1
		self._player.Text = "player"
		# 
		# tscroll
		# 
		self._tscroll.Enabled = True
		self._tscroll.Interval = 10
		self._tscroll.Tick += self.TscrollTick
		# 
		# Shelf
		# 
		self._Shelf.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._Shelf.Location = System.Drawing.Point(638, 9)
		self._Shelf.Name = "Shelf"
		self._Shelf.Size = System.Drawing.Size(334, 23)
		self._Shelf.TabIndex = 2
		self._Shelf.Text = "XBX"
		self._Shelf.Click += self.Label2Click
		# 
		# Tspawn
		# 
		self._Tspawn.Enabled = True
		self._Tspawn.Interval = 10
		# 
		# Cabnet
		# 
		self._Cabnet.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._Cabnet.ForeColor = System.Drawing.Color.Black
		self._Cabnet.Location = System.Drawing.Point(577, 9)
		self._Cabnet.Name = "Cabnet"
		self._Cabnet.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._Cabnet.Size = System.Drawing.Size(55, 77)
		self._Cabnet.TabIndex = 3
		self._Cabnet.Text = "Medical Supplies"
		self._Cabnet.Click += self.CabnetClick
		# 
		# Radio
		# 
		self._Radio.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._Radio.ForeColor = System.Drawing.Color.Black
		self._Radio.Location = System.Drawing.Point(872, 123)
		self._Radio.Name = "Radio"
		self._Radio.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._Radio.Size = System.Drawing.Size(100, 50)
		self._Radio.TabIndex = 4
		self._Radio.Text = "Medical Requests"
		self._Radio.Click += self.Label4Click
		# 
		# progressBar1
		# 
		self._progressBar1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._progressBar1.Location = System.Drawing.Point(872, 97)
		self._progressBar1.Maximum = 120
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(100, 23)
		self._progressBar1.TabIndex = 5
		self._progressBar1.Click += self.ProgressBar1Click
		# 
		# DebugBox
		# 
		self._DebugBox.BackColor = System.Drawing.SystemColors.ButtonFace
		self._DebugBox.Location = System.Drawing.Point(372, 429)
		self._DebugBox.Name = "DebugBox"
		self._DebugBox.Size = System.Drawing.Size(260, 23)
		self._DebugBox.TabIndex = 6
		self._DebugBox.Text = "Dialouge Box"
		# 
		# Shelf2
		# 
		self._Shelf2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._Shelf2.Location = System.Drawing.Point(638, 36)
		self._Shelf2.Name = "Shelf2"
		self._Shelf2.Size = System.Drawing.Size(334, 23)
		self._Shelf2.TabIndex = 7
		self._Shelf2.Text = "XBX"
		# 
		# Shelf3
		# 
		self._Shelf3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._Shelf3.Location = System.Drawing.Point(638, 63)
		self._Shelf3.Name = "Shelf3"
		self._Shelf3.Size = System.Drawing.Size(334, 23)
		self._Shelf3.TabIndex = 8
		self._Shelf3.Text = "XBX"
		# 
		# UpdateTimer
		# 
		self._UpdateTimer.Enabled = True
		self._UpdateTimer.Tick += self.UpdateTimerTick
		# 
		# playerinv
		# 
		self._playerinv.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._playerinv.Location = System.Drawing.Point(426, 350)
		self._playerinv.Name = "playerinv"
		self._playerinv.Size = System.Drawing.Size(28, 23)
		self._playerinv.TabIndex = 9
		self._playerinv.Text = "X"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(984, 461)
		self.Controls.Add(self._playerinv)
		self.Controls.Add(self._Shelf3)
		self.Controls.Add(self._Shelf2)
		self.Controls.Add(self._DebugBox)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._Radio)
		self.Controls.Add(self._Cabnet)
		self.Controls.Add(self._Shelf)
		self.Controls.Add(self._player)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgrammingI_Final"
		self.Load += self.MainFormLoad
		self.KeyDown += self.MainFormKeyDown
		self.KeyUp += self.MainFormKeyUp
		self.ResumeLayout(False)

	def Proximity(self, X1, X2, Y1, Y2): 
		d = math.sqrt(((X2-X1)**2) + ((Y2-Y1)**2))
		return d 

	def unpause(self):
		self.menuflag = False 
		self.playflagleft = False 
		self.playflagup = False 
		self.playflagright = False 
		self.playflagdown  = False 
		pass
		

	def TscrollTick(self, sender, e):
		if self.menuflag == False: 
			if self.playflagleft == True: 
				self._player.Left -= 3
				self._playerinv.Left -= 3
				pass
			elif self.playflagup == True: 
				self._player.Top -= 3
				self._playerinv.Top -= 3
				pass 
			elif self.playflagright == True:
				self._player.Left += 3
				self._playerinv.Left += 3
				pass
			elif self.playflagdown == True: 
				self._player.Top += 3
				self._playerinv.Top += 3
				pass
		else: 
			pass 
		if self._player.Top <= 20:
			self._player.Top += 3
			self._playerinv.Top += 3
		elif self._player.Left <= 20:
			self._player.Left += 3
			self._playerinv.Left += 3
		elif self._player.Bottom >= 480:
			self._player.Top -= 3
			self._playerinv.Top -= 3
		elif self._player.Left >= 950:
			self._player.Left -= 3
			self._playerinv.Left -= 3

	def MainFormLoad(self, sender, e):
		pass

	def MainFormKeyDown(self, sender, e):
				
		if e.KeyCode == Keys.A:
			self.playflagleft = True 
		elif e.KeyCode == Keys.W:
			self.playflagup = True 
		elif e.KeyCode == Keys.D:
			self.playflagright = True 
		elif e.KeyCode == Keys.S:
			self.playflagdown  = True 
			pass

	def MainFormKeyUp(self, sender, e):
		
		if e.KeyCode == Keys.A:
			self.playflagleft = False 
		elif e.KeyCode == Keys.W:
			self.playflagup = False 
		elif e.KeyCode == Keys.D:
			self.playflagright = False 
		elif e.KeyCode == Keys.S:
			self.playflagdown  = False 
			pass
		
		pass
	
	

	def Label2Click(self, sender, e):
		self._label2.Text = "Clicked" 
		
		pass


	def Label4Click(self, sender, e):
		#Radio click 
		dist = self.Proximity(self._player.Top+32, self.radloc[0], self._player.Right-16, self.radloc[1])
		if dist <= self.intdist:
			self.menu2.Show()
			self.menuflag = True 
		pass

	############################ CABNET FUNCTIONS ###########################################

	def CabnetClick(self, sender, e):
		dist = self.Proximity(self._player.Top+32, self.cabloc[0], self._player.Right-16, self.cabloc[1])
		if dist <= self.intdist:
			self.menu.Show()
			self.menuflag = True 
		else:
			self._DebugBox.Text = "Too far away!" 
		pass
	def Cab1Click(self):
		self.store.band_to_player()
		pass
	def Cab2Click(self):
		self.store.morp_to_player()
		pass
	def Cab3Click(self):
		self.store.spli_to_player()
		pass
	def Cab4Click(self):
		self.store.heldreturn()

	
	############################ STORAGE FUNCTIONS ###########################################
	
	def updatestore(self, bandage, morphine, splint, playerinv):
		band = bandage 
		morp = morphine 
		spli = splint 
		inv = playerinv
		self._Shelf.Text = str(" B ") * band 
		self._Shelf2.Text = str(" M ") * morp 
		self._Shelf3.Text = str(" S ") * spli 
		self._playerinv.Text = str(inv)
		
	def storeerror(self, message): 
		msg = message 
		self._DebugBox.Text = str(msg) 
		

	def UpdateTimerTick(self, sender, e):
		self.store.storeupdate()
		pass
	
	def ProgressBarAdd(self):
		self.ProgressBar1.inc		 
	
	
	def ProgressBar1Click(self, sender, e):
		pass