from kivymd.app import MDApp
from kivymd.uix.button import MDButton

class HelloWorldApp(MDApp):
    def build(self):
        return MDButton()

if __name__ == '__main__':
    HelloWorldApp().run()
