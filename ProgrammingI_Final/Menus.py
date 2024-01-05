
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Menus(Form):
	def __init__(self,myparent):
		self.InitializeComponent()
		self.myparent = myparent
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 69)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(201, 33)
		self._button1.TabIndex = 0
		self._button1.Text = "Bandage (\"B\")"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(0, 1)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(225, 65)
		self._label1.TabIndex = 1
		self._label1.Text = "What do you want to grab from the stockpile? "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 108)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(201, 33)
		self._button2.TabIndex = 2
		self._button2.Text = "Morphine (\"M\")"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(12, 147)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(201, 33)
		self._button3.TabIndex = 3
		self._button3.Text = "Splint (\"S\")"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(12, 186)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(201, 33)
		self._button4.TabIndex = 4
		self._button4.Text = "Put Held Item Back"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# Menus
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(225, 246)
		self.ControlBox = False
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
		self.Name = "Menus"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Menus"
		self.TopMost = True
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Hide() 
		self.myparent.unpause()
		self.myparent.Cab1Click()

	def Button2Click(self, sender, e):
		self.Hide() 
		self.myparent.unpause() 
		self.myparent.Cab2Click()
	def Button3Click(self, sender, e):
		self.Hide() 
		self.myparent.unpause() 
		self.myparent.Cab3Click()
	def Button4Click(self, sender, e):
		self.Hide() 
		self.myparent.unpause()
		self.myparent.Cab4Click()		