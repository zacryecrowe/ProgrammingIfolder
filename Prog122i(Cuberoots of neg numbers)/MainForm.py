import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(223, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 30)
		self._button3.TabIndex = 13
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(127, 12)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 30)
		self._button2.TabIndex = 12
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(31, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 30)
		self._button1.TabIndex = 11
		self._button1.Text = "Print"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 20
		self._listBox1.Location = System.Drawing.Point(22, 48)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(300, 204)
		self._listBox1.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(362, 283)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122i(Cuberoots of neg numbers)"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number \t Cube Root \t Cube"
		self._listBox1.Items.Add(header) 
		for num in range (-25,26): 
			if num < 0:
				root = -(round((abs(num)**(1./3)),5))
			else: 
				root = (round((num**(1./3)),5))
			cube = (num**3) 
			msg = str(num) + "\t  " + str(root) + "\t\t" + str(cube) 
			self._listBox1.Items.Add(msg) 
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear() 
		pass

	def Button3Click(self, sender, e):
		Application.Exit() 
		pass