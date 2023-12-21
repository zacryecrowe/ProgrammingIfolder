import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gray
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(221, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Cost per Kilowatt-Hour"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(239, 35)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(128, 26)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Gray
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 74)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(221, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Kilowatt-Hours Used"
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(239, 74)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(128, 26)
		self._textBox2.TabIndex = 5
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gray
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 142)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(221, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Base Rate"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Gray
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 183)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(221, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Surcharge"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Gray
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 221)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(221, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "City Tax"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Gray
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 261)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(221, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Amount Due"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Gray
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(12, 313)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(201, 23)
		self._label7.TabIndex = 10
		self._label7.Text = "Amount Due + Late Fee"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(267, 142)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 11
		self._label8.Text = "label8"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.White
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(267, 183)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 12
		self._label9.Text = "label9"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.White
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(267, 221)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 13
		self._label10.Text = "label10"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.White
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(267, 261)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 14
		self._label11.Text = "label11"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.White
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(267, 313)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 15
		self._label12.Text = "label12"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 385)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(99, 46)
		self._button1.TabIndex = 16
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(134, 385)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 46)
		self._button2.TabIndex = 17
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(258, 385)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 46)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(379, 443)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		CostPer = float(self._textBox1.Text)
		HourU = int(self._textBox2.Text) 
		BaseRate = round((CostPer*HourU),2)  
		SurChg = round((0.1*BaseRate),2) 
		CityTax = round((0.03*BaseRate),2) 
		Total = BaseRate + SurChg + CityTax 
		LateFee = round((0.04*Total),2) 
		LateFeeTotal = LateFee+Total 
		self._label8.Text = str(BaseRate)  
		self._label9.Text = str(SurChg) 
		self._label10.Text = str(CityTax) 
		self._label11.Text = str(Total) 
		self._label12.Text = str(LateFeeTotal) 		
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = "" 
		self._textBox2.Text = "" 
		self._label8.Text = "" 
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = "" 	
		self._label12.Text = "" 		
		
		pass

	def Button3Click(self, sender, e):
		Application.Exit() 
		pass