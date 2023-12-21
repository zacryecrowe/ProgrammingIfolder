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
		@label1.Font = System::Drawing::Font.new("Script MT Bold", 24, System::Drawing::FontStyle.Bold | System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(139, 58)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(330, 60)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.SpringGreen
		@button1.ForeColor = System::Drawing::Color.Black
		@button1.Location = System::Drawing::Point.new(139, 159)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(129, 53)
		@button1.TabIndex = 1
		@button1.Text = "Show Fabulous name"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Red
		@button2.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button2.Location = System::Drawing::Point.new(341, 159)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(128, 53)
		@button2.TabIndex = 2
		@button2.Text = "Clear Fabulous name"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Black
		self.ClientSize = System::Drawing::Size.new(588, 296)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "My Name"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Zacrye Miles Crowe" 
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

