from kivymd.app import MDApp
from kivy.lang import Builder

kv='''
MDScreen:
	md_bg_color: "#238020"
	MDTopAppBar:
	MDButton:
		style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .5}
		MDButtonIcon:
			icon: "plus"
		MDButtonText:
			text: "Elevated"
'''
class MyApp(MDApp):
	def build(self):
		return Builder.load_string(kv)
		
MyApp().run()