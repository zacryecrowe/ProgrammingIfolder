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
		self._Player = System.Windows.Forms.Label()
		self._Paddle = System.Windows.Forms.Label()
		self._timerPlay = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# Player
		# 
		self._Player.BackColor = System.Drawing.Color.White
		self._Player.Location = System.Drawing.Point(505, 544)
		self._Player.Name = "Player"
		self._Player.Size = System.Drawing.Size(40, 40)
		self._Player.TabIndex = 0
		# 
		# Paddle
		# 
		self._Paddle.BackColor = System.Drawing.Color.White
		self._Paddle.Location = System.Drawing.Point(475, 496)
		self._Paddle.Name = "Paddle"
		self._Paddle.RightToLeft = System.Windows.Forms.RightToLeft.Yes
		self._Paddle.Size = System.Drawing.Size(100, 25)
		self._Paddle.TabIndex = 1
		# 
		# timerPlay
		# 
		self._timerPlay.Enabled = True
		self._timerPlay.Interval = 1000
		self._timerPlay.Tick += self.TimerPlayTick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(988, 647)
		self.Controls.Add(self._Paddle)
		self.Controls.Add(self._Player)
		self.Name = "MainForm"
		self.Text = "ProgrammingFinal (Pong Redux)"
		self.ResumeLayout(False)
		
		
		
		
	def MainFormKeyDown(self, sender, e):
		#self._playflagleft  
		#self._playflagright 
		#self._playflagup 
		#self._playflagdown 
		
		if e.KeyCode == Keys.A:
			self.playflagleft = True 
		elif e.KeyCode == Keys.W:
			self.playflagright= True 
		elif e.KeyCode == Keys.D:
			self.playflagup  = True 
		elif e.KeyCode == Keys.S:
			self.playflagdown  = True 

			
		pass




	def TimerPlayTick(self, sender, e):
		#1 for cardinal 
		#0.707 for horizontal 
		if self.playflagleft == True: 
			pass
		elif self.playflagup == True: 
			player.Top -= 5
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
		pass