
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Patients(Form):
<<<<<<< Updated upstream
	def __init__(self, myparent):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._button5 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(15, 151)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(61, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Patient 1 "
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(93, 151)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(61, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Patient 2 "
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(171, 151)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(61, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Patient 3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(249, 151)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(61, 23)
		self._button4.TabIndex = 3
		self._button4.Text = "Patient 4"
		self._button4.UseVisualStyleBackColor = True
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(375, 132)
		self._groupBox1.TabIndex = 4
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Overview"
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(327, 151)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(61, 23)
		self._button5.TabIndex = 5
		self._button5.Text = "Patient 5"
		self._button5.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(92, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Num of Patients"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(96, 20)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(45, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "0"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._groupBox2.Location = System.Drawing.Point(15, 180)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(375, 146)
		self._groupBox2.TabIndex = 5
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Patient"
		# 
		# Patients
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(400, 342)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "Patients"
		self.Text = "Patients"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
=======
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self.SuspendLayout()
		# 
		# Patients
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Name = "Patients"
		self.Text = "Patients"
		self.Load += self.PatientsLoad
		self.ResumeLayout(False)









	def PatientsLoad(self, sender, e):
>>>>>>> Stashed changes
		pass