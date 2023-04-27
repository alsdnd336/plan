from kivy.app import App
from kivy.uix.textinput import TextInput

class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        self.bind(on_text=self.on_text)

    def on_text(self, instance, value):
        f =  open('my_text_file.txt', 'w')
        f.write(value)
        f.close()

class MyApp(App):
    def build(self):
        return MyTextInput()

if __name__ == '__main__':
    MyApp().run()