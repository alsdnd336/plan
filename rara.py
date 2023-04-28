from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
import os
text = StringProperty('')
import os


class myscreen(Screen):
    
    def __init__(self,**kwargs):
        super(myscreen, self).__init__(**kwargs)
        self.text_input = TextInput(text = '')
        self.add_widget(self.text_input)

    def on_pre_enter(self):
        with  open('C:\\coding\\text.txt', 'r') as f:
            self.text = f.read()
            self.text_input.text = self.text # Textinput에 파일에서 읽은 대용을 할당한다.

    def on_text(self, instance, value):
        with  open("C:\\coding\\text.txt", 'a') as f:
            f.write(value)

        self.text_input.text = value



class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(myscreen(name= 'my'))
        return sm
    
    def on_stop(self):
        with open("C:\\coding\\text.txt", 'w') as f:
            f.write(self.root.get_screen('my').text_input.text)

if __name__ == '__main__':
    MyApp().run()

# current_path = os.getcwd()
# file_path = os.path.join(current_path, 'text.txt')

# print("text.txt의 경로:", file_path)