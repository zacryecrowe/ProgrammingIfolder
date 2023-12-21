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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(180, 291)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 23
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Location = System.Drawing.Point(99, 291)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 22
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Location = System.Drawing.Point(18, 291)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 21
		self._button1.Text = "Calc"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(30, 33)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(62, 23)
		self._label1.TabIndex = 24
		self._label1.Text = "Runner 1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(30, 66)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(62, 23)
		self._label2.TabIndex = 25
		self._label2.Text = "Runner 2"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(30, 98)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(62, 23)
		self._label3.TabIndex = 26
		self._label3.Text = "Runner 3"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(95, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(62, 23)
		self._label4.TabIndex = 27
		self._label4.Text = "Name"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(163, 9)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(75, 23)
		self._label5.TabIndex = 28
		self._label5.Text = "Race Time (s)"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(99, 35)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(58, 20)
		self._textBox1.TabIndex = 29
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(99, 68)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(58, 20)
		self._textBox2.TabIndex = 30
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(99, 100)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(58, 20)
		self._textBox3.TabIndex = 31
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(163, 36)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(75, 20)
		self._textBox4.TabIndex = 32
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(163, 69)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(75, 20)
		self._textBox5.TabIndex = 33
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(163, 101)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(75, 20)
		self._textBox6.TabIndex = 34
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(52, 135)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(144, 23)
		self._label6.TabIndex = 35
		self._label6.Text = "Results"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(31, 240)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(62, 23)
		self._label7.TabIndex = 38
		self._label7.Text = "3rd Place"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(31, 208)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(62, 23)
		self._label8.TabIndex = 37
		self._label8.Text = "2nd Place"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.White
		self._label9.Location = System.Drawing.Point(31, 175)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(62, 23)
		self._label9.TabIndex = 36
		self._label9.Text = "1st Place"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.White
		self._label10.Location = System.Drawing.Point(99, 175)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(97, 23)
		self._label10.TabIndex = 39
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.White
		self._label11.Location = System.Drawing.Point(99, 208)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(97, 23)
		self._label11.TabIndex = 40
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.White
		self._label12.Location = System.Drawing.Point(99, 240)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(97, 23)
		self._label12.TabIndex = 41
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(268, 326)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
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
		self.Text = "pg269(race)"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		R1 = [str(self._textBox1.Text), int(self._textBox4.Text)]
		R2 = [str(self._textBox2.Text), int(self._textBox5.Text)]
		R3 = [str(self._textBox3.Text), int(self._textBox6.Text)]
		if R1[1] < R2[1] and R1[1] < R3[1]:
			if R2[1] < R3[1]: 
				self._label10.Text = R1[0]
				self._label11.Text = R2[0]
				self._label12.Text = R3[0]
			else: 
				self._label10.Text = R1[0]
				self._label11.Text = R3[0]
				self._label12.Text = R2[0]
		elif R2[1] < R1[1] and R2[1] < R3[1]:
			if R1[1] < R3[1]: 
				self._label10.Text = R2[0]
				self._label11.Text = R1[0]
				self._label12.Text = R3[0]
			else: 
				self._label10.Text = R2[0]
				self._label11.Text = R3[0]
				self._label12.Text = R1[0]
		else: 
			if R1[1] < R2[1]: 
				self._label10.Text = R3[0]
				self._label11.Text = R1[0]
				self._label12.Text = R2[0]
			else: 
				self._label10.Text = R3[0]
				self._label11.Text = R2[0]
				self._label12.Text = R1[0]
				
				
						 					
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = "" 
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._textBox5.Text = ""
		self._textBox6.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		
		
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass