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
		self._label2 = System.Windows.Forms.Label()
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
		self._player.Size = System.Drawing.Size(33, 95)
		self._player.TabIndex = 1
		self._player.Text = "player"
		# 
		# tscroll
		# 
		self._tscroll.Enabled = True
		self._tscroll.Interval = 10
		self._tscroll.Tick += self.TscrollTick
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(426, 106)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Output"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(984, 461)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._player)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgrammingI_Final"
		self.Load += self.MainFormLoad
		self.KeyDown += self.MainFormKeyDown
		self.KeyUp += self.MainFormKeyUp
		self.ResumeLayout(False)



	def TscrollTick(self, sender, e):
		
		#1 for cardinal 
		#0.707 for horizontal 
		if self.playflagleft == True: 
			pass
		elif self.playflagup == True: 
			self._player.Top -= 3
			self._label2.Text = "pressing W"
		elif self.playflagright == True:
			pass
		elif self.playflagdown == True: 
			pass
		elif self.playflagleft == True and self.playflagup == True: 
			pass
		elif self.playflagup == True and self.playflagright == True:
			pass 
		elif self.playflagright == True and self.playflagdown == True:
			pass 
		elif self.playflagdown == True and self.playflagleft == True:
			pass

	def MainFormLoad(self, sender, e):
		pass

	def MainFormKeyDown(self, sender, e):
		
		
		
				
		if e.KeyCode == Keys.A:
			self.playflagleft = True 
		elif e.KeyCode == Keys.W:
			self.playflagup = True 
			#self._label2.Text = "pressing W"
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
			#self._label2.Text = "pressing W"
		elif e.KeyCode == Keys.D:
			self.playflagright = False 
		elif e.KeyCode == Keys.S:
			self.playflagdown  = False 
			pass

		pass