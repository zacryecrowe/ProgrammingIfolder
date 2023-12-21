import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gray
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 48)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(221, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Speed Limit (MPH)"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Gray
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 75)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(221, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter Vehicle Speed (MPH)"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 141)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(93, 66)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(239, 45)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(131, 26)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(239, 72)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(131, 26)
		self._textBox2.TabIndex = 4
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(140, 142)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(93, 66)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(277, 142)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(93, 66)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gray
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 101)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(221, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Fine Amount Levied "
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(239, 101)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(131, 23)
		self._label4.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(382, 220)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog82a(trafficticketCorrect)"
		self.ResumeLayout(False)
		self.PerformLayout()

	
	def Button2Click(self, sender, e):
		self._textbox1.Text = "" 
		self._textbox2.Text = "" 
		self._label4.Text = "" 
		pass

	def Button3Click(self, sender, e):
		self._application.Exit() 
		pass

	def Button1Click(self, sender, e):
		Limit = int(self._textBox1.Text) 
		Speed = int(self._textBox2.Text) 
		Fine = float(20 + ((Speed-Limit)*5.00))
		self._label4.Text = str(Fine)
		pass