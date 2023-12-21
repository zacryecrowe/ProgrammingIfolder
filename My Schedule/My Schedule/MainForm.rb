require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.White
		@label1.ForeColor = System::Drawing::SystemColors.ControlText
		@label1.Location = System::Drawing::Point.new(51, 26)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(156, 108)
		@label1.TabIndex = 0
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.ForestGreen
		@button1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button1.Location = System::Drawing::Point.new(235, 25)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(99, 45)
		@button1.TabIndex = 1
		@button1.Text = "Show Schedule"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Crimson
		@button2.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button2.Location = System::Drawing::Point.new(235, 76)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(99, 44)
		@button2.TabIndex = 2
		@button2.Text = "Clear Schedule "
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(548, 331)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "My Schedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Period 1 - Studyhall\nPeriod 2 -Photography\nPeriod 3 - Sci-fi & Fantasy\nPeriod 4 - TC Speech\nPeriod 5 - Intergrated Algebra\nPeriod 6 - Programming 1\nPeriod 7 - AP Physics 2\nPeriod 8 - TC Psychology"
	end

	def Button2Click(sender, e)
		@label1.Text 
	end
end

