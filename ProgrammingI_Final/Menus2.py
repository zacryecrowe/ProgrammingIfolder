
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Menus2(Form):
	def __init__(self,myparent):
		self.InitializeComponent()
		self.myparent = myparent	
		self.requestFlag = False 
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(12, 146)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(190, 33)
		self._button3.TabIndex = 7
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(13, 107)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(190, 33)
		self._button2.TabIndex = 6
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(-3, 0)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(225, 65)
		self._label1.TabIndex = 5
		self._label1.Text = "What do you want to request?"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 68)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(190, 33)
		self._button1.TabIndex = 4
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Menus2
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(215, 192)
		self.ControlBox = False
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.MaximizeBox = False
		self.Name = "Menus2"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Menus2"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		if self.requestFlag == False:
			self.Hide()
			self.myparent.Rad1Click()
			self.myparent.unpause() 
		elif self.requestFlag == True:
			#self.myparent.storeerror("You already requested something! Supplies are on the way!") 
			self.Hide()		
			self.myparent.unpause() 			
		pass

	def Button2Click(self, sender, e):
		if self.requestFlag == False:
			self.Hide()
			self.myparent.Rad2Click()
			self.myparent.unpause()
		elif self.requestFlag == True:
			self.myparent.storeerror("You already requested something! Supplies are on the way!") 
			self.Hide()		
			self.myparent.unpause() 			
		pass

	def Button3Click(self, sender, e):
		if self.requestFlag == False:
			self.Hide()
			self.myparent.Rad3Click()
			self.myparent.unpause()
		elif self.requestFlag == True:
			self.myparent.storeerror("You already requested something! Supplies are on the way!") 
			self.Hide()		
			self.myparent.unpause() 			
		pass
	
	def FlagOn(self): 
		self.requestFlag = True
		
	def FlagOff(self): 
		self.requestFlag = False