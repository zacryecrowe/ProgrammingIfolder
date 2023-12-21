﻿require "mscorlib"
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
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.ForestGreen
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(60, 186)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(106, 39)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Yellow
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::SystemColors.ControlText
		@button2.Location = System::Drawing::Point.new(169, 186)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(106, 39)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Red
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 12, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(283, 186)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(106, 39)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.White
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(37, 100)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(112, 29)
		@label1.TabIndex = 3
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.White
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(173, 100)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(112, 29)
		@label2.TabIndex = 4
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label2.Click { |sender, e| self.Label2Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.White
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(308, 100)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(112, 29)
		@label3.TabIndex = 5
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label3.Click { |sender, e| self.Label3Click(sender, e) }
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::Color.White
		@label4.Location = System::Drawing::Point.new(47, 47)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(106, 26)
		@label4.TabIndex = 6
		@label4.Text = "Input Radius:"
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(156, 47)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(216, 24)
		@textBox1.TabIndex = 7
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(452, 250)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Font = System::Drawing::Font.new("Microsoft Sans Serif", 11.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Lang54c (V3)"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Label1Click(sender, e)
		
	end

	def MainFormLoad(sender, e)
		
	end

	def Button1Click(sender, e)
		rad = float(@textBox1.Text) 
		pi = 3.14159
		area = pi*rad**2
		circum = 2*pi*rad
		@label1.Text = "Radius: " + str(round(rad, 3)) 
		@label2.Text = "Area: " + str(round(area, 3)) 
		@label3.Text = "Circum: " + str(round(circum, 3)) 
		
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@textBox1.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit() 
		
	end

end

