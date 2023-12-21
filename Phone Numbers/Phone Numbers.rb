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
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 20.25, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(33, 23)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(559, 210)
		@label1.TabIndex = 0
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.ForestGreen
		@button1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@button1.Location = System::Drawing::Point.new(86, 254)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(212, 23)
		@button1.TabIndex = 2
		@button1.Text = "Show Numbers"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DarkRed
		@button2.ForeColor = System::Drawing::SystemColors.Control
		@button2.Location = System::Drawing::Point.new(321, 254)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(212, 23)
		@button2.TabIndex = 3
		@button2.Text = "Clear Numbers"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(678, 400)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Phone Numbers"
		self.ResumeLayout(false)
	end

	def CheckBox1CheckedChanged(sender, e)
		
	end

	def Button2Click(sender, e)
		@label1.Text = "" 
	end

	def Button1Click(sender, e)
		@label1.Text = "Mox Games - (608) 563-1337\nTexas Roadhouse - (608) 757-9700\nEarthsong - (608) 754-3933\nKryptonite Collectables - (608) 758-2100\nBam Books - (608) 752-6071"
	end
end

