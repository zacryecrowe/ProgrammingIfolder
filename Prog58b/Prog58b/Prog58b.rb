require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox
class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@label6 = System::Windows::Forms::Label.new()
		@label7 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.White
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(39, 229)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 36)
		@label1.TabIndex = 0
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.White
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(182, 229)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(100, 36)
		@label2.TabIndex = 1
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.White
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(39, 43)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(117, 35)
		@label3.TabIndex = 2
		@label3.Text = "Input A: "
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.White
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(39, 84)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(117, 35)
		@label4.TabIndex = 3
		@label4.Text = "Input B:"
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::Color.White
		@label5.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(39, 124)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(117, 35)
		@label5.TabIndex = 4
		@label5.Text = "Input C:"
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(162, 53)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(120, 20)
		@textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(162, 94)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(120, 20)
		@textBox2.TabIndex = 6
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(162, 134)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(120, 20)
		@textBox3.TabIndex = 7
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::Color.White
		@label6.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label6.Location = System::Drawing::Point.new(39, 198)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(100, 23)
		@label6.TabIndex = 8
		@label6.Text = "Pos Root: "
		# 
		# label7
		# 
		@label7.BackColor = System::Drawing::Color.White
		@label7.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label7.Location = System::Drawing::Point.new(182, 198)
		@label7.Name = "label7"
		@label7.Size = System::Drawing::Size.new(100, 23)
		@label7.TabIndex = 9
		@label7.Text = """Neg Root:
"""
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.ForestGreen
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(326, 40)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(105, 43)
		@button1.TabIndex = 10
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Yellow
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(326, 89)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(105, 42)
		@button2.TabIndex = 11
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Red
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(326, 140)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(105, 42)
		@button3.TabIndex = 12
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Black
		self.ClientSize = System::Drawing::Size.new(479, 322)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label7)
		self.Controls.Add(@label6)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		A = int(@textBox1.Text) 
		B = int(@textBox2.Text)
		C = int(@textBox3.Text) 
		Root1 =((-B + $math.sqrt(B**2 -4*A*C)))/2*A
		Root2 = (-B - ($math.sqrt(B**2 -4*A*C)))/2*A
		@label1.Text = "Root 1: " + str(Root1)
		@label2.Text = "Root 2: " + str(Root2) 
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@label1.text = ""
		@label2.text = ""
	end

	def Button3Click(sender, e)
		Application.Exit() 
	end
end

