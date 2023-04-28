from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
import os


current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, 'textinput_fle')

class myscreen(Screen):
    
    def __init__(self,**kwargs):
        super(myscreen, self).__init__(**kwargs)
        self.text_input = TextInput(text = '')
        self.add_widget(self.text_input)

    def on_pre_enter(self):
        with  open(file_path, 'r') as f:
            self.text = f.read()
            self.text_input.text = self.text # Textinput에 파일에서 읽은 대용을 할당한다.

    def on_text(self, instance, value):
        with  open(file_path, 'w') as f:
            self.text_input.text = f.write(value)

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(myscreen(name= 'my'))
        return sm

if __name__ == '__main__':
    MyApp().run()

