from kivymd.app import MDApp
from kivy.uix.button import Button

class HelloWorldApp(MDApp):
    def build(self):
        return Button(text='Hello World!')

if __name__ == '__main__':
    HelloWorldApp().run()
