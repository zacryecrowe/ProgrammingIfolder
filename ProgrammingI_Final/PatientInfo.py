
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class PatientInfo(Form):
	def __init__(self, my parent):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label1.Location = System.Drawing.Point(12, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(69, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "NAME: "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label2.Location = System.Drawing.Point(12, 57)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(69, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "RANK "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 112)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(263, 186)
		self._listBox1.TabIndex = 2
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label3.Location = System.Drawing.Point(12, 89)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(69, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "WOUNDS"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label4.Location = System.Drawing.Point(87, 24)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(188, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "SoldierNameHere"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label5.Location = System.Drawing.Point(87, 57)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(188, 23)
		self._label5.TabIndex = 5
		self._label5.Text = "SoldierRankHere"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Silver
		self._button1.Location = System.Drawing.Point(12, 304)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 52)
		self._button1.TabIndex = 6
		self._button1.Text = "Transfer Soldier"
		self._button1.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Silver
		self._button2.Location = System.Drawing.Point(105, 304)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 52)
		self._button2.TabIndex = 7
		self._button2.Text = "TreatWound"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Silver
		self._button3.Location = System.Drawing.Point(200, 304)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 52)
		self._button3.TabIndex = 8
		self._button3.Text = "EVAC"
		self._button3.UseVisualStyleBackColor = False
		# 
		# PatientInfo
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(287, 368)
		self.ControlBox = False
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "PatientInfo"
		self.Text = "PatientInfo"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass