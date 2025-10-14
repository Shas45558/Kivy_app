from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Kv='''
TTT:
<TTT>:
	MDFloatLayout:
		md_bg_color: "yellow"
		MDGridLayout:
			spacing : "5dp"
			md_bg_color:"pink"
			size_hint: .5 , .3
			pos_hint: {"center_x": .5 ,"center_y": .7}
			cols:3
			rows:3
			Button:
				id:btn1
				on_release:root.presser(self)
			Button:
				id:btn2
				on_release:root.presser(self)
			Button:
				id:btn3
				on_release:root.presser(self)
			Button:
				id:btn4
				on_release:root.presser(self)
			Button:
				id:btn5
				on_release:root.presser(self)
			Button:
				id:btn6
				on_release:root.presser(self)
			Button:
				id:btn7
				on_release:root.presser(self)
			Button:
				id:btn8
				on_release:root.presser(self)
			Button:
				id:btn9
				on_release:root.presser(self)
	MDLabel:
		id: turn_label
		md_bg_color:"yellow"
		pos_hint: {"center_x": .5 ,"center_y": .5}
		size_hint: .4 ,.05
		text:"Now X's turn"
		halign:"center"
		theme_text_color:"Custom"
		text_color:"#2596be"
	Button:
	    size_hint:.5,.09
	    text:"Reset"
        style: "filled"
        height: "70dp"
        theme_bg_color: "Custom"
        md_bg_color: "red"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_press:root.reset()
	MDLabel:
		id: x_win
		md_bg_color:"yellow"
		pos_hint: {"center_x": .2 ,"center_y": .3}
		size_hint: .2 ,.05
		text:"X Wins: 0"
		halign:"center"
		theme_text_color:"Custom"
		text_color:"#2596be"
	MDLabel:
		id: o_win
		md_bg_color:"yellow"
		pos_hint: {"center_x": .8 ,"center_y": .3}
		size_hint: .2 ,.05
		text:"O Wins: 0"
		halign:"center"
		theme_text_color:"Custom"
		text_color:"#2596be"
'''
class TTT(MDFloatLayout):
	turn=0
	x=0
	y=0
	def reset(self):
		self.ids.btn1.disabled=False
		self.ids.btn2.disabled=False
		self.ids.btn3.disabled=False
		self.ids.btn4.disabled=False
		self.ids.btn5.disabled=False
		self.ids.btn6.disabled=False
		self.ids.btn7.disabled=False
		self.ids.btn8.disabled=False
		self.ids.btn9.disabled=False
		self.ids.btn1.text=""
		self.ids.btn2.text=""
		self.ids.btn3.text=""
		self.ids.btn4.text=""
		self.ids.btn5.text=""
		self.ids.btn6.text=""
		self.ids.btn7.text=""
		self.ids.btn8.text=""
		self.ids.btn9.text=""
		self.ids.turn_label.text="Now X's turn"
		self.turn=0
	def disabler(self):
		self.ids.btn1.disabled=True
		self.ids.btn2.disabled=True
		self.ids.btn3.disabled=True
		self.ids.btn4.disabled=True
		self.ids.btn5.disabled=True
		self.ids.btn6.disabled=True
		self.ids.btn7.disabled=True
		self.ids.btn8.disabled=True
		self.ids.btn9.disabled=True
	def checker(self):
		if self.ids.btn1.text=="X" and self.ids.btn2.text=="X" and self.ids.btn3.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
			self.x=self.x+1
			self.ids.x_win.text="X Wins: "+str(self.x)
		if self.ids.btn4.text=="X" and self.ids.btn5.text=="X" and self.ids.btn6.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
			self.x=self.x+1
			self.ids.x_win.text="X Wins: "+str(self.x)
		if self.ids.btn7.text=="X" and self.ids.btn8.text=="X" and self.ids.btn9.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
			self.x=self.x+1
			self.ids.x_win.text="X Wins: "+str(self.x)
		if self.ids.btn1.text=="X" and self.ids.btn4.text=="X" and self.ids.btn7.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
		if self.ids.btn2.text=="X" and self.ids.btn5.text=="X" and self.ids.btn8.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
			self.x=self.x+1
			self.ids.x_win.text="X Wins: "+str(self.x)
		if self.ids.btn3.text=="X" and self.ids.btn6.text=="X" and self.ids.btn9.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
			self.x=self.x+1
			self.ids.x_win.text="X Wins: "+str(self.x)
		if self.ids.btn1.text=="X" and self.ids.btn5.text=="X" and self.ids.btn9.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
			self.x=self.x+1
			self.ids.x_win.text="X Wins: "+str(self.x)
		if self.ids.btn3.text=="X" and self.ids.btn5.text=="X" and self.ids.btn7.text== "X":
			self.disabler()
			self.ids.turn_label.text="X is win the Match"
			self.x=self.x+1
			self.ids.x_win.text="X Wins: "+str(self.x)
		if self.ids.btn1.text=="O" and self.ids.btn2.text=="O" and self.ids.btn3.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		if self.ids.btn4.text=="O" and self.ids.btn5.text=="O" and self.ids.btn6.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		if self.ids.btn7.text=="O" and self.ids.btn8.text=="O" and self.ids.btn9.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		if self.ids.btn1.text=="O" and self.ids.btn4.text=="O" and self.ids.btn7.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		if self.ids.btn2.text=="O" and self.ids.btn5.text=="O" and self.ids.btn8.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		if self.ids.btn3.text=="O" and self.ids.btn6.text=="O" and self.ids.btn9.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		if self.ids.btn1.text=="O" and self.ids.btn5.text=="O" and self.ids.btn9.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		if self.ids.btn3.text=="O" and self.ids.btn5.text=="O" and self.ids.btn7.text== "O":
			self.disabler()
			self.ids.turn_label.text="O is win the Match"
			self.y=self.y+1
			self.ids.o_win.text="O Wins: "+str(self.y)
		else:
			pass
	def presser(self,btn):
		btn.font_size="50dp"
		if self.turn==0:
			btn.text="X"
			self.turn=1
			self.ids.turn_label.text="Now 0's turn"
			btn.disabled= True
			self.draw()
			self.checker()
		else:
			btn.text="O"
			self.turn=0
			self.ids.turn_label.text="Now X's turn"
			btn.disabled= True
			self.draw()
			self.checker()
	def draw(self):
		if self.ids.btn1.disabled==self.ids.btn2.disabled==self.ids.btn3.disabled==self.ids.btn4.disabled==self.ids.btn5.disabled==self.ids.btn6.disabled==self.ids.btn7.disabled==self.ids.btn8.disabled==self.ids.btn9.disabled==True and self.ids.btn1.text!="" and self.ids.btn2.text!="" and self.ids.btn3.text!="" and self.ids.btn4.text!="" and self.ids.btn5.text!="" and self.ids.btn6.text!="" and self.ids.btn7.text!="" and self.ids.btn8.text!="" and self.ids.btn9.text!="":
			self.ids.turn_label.text="Draw"
		else:
			pass
class TttApp(MDApp):

	def build(self):
		return Builder.load_string(Kv)
		

if __name__ == '__main__':
    TttApp().run()
