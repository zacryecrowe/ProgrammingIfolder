import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox1.Location = System.Drawing.Point(27, 23)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(142, 120)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Type of Membership"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Controls.Add(self._checkBox2)
		self._groupBox2.Controls.Add(self._checkBox1)
		self._groupBox2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox2.Location = System.Drawing.Point(189, 23)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(142, 100)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Options"
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._groupBox3.Controls.Add(self._label1)
		self._groupBox3.Controls.Add(self._textBox1)
		self._groupBox3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox3.Location = System.Drawing.Point(27, 149)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(142, 80)
		self._groupBox3.TabIndex = 1
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Membership Length"
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._groupBox4.Controls.Add(self._label5)
		self._groupBox4.Controls.Add(self._label4)
		self._groupBox4.Controls.Add(self._label3)
		self._groupBox4.Controls.Add(self._label2)
		self._groupBox4.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox4.Location = System.Drawing.Point(189, 129)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(142, 100)
		self._groupBox4.TabIndex = 2
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Membership Fees"
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._radioButton1.Location = System.Drawing.Point(7, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 16)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Adult Standard"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._radioButton2.Location = System.Drawing.Point(7, 41)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 16)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Child (under 12)"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._radioButton3.Location = System.Drawing.Point(6, 63)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 17)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Student"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._radioButton4.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._radioButton4.Location = System.Drawing.Point(6, 87)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(104, 16)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senior Citizen"
		self._radioButton4.UseVisualStyleBackColor = False
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._checkBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._checkBox1.Location = System.Drawing.Point(7, 16)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Yoga"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._checkBox2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._checkBox2.Location = System.Drawing.Point(7, 42)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Karate"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._checkBox3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._checkBox3.Location = System.Drawing.Point(7, 70)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Personal Trainer"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._textBox1.Location = System.Drawing.Point(11, 54)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label1.Location = System.Drawing.Point(11, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Enter # of Months"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label2.Location = System.Drawing.Point(7, 20)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(65, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Per Month"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label3.Location = System.Drawing.Point(7, 57)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(65, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Total"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label4.Location = System.Drawing.Point(78, 20)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(58, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "4"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label5.Location = System.Drawing.Point(78, 57)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(58, 23)
		self._label5.TabIndex = 5
		self._label5.Text = "5"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Location = System.Drawing.Point(36, 235)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(88, 28)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Location = System.Drawing.Point(130, 235)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(88, 28)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(224, 235)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(88, 28)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(356, 285)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg250(MonthlyFeeCalc)"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		fee = 0
		months = int(self._textBox1.Text)
		discount = 0
		if self._radioButton1.Checked == True:
			fee += 40 
		elif self._radioButton2.Checked == True:
			fee += 20
		elif self._radioButton3.Checked == True:
			fee += 25
		elif self._radioButton4.Checked == True:
			fee += 30
			
		if self._checkBox1.Checked == True:
			fee += 10 
		if self._checkBox2.Checked == True:
			fee += 30
		if self._checkBox3.Checked == True:
			fee += 50
			
		if months <= 3: 
			discout = 0 
		elif months > 3 and months <= 7: 
			discount = 0.05
		elif months > 7 and months <= 9:
			discout = 0.08
		elif months > 9: 
			discount = 0.1
			
		monthfee = fee-(fee*discount) 
		total = monthfee*months
		self._label4.Text = str(monthfee)
		self._label5.Text = str(total) 		

		pass

	def Button2Click(self, sender, e):
		self._radioButton1.Checked = True 
		self._radioButton2.Checked = False
		self._radioButton3.Checked = False
		self._radioButton4.Checked = False
		self._checkBox1.Checked = False
		self._checkBox2.Checked = False
		self._checkBox3.Checked = False
		self._label4.Text = "" 
		self._label5.Text = "" 
		
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass