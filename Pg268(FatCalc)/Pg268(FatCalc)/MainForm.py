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
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(187, 180)
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
		self._button2.Location = System.Drawing.Point(106, 180)
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
		self._button1.Location = System.Drawing.Point(25, 180)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 18
		self._button1.Text = "Calc"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(13, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(178, 23)
		self._label1.TabIndex = 21
		self._label1.Text = "Enter amount of Calories in Food"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(13, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(178, 23)
		self._label2.TabIndex = 22
		self._label2.Text = "Enter amount of fat grams in Food"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(13, 106)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(178, 23)
		self._label3.TabIndex = 23
		self._label3.Text = "Percentage of calroies from fat"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(197, 106)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(66, 23)
		self._label4.TabIndex = 24
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Location = System.Drawing.Point(25, 145)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(238, 23)
		self._label5.TabIndex = 25
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(198, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(65, 20)
		self._textBox1.TabIndex = 26
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(198, 64)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(65, 20)
		self._textBox2.TabIndex = 27
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(284, 216)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg268(FatCalc)"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Cal = int(self._textBox1.Text)
		Fat = int(self._textBox2.Text)
		FatCal = float(Fat * 9) 
		Per = (FatCal/Cal)*100
		self._label4.Text = str(Per) + " %" 
		if Per < 30: 
			self._label5.Text = "Yay, this food is low in fat" 
		else:
			pass
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = "" 
		self._label5.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		
		
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass