import math
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *
from Menus import * 
from Menus2 import * 
from store import * 
from Patients import * 
class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		#ToggleFlags
		self.playflagleft = False 
		self.playflagright = False
		self.playflagup = False
		self.playflagdown = False
		self.menuflag = False
		self.requestFlag = False
		#######Game Vars
		#distance to objects where they become interactable 
		self.intdist = 125
		self.requesttype = 0
		self.counter = 0
		self.delivertime = 45 
		#Center of Objects for Prox function. Each is first 3 letters of word with loc after
		self.playloc = [self._player.Top+32, self._player.Right-16]
		self.cabloc = [self._Cabnet.Bottom-25, self._Cabnet.Right-50]
		self.radloc = [self._Radio.Bottom-25, self._Radio.Right-50]
		#self.bed1loc = [self._Bed1.Top+44, self._Bed1.Right-36]		
		###### All Patient Stuff ######## 
		
		patients = []
		
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
		self._ProgressBar1 = System.Windows.Forms.ProgressBar()
		self._DebugBox = System.Windows.Forms.Label()
		self._Shelf2 = System.Windows.Forms.Label()
		self._Shelf3 = System.Windows.Forms.Label()
		self._UpdateTimer = System.Windows.Forms.Timer(self._components)
		self._playerinv = System.Windows.Forms.Label()
		self._TrequestTimer = System.Windows.Forms.Timer(self._components)
		self._Bed2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._progressBar2 = System.Windows.Forms.ProgressBar()
		self._label2 = System.Windows.Forms.Label()
		self._TBattle = System.Windows.Forms.Timer(self._components)
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
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
		self._player.Location = System.Drawing.Point(416, 198)
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
		# ProgressBar1
		# 
		self._ProgressBar1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._ProgressBar1.Location = System.Drawing.Point(872, 97)
		self._ProgressBar1.MarqueeAnimationSpeed = 1
		self._ProgressBar1.Maximum = 45
		self._ProgressBar1.Name = "ProgressBar1"
		self._ProgressBar1.Size = System.Drawing.Size(100, 23)
		self._ProgressBar1.Step = 1
		self._ProgressBar1.TabIndex = 5
		self._ProgressBar1.Click += self.ProgressBar1Click
		# 
		# DebugBox
		# 
		self._DebugBox.BackColor = System.Drawing.SystemColors.ButtonFace
		self._DebugBox.Location = System.Drawing.Point(712, 279)
		self._DebugBox.Name = "DebugBox"
		self._DebugBox.Size = System.Drawing.Size(260, 162)
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
		self._playerinv.Location = System.Drawing.Point(416, 228)
		self._playerinv.Name = "playerinv"
		self._playerinv.Size = System.Drawing.Size(28, 23)
		self._playerinv.TabIndex = 9
		self._playerinv.Text = "X"
		# 
		# TrequestTimer
		# 
		self._TrequestTimer.Interval = 1000
		self._TrequestTimer.Tick += self.TrequestTimerTick
		# 
		# Bed2
		# 
		self._Bed2.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._Bed2.ForeColor = System.Drawing.Color.Black
		self._Bed2.Location = System.Drawing.Point(137, 177)
		self._Bed2.Name = "Bed2"
		self._Bed2.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._Bed2.Size = System.Drawing.Size(70, 86)
		self._Bed2.TabIndex = 11
		self._Bed2.Text = "Bed1"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(26, 418)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(195, 34)
		self._button1.TabIndex = 12
		self._button1.Text = "Patient Menu"
		self._button1.UseVisualStyleBackColor = True
		# 
		# progressBar2
		# 
		self._progressBar2.Location = System.Drawing.Point(333, 418)
		self._progressBar2.Name = "progressBar2"
		self._progressBar2.Size = System.Drawing.Size(363, 34)
		self._progressBar2.TabIndex = 13
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
		self._label2.Location = System.Drawing.Point(227, 418)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 34)
		self._label2.TabIndex = 14
		self._label2.Text = "Battle Progress"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# TBattle
		# 
		self._TBattle.Enabled = True
		self._TBattle.Interval = 1000
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label3.Location = System.Drawing.Point(213, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(21, 23)
		self._label3.TabIndex = 15
		self._label3.Text = "0"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(120, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(87, 23)
		self._label4.TabIndex = 16
		self._label4.Text = "Patients Waiting: "
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(984, 461)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._progressBar2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._Bed2)
		self.Controls.Add(self._playerinv)
		self.Controls.Add(self._Shelf3)
		self.Controls.Add(self._Shelf2)
		self.Controls.Add(self._DebugBox)
		self.Controls.Add(self._ProgressBar1)
		self.Controls.Add(self._Radio)
		self.Controls.Add(self._Cabnet)
		self.Controls.Add(self._Shelf)
		self.Controls.Add(self._player)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgrammingI_Final"
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
		
		
	def MainFormKeyDown(self, sender, e):
		if e.KeyCode == Keys.A:
			self.playflagleft = True 
		pass

	def MainFormKeyUp(self, sender, e):
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
			
	def Label4Click(self, sender, e):
		#Radio click 
		dist = self.Proximity(self._player.Top+32, self.radloc[0], self._player.Right-16, self.radloc[1])
		if dist <= self.intdist:
			self.menu2.Show()
			self.menuflag = True 
			
	############################ CABNET FUNCTIONS ###########################################

	def CabnetClick(self, sender, e):
		dist = self.Proximity(self._player.Top+32, self.cabloc[0], self._player.Right-16, self.cabloc[1])
		if dist <= self.intdist:
			self.menu.Show()
			self.menuflag = True 
		else:
			self._DebugBox.Text = "Too far away!" 
			
	def Cab1Click(self):
		self.store.band_to_player()
		
	def Cab2Click(self):
		self.store.morp_to_player()
		
	def Cab3Click(self):
		self.store.spli_to_player()
		
	def Cab4Click(self):
		self.store.heldreturn()
		
	def Rad1Click(self):
		self._TrequestTimer.Enabled = True
		self.menu2.FlagOn()
		self.requesttype = 1		
		
	def Rad2Click(self):
		self._TrequestTimer.Enabled = True
		self.menu2.FlagOn()  
		self.requesttype = 2
		
	def Rad3Click(self):
		self._TrequestTimer.Enabled = True
		self.menu2.FlagOn() 
		self.requesttype = 3		
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

	def TrequestTimerTick(self, sender, e):
		self.counter += 1
		self._ProgressBar1.Increment(1) 		
		self.TimerChecker() 
	
	def TimerChecker(self):
		self.storeerror(str(self.counter))	
		type = self.requesttype 		 
		if self.counter >= 30:
			self.storeerror(str(self.requesttype))			 
			if type == 1:
				self.store.bandrequest()
				self.requesttype = 0
				self.storeerror("Bandage Request Sent!")
				self.requestreset()
			elif type == 2: 
				self.store.morprequest()
				self.requesttype = 0
				self.storeerror("Morphine Request Sent!")
				self.requestreset()
			elif type == 3:
				self.store.splirequest()
				self.requesttype = 0
				self.storeerror("Splint Request Sent!")
				self.requestreset()

	def requestreset(self):
		self.counter = 0 
		self.menu2.FlagOff()
		self._TrequestTimer.Enabled = False
		self._ProgressBar1.Increment(-30)
		pass
<<<<<<< Updated upstream
########## BED NONSENSE #################### 
=======
#Bed 
	def Label2Click(self, sender, e):
		self._label2.Text = "Clicked" 
#Bed1		
	def Label9Click(self, sender, e):
		self.storeerror("Bed Click!")
		pass
	#Bed2
	def Label3Click(self, sender, e):
		pass
>>>>>>> Stashed changes

########## PATIENT NONSENSE #################### 

class Patient:
    def __init__(self, name, rank, wounds, ):
        self.name = name
        self.rank = rank
        self.wounds = wounds
      
    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def getWounds(self):
        return self.wounds

    def getRandomName():
        names = ["S.Franciszek", "Y.Dor","N.Jozef","S.Edmund","G.Gallagher","H.Iago",
                 "A.Vitaliy","O.Langdon","E.Bertrand","I.Dayton","J.Osborne","R.Herschel",
                 "O.Wright","T.Graciano","J.Goodwin","M.Hallsteinn","M.O'Bren"]
        return random.choice(names)

    def getRandomRank():
        ranks = ["Private", "Corporal","Sergeant","PFC.","W.O."]
        return random.choice(ranks)

    def getRandomWounds():
      ### Possible Wounds 
      Gunshot = ["Gunshot-","Band",7] 
      Shrapnel = ["Shrapnel","Band",5]
      Scrapes = ["Scrapes","Band",3]
      Shock = ["Shock","Morp",7]
      Fractures = ["Fractures","Spli",2]
      Broken_Bones = ["Broken_Bones","Spli",5]
      Mangled_Limb = ["Mangled_Limb","Surg",10]
      Wounds = [] 
      Pos = [Gunshot, Shrapnel,Scrapes,Shock,Fractures,Broken_Bones,Mangled_Limb]
      Rand = [1,2,3,4,5] 
      num = random.choice(Rand)
      for i in range (num): 
        Wounds.append(random.choice(Pos))
      return Wounds

    def createRandomPatient():
        name = Patient.getRandomName()
        rank = Patient.getRandomRank()
        wounds = Patient.getRandomWounds()
        return Patient(name, rank, wounds,)




#### TEST STUFF###
#num_patients = 4

#for _ in range(num_patients):
 #   patients.append(Patient.createRandomPatient())



#for patient in patients:
   # print(f"Name: {patient.getName()}, Rank: {patient.getRank()}, Wounds: {patient.getWounds()}")
