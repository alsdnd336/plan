from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
Window.size = (500, 800)


a = ["month goals", "1years goals", "5 years Goals", "the final goals"]

class FirstWindow(Screen):
    pass


class Advice(Screen):
    pass

class Todolist(Screen):
    def on_enter(self, *args):
        for i in range(1, 32):
            self.ids.grid_layout.add_widget(Button(text=f'{i} day', height= self.height/5))
        clear_btn = Button(text='Clear', size_hint=(2, 1))
        self.ids.grid_layout.add_widget(clear_btn)

class Goals(Screen):
    def on_enter(self, **args):
        for i in range(4):
            self.ids.goal_layout.add_widget(Button(text = a[i], font_size = 44))
    


class WindowManager(ScreenManager):
    pass


kv = Builder.load_string("""

WindowManager:
    FirstWindow:
    Advice:
    Todolist:
    Goals:

<FirstWindow>:
    name: "first"
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        size_hint: 0.9, 0.9
        spacing: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.5}



        Button:
            text: "To-Do-List"
            font_size: 44
            font: 
            on_release: 
                app.root.current = "list"
                root.manager.transition.direction = "left"

        Button:
            text: "Goals"
            font_size: 44
            on_release: 
                app.root.current = "Goals"
                root.manager.transition.direction = "left"

        Button:
            text: "advice to me"
            font_size: 44
            on_release: 
                app.root.current = "advice"
                root.manager.transition.direction = "left"
        

<Todolist>:
    name:"list"
    GridLayout:
        size_hint: 0.96, 0.96
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        id: grid_layout
        cols: 7
        rows: 5
        spacing: 5

            
<Goals>:
    name: 'Goals'
    GridLayout:
        size_hint: 0.96, 0.96
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        id: goal_layout
        cols: 1
        spacing: 12
        
<Advice>:
    name: "advice"
    BoxLayout: 
        orientation: "vertical"
        size: root.width, root.height
    
        Label:
            text: "Adive To ME"
            font_size: 50

        TextInput:
            text: " "
            font_size: 17
            size_hint: (1, 5)
""")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()