import System.Drawing
import System.Windows.Forms
from _random import Random

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False
		self.flagball = False
		self.ballspeed = 8
		self.ballspeedM = 1
		self.Var = 0
		self.VarL = 0 
		self.flaglights = False 
		self.PspeedM = 1
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lbltitle = System.Windows.Forms.Label()
		self._leftscore = System.Windows.Forms.Label()
		self._rightscore = System.Windows.Forms.Label()
		self._lblball = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self._timerlight = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# lbltitle
		# 
		self._lbltitle.BackColor = System.Drawing.Color.Transparent
		self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.Color.White
		self._lbltitle.Location = System.Drawing.Point(12, 25)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(958, 52)
		self._lbltitle.TabIndex = 0
		self._lbltitle.Text = "Press Enter to Start or M to start multiplayer"
		self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# leftscore
		# 
		self._leftscore.BackColor = System.Drawing.Color.Transparent
		self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._leftscore.ForeColor = System.Drawing.Color.White
		self._leftscore.Location = System.Drawing.Point(78, 96)
		self._leftscore.Name = "leftscore"
		self._leftscore.Size = System.Drawing.Size(166, 109)
		self._leftscore.TabIndex = 1
		self._leftscore.Text = "0"
		self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# rightscore
		# 
		self._rightscore.BackColor = System.Drawing.Color.Transparent
		self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._rightscore.ForeColor = System.Drawing.Color.White
		self._rightscore.Location = System.Drawing.Point(734, 96)
		self._rightscore.Name = "rightscore"
		self._rightscore.Size = System.Drawing.Size(166, 109)
		self._rightscore.TabIndex = 2
		self._rightscore.Text = "0"
		self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblball
		# 
		self._lblball.BackColor = System.Drawing.Color.White
		self._lblball.Location = System.Drawing.Point(479, 304)
		self._lblball.Name = "lblball"
		self._lblball.Size = System.Drawing.Size(20, 20)
		self._lblball.TabIndex = 3
		self._lblball.Click += self.LblballClick
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.Color.White
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 4
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.Color.White
		self._lblright.Location = System.Drawing.Point(950, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 5
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# timerlight
		# 
		self._timerlight.Interval = 8000
		self._timerlight.Tick += self.Timer1Tick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(982, 590)
		self.Controls.Add(self._lblball)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._rightscore)
		self.Controls.Add(self._leftscore)
		self.Controls.Add(self._lbltitle)
		self.Name = "MainForm"
		self.Text = "Pong"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)


	def TimerballTick(self, sender, e):
		ball = self._lblball
		lpdl = self._lblleft
		rpdl = self._lblright
		rscore = int(self._rightscore.Text)
		lscore = int(self._leftscore.Text)
		ball.Top += self.ballup
		ball.Left += (self.ballspeed * self.balld) * self.ballspeedM
		
		if ball.Right >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4, 5)
		elif ball.Left <= lpdl.Right and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
			self.balld = 1
			self.ballup = self.R.Next(-4, 5)
		
		
		if ball.Location.X <= 0 or \
		   (ball.Location.X < lpdl.Left + 20 and ball.Location.Y < lpdl.Top):
		   	rscore += 1
		   	ball.Left = self.Width // 2
		   	ball.Top = self.Height // 2
		   	self._rightscore.Text = str(rscore)
		   	pass
		
		if ball.Location.X >= self.Width or \
		   (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top):
		   	lscore += 1
		   	ball.Left = self.Width // 2
		   	ball.Top = self.Height // 2
		   	self._leftscore.Text = str(lscore)
		
		
		if lscore == 10:  # Left win condition
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Left Player Wins! Press R to restart"
			
		if rscore == 10: 
			self._timerball.Enabled = False 
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2 
			self.ballup = 0 
			self._lbltitle.Visible = True 
			self._lbltitle.Text = "Right Player Wins! Press R to restart" 
		
		if ball.Location.Y <= 5: 
			ball.Top += 20
			self.ballup *= -1
		elif ball.Location.Y >= self.Height-30:
			ball.Top -= 20
			self.ballup *= -1
		
		if self._timerlight.Enabled == True:
			self.VarL += 1 
			if self.VarL >= 74:
					if self._lblball.BackColor == Color.White:
						self._lblball.BackColor = Color.Black
					elif self._lblball.BackColor == Color.Black:
						self._lblball.BackColor = Color.White
					self.VarL = 0
			
			
		if self._timerboolean.Enabled == True:
				self.Var += 1
				if self.Var >= 20:
					if lpdl.Top+80 > ball.Location.Y: 
						self.flagleft = False 
					elif lpdl.Top+30 <= ball.Location.Y: 
						self.flagleft = True 
				if self.Var >= 25:
					self.Var = 1
					lpdl.BackColor = Color.White
		if self._timerboolean.Enabled == True and self.flagleft == True: 
			lpdl.Top += (5 * self.PspeedM)
		elif self._timerboolean.Enabled == True and self.flagleft == False: 
			lpdl.Top -= (5 * self.PspeedM)
		"""			
		if lpdl.Top > 0 and lpdl.Top < self.Height - 150:
			if self.flagleft == True:
				lpdl.Top += 5
			elif self.flagleft == False: 
				lpdl.Top -= 5
		elif lpdl.Top <= 0:
			lpdl.Top += 5 
		elif lpdl.Top > self.Height-150:
			lpdl.Top -= 5
		"""
				
			

			

	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmult = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self._lblball
		lblf = self._lblleft
		lblrt = self._lblright
		tlights = self._timerlight
		
		def reset():
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text = "0"
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmult.Enabled = False
			tleft.Enabled = False
			tright.Enabled = False
			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			lblf.Top = (self.Height // 2) - 100 + self._lblleft.Height
			lblrt.Top = (self.Height // 2) - 100 + self._lblright.Height
			self.ballspeed = 8
			self.ballspeedM = 1
			""" TODO: RESET SECRETS """
			bl.BackColor = Color.White
			self.BackColor = Color.Black
			self._timerlight.Enabled = False
			self.PspeedM = 1
		
		if e.KeyCode == Keys.R:
			reset()
			
		if e.KeyCode == Keys.NumPad1:
			self.ballspeedM += .1
		if e.KeyCode == Keys.NumPad0:
			if self.ballspeedM >= .2:
				self.ballspeedM -= .1 
		if e.KeyCode == Keys.NumPad2:
			self._timerlight.Enabled = True 	
		if e.KeyCode == Keys.NumPad3:
			self.PspeedM += .1 
		if e.KeyCode == Keys.NumPad4:
			if self.PspeedM >= .2:
				self.PspeedM -= .1 

				 
		""" TODO: SECRET CONTROL """

	
		if e.KeyCode == Keys.M:
			reset()
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Use W and S to move the left paddle; hit Enter to begin"
			tmult.Enabled = True
		if  e.KeyCode == Keys.Enter:
			if tmult.Enabled == True:
				self._lbltitle.Visible = False
				tbool.Enabled = False
				tmult.Enabled = True
				tdum.Enabled = False
				tball.Enabled = True
			else: 
				self._lbltitle.Visible = False
				tball.Enabled = True
				tdum.Enabled = True
				tbool.Enabled = True
				self._lbltitle.Visible = False
				

		
		
		if tdum.Enabled:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.KeyCode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
			#elif tright.Enabled and self.flagright == False:
				#tright.Enabled = False
			if e.KeyCode == Keys.NumPad2:
				self.flaglights = True
		
		""" TODO: FINISH MULTIPLAYER CONTROLS """
		if tmult.Enabled and tball.Enabled:
			
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.KeyCode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
		#	elif tright.Enabled:
				#tright.Enabled = False
		if tmult.Enabled and tball.Enabled:
			
			if e.KeyCode == Keys.W:
				self.flagleft = False
				tleft.Enabled = True
			elif e.KeyCode == Keys.S:
				self.flagleft = True 
				tleft.Enabled = True
			#elif tleft.Enabled:
				#tleft.Enabled = False
				pass

	def MainFormLoad(self, sender, e):
		""" TODO: ADD 3 UNIQUE SECRETS/CHEATS/EASTER EGGS IN TOTAL
		AND FINISH MULTIPLAYER AND SCOREBOARD AND DUMMY AI """
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
		self._timerball.Enabled = False
		self._timerdummy.Enabled = False
		self._timermulti.Enabled = False
		
	
	def pdlTick(self, pdl, flagd, tmr):
		if pdl.Top > 0 and pdl.Top < self.Height - 150:
			if flagd == True:
				pdl.Top += (5 * self.PspeedM)
			if flagd == False:
				pdl.Top -= (5 * self.PspeedM)
			if pdl.Top <= 10:
				tmr.Enabled = False
			if pdl.Top >= self.Height - 150:
				tmr.Enabled = False
		elif pdl.Top <= 0:
			pdl.Top += 5 
		else:
			pdl.Top -= 5
	# pdl.Top >= self.Height -150 : 
				

	def TimerleftTick(self, sender, e):
		self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

	def TimerrightTick(self, sender, e):
		self.pdlTick(self._lblright, self.flagright, self._timerright)

	def LblballClick(self, sender, e):
		self._lblball.BackColor = Color.Red
		""" TODO: PUT MORE EASTER EGGS LATER """
		self.BackColor = Color.Green

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblball.Left = self.Width // 2
		self._lblball.Top = self.Height // 2
		self._lbltitle.Width = self.Width - 25
		self._rightscore.Left = self.Width - 75 - self._rightscore.Width
	def Timer1Tick(self, sender, e):
		pass