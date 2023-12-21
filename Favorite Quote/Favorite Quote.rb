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
		@label1.BackColor = System::Drawing::SystemColors.HighlightText
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Bold | System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.Black
		@label1.Location = System::Drawing::Point.new(160, 30)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(417, 154)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.LimeGreen
		@button1.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button1.Location = System::Drawing::Point.new(197, 212)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(118, 56)
		@button1.TabIndex = 1
		@button1.Text = "Show Quote"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Brown
		@button2.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@button2.Location = System::Drawing::Point.new(398, 212)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(118, 56)
		@button2.TabIndex = 2
		@button2.Text = "Clear Quote"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(762, 351)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Favorite Quote"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Innocent people sleep easy at night knowing that good men stand ready to do violence on their behalf"
	end

	def Button2Click(sender, e)
		@label1.Text = "" 
	end

	def Label1Click(sender, e)
		
	end
end

