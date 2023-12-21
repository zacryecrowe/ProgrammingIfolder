import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(87, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 40)
		self._button1.TabIndex = 0
		self._button1.Text = "Print"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 15
		self._listBox1.Location = System.Drawing.Point(27, 59)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(429, 274)
		self._listBox1.TabIndex = 1
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(182, 12)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(89, 40)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(277, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(89, 40)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(481, 345)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Prog122h(roots+cubes)"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number\tSquare\tSquare_Root\tCube\tFourth_Root" 
		self._listBox1.Items.Add(header)
		for num in range (1,21): 
			square = num**2
			square_root = round(math.sqrt(num),4) 
			cube = num**3
			four_root = round(math.sqrt(math.sqrt(num)),4)
			msg = str(num) + "\t" + str(square) + "\t" + str(square_root) + "\t\t" + str(cube) + "\t" + str(four_root)
			self._listBox1.Items.Add(msg) 
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear() 
		pass

	def Button3Click(self, sender, e):
		Application.Exit() 
		pass