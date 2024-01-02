import math
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.playflagleft = False 
		self.playflagright = False
		self.playflagup = False
		self.playflagdown = False 
		
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._label1 = System.Windows.Forms.Label()
		self._player = System.Windows.Forms.Label()
		self._tscroll = System.Windows.Forms.Timer(self._components)
		self._CabnetInv = System.Windows.Forms.Label()
		self._Tspawn = System.Windows.Forms.Timer(self._components)
		self._Cabnet = System.Windows.Forms.Label()
		self._Radio = System.Windows.Forms.Label()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self._DebugBox = System.Windows.Forms.Label()
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
		# CabnetInv
		# 
		self._CabnetInv.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._CabnetInv.Location = System.Drawing.Point(638, 9)
		self._CabnetInv.Name = "CabnetInv"
		self._CabnetInv.Size = System.Drawing.Size(334, 52)
		self._CabnetInv.TabIndex = 2
		self._CabnetInv.Text = "XBX"
		self._CabnetInv.Click += self.Label2Click
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
		self._Cabnet.Location = System.Drawing.Point(544, 9)
		self._Cabnet.Name = "Cabnet"
		self._Cabnet.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._Cabnet.Size = System.Drawing.Size(88, 40)
		self._Cabnet.TabIndex = 3
		self._Cabnet.Text = "Medical Supplies"
		self._Cabnet.Click += self.CabnetClick
		# 
		# Radio
		# 
		self._Radio.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._Radio.ForeColor = System.Drawing.Color.Black
		self._Radio.Location = System.Drawing.Point(884, 90)
		self._Radio.Name = "Radio"
		self._Radio.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._Radio.Size = System.Drawing.Size(88, 43)
		self._Radio.TabIndex = 4
		self._Radio.Text = "Medical Requests"
		self._Radio.Click += self.Label4Click
		# 
		# progressBar1
		# 
		self._progressBar1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._progressBar1.Location = System.Drawing.Point(884, 64)
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(88, 23)
		self._progressBar1.TabIndex = 5
		# 
		# DebugBox
		# 
		self._DebugBox.BackColor = System.Drawing.SystemColors.ButtonFace
		self._DebugBox.Location = System.Drawing.Point(366, 105)
		self._DebugBox.Name = "DebugBox"
		self._DebugBox.Size = System.Drawing.Size(100, 23)
		self._DebugBox.TabIndex = 6
		self._DebugBox.Text = "DebugBox"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(984, 461)
		self.Controls.Add(self._DebugBox)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._Radio)
		self.Controls.Add(self._Cabnet)
		self.Controls.Add(self._CabnetInv)
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
		self._DebugBox.Text = str(d)

		

	def TscrollTick(self, sender, e):
		
		#1 for cardinal 
		#0.707 for horizontal 
		if self.playflagleft == True: 
			self._player.Left -= 3
			pass
		elif self.playflagup == True: 
			self._player.Top -= 3
			pass 
		elif self.playflagright == True:
			self._player.Left += 3
			pass
		elif self.playflagdown == True: 
			self._player.Top += 3
			pass

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
		pass

	def CabnetClick(self, sender, e):
		return self.Proximity(self._player.Top+32, self._Cabnet.Bottom-20, self._player.Right-16, self._Cabnet.Left+40)
		pass