import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.White
		self._checkBox1.ForeColor = System.Drawing.Color.Black
		self._checkBox1.Location = System.Drawing.Point(6, 19)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "checkBox1"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(115, 114)
		self._groupBox1.TabIndex = 1
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Controls.Add(self._checkBox2)
		self._groupBox2.Controls.Add(self._checkBox1)
		self._groupBox2.Location = System.Drawing.Point(147, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(115, 114)
		self._groupBox2.TabIndex = 2
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "groupBox2"
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.White
		self._checkBox2.ForeColor = System.Drawing.Color.Black
		self._checkBox2.Location = System.Drawing.Point(5, 49)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "checkBox2"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.White
		self._checkBox3.ForeColor = System.Drawing.Color.Black
		self._checkBox3.Location = System.Drawing.Point(5, 79)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "checkBox3"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 129)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(250, 62)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.White
		self._radioButton1.ForeColor = System.Drawing.Color.Black
		self._radioButton1.Location = System.Drawing.Point(7, 21)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "radioButton1"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.White
		self._radioButton2.ForeColor = System.Drawing.Color.Black
		self._radioButton2.Location = System.Drawing.Point(5, 48)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "radioButton2"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.White
		self._radioButton3.ForeColor = System.Drawing.Color.Black
		self._radioButton3.Location = System.Drawing.Point(5, 78)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "radioButton3"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(19, 194)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 33)
		self._button1.TabIndex = 4
		self._button1.Text = "Done"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(100, 194)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 33)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(182, 194)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 33)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg247(RadioButtonsOhBoyYayyyyy)"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True: 
			msg = "You selected choice 1" 
		elif self._radioButton2.Checked == True: 
			msg = "You selected choice 2"
		elif self._radioButton3.Checked == True: 
			msg = "You selected choice 3"

		if self._checkBox1.Checked == True: 
			msg += " and choice 4" 
		if self._checkBox2.Checked == True: 
			msg += " and choice 5"
		if self._checkBox3.Checked == True: 
			msg += " and choice 6"
			
		self._label1.Text = msg
		
		pass

	def Button2Click(self, sender, e):
		self._radioButton1.Checked = True
		self._radioButton2.Checked = False
		self._radioButton3.Checked = False
		self._checkBox1.Checked = False
		self._checkBox2.Checked = False
		self._checkBox3.Checked = False
		msg = "" 
		self._label1.Text = "" 
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass