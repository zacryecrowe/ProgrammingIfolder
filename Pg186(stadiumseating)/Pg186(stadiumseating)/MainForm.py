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
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(229, 173)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 17
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Location = System.Drawing.Point(148, 173)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 16
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Location = System.Drawing.Point(67, 173)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 15
		self._button1.Text = "Calc"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(25, 58)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(51, 23)
		self._label1.TabIndex = 18
		self._label1.Text = "ClassA"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(25, 86)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(51, 23)
		self._label2.TabIndex = 19
		self._label2.Text = "ClassB"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(25, 114)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(51, 23)
		self._label3.TabIndex = 20
		self._label3.Text = "ClassC"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(187, 114)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(51, 23)
		self._label4.TabIndex = 23
		self._label4.Text = "ClassC"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Location = System.Drawing.Point(187, 86)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(51, 23)
		self._label5.TabIndex = 22
		self._label5.Text = "ClassB"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Location = System.Drawing.Point(187, 58)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(51, 23)
		self._label6.TabIndex = 21
		self._label6.Text = "ClassA"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label7.Location = System.Drawing.Point(83, 30)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(98, 23)
		self._label7.TabIndex = 24
		self._label7.Text = "Tickets Sold"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label8.Location = System.Drawing.Point(239, 30)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(108, 23)
		self._label8.TabIndex = 25
		self._label8.Text = "Revenue Generated"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label9.Location = System.Drawing.Point(245, 58)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(102, 23)
		self._label9.TabIndex = 26
		self._label9.Text = "9"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label10.Location = System.Drawing.Point(245, 86)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(102, 23)
		self._label10.TabIndex = 27
		self._label10.Text = "10"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label11.Location = System.Drawing.Point(245, 114)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(102, 23)
		self._label11.TabIndex = 28
		self._label11.Text = "11"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(82, 60)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 29
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(81, 86)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 30
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(81, 116)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 31
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label12.Location = System.Drawing.Point(130, 142)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(108, 23)
		self._label12.TabIndex = 32
		self._label12.Text = "Total Revenue"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label13.Location = System.Drawing.Point(245, 142)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(102, 23)
		self._label13.TabIndex = 33
		self._label13.Text = "13"
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(385, 202)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg186(stadiumseating)"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		A_S = int(self._textBox1.Text) 
		B_S = int(self._textBox2.Text)
		C_S = int(self._textBox3.Text)
		A_R = (15 * A_S)		
		B_R = (12 * B_S)
		C_R = (9 * C_S)
		Rev = A_R + B_R + C_R 
		self._label9.Text = str(A_R)
		self._label10.Text = str(B_R)
		self._label11.Text = str(C_R)
		self._label13.Text = str(Rev)
		pass

	def Button2Click(self, sender, e):
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label13.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass