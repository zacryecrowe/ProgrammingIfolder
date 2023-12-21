import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(181, 226)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Location = System.Drawing.Point(100, 226)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Location = System.Drawing.Point(19, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 18
		self._button1.Text = "Calc"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(19, 8)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 21
		self._label1.Text = "Pacakge A"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(19, 36)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 22
		self._label2.Text = "Pacakge B"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(19, 64)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 23
		self._label3.Text = "Pacakge C"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(137, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 25
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(137, 39)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 26
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(137, 67)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 27
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(19, 105)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(218, 102)
		self._label4.TabIndex = 28
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg269(SoftwareSales)"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		CA = 99
		CB = 199
		CC = 299
		SA = int(self._textBox1.Text)
		SB = int(self._textBox2.Text)
		SC = int(self._textBox3.Text)
		DA = 0
		DB = 0
		DC = 0
		if SA >= 10 and SA < 20: 
			DA = .80
		elif SA >= 20 and SA < 50:
			DA = .70
		elif SA >= 50 and SA < 100: 
			DA = .60 
		elif SA >= 100: 
			DA = .5 
		else: 
			DA = 1
		if SB >= 10 and SB < 20: 
			DB = .80
		elif SB >= 20 and SB < 50:
			DB = .70
		elif SB >= 50 and SB < 100: 
			DB = .60 
		elif SB >= 100: 
			DB = .5 
		else: 
			DB = 1
		if SC >= 10 and SC < 20: 
			DC = .80
		elif SC >= 20 and SC < 50:
			DC = .70
		elif SC >= 50 and SC < 100: 
			DC = .60 
		elif SC >= 100: 
			DC = .5 
		else: 
			DC = 1
			
		
		GA = CA*SA*DA
		GB = CB*SB*DB
		GC = CC*SC*DC
		Total = GA+GB+GC
		self._label4.Text = "\nPackage A: $" + str(GA) + "\nPackage B: $" + str(GB) + "\nPackage C: $" + str(GC) + "\nTotal: $" + str(Total)
		
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label4.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass