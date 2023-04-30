from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
import os.path


screen_width = 500
screen_height = 800

Window.size = (screen_width, screen_height)

slide_button_width = 50
slide_button_height = 50

a = ["month goals", "1years goals", "5 years Goals", "the final goals"]

class FirstWindow(Screen):
    pass


class Advice(Screen):

    def on_pre_enter(self):
        self.ids.box_layout.clear_widgets()
        self.label = Label(text='Adive To ME', font_size= 50, size_hint = (1, 0.18))
        self.ids.box_layout.add_widget(self.label)
        self.text_input = TextInput(text='')
        self.ids.box_layout.add_widget(self.text_input)

        if not os.path.isfile("C:\\venv\\Page\\advice to me"):
            with open("C:\\venv\\Page\\advice to me", 'w') as f:
                f.write('')

        with open("C:\\venv\\Page\\advice to me", 'r') as f:
            self.text = f.read()
            self.text_input.text = self.text

    def on_text(self, instance, value):
        with open("C:\\venv\\Page\\advice to me", 'a') as f:
            f.write(value)
    
    def on_leave(self):
        with open("C:\\venv\\Page\\advice to me", 'w') as f:
            f.write(self.text_input.text)

    

class Todolist(Screen):
    def on_enter(self, *args):
        self.ids.grid_layout.clear_widgets()
        for i in range(1, 32):
            btn = Button(text=f'{i} day', height = self.height/5)
            btn.bind(on_release = self.go_to_metamong)
            self.ids.grid_layout.add_widget(btn)
        clear_btn = Button(text='Clear')
        self.ids.grid_layout.add_widget(clear_btn)
        
    def go_to_metamong(self, instance):
        num = int(instance.text.split(" ")[0])
        page_name = f'{num} days'

        if not self.manager.has_screen(page_name):
            day_page = Metamong(name = page_name, num = num)
            self.manager.add_widget(day_page)

        app = App.get_running_app()
        app.page_name = page_name
        app.num = num

        self.manager.current = page_name
        self.manager.transition.direction = 'left'



class Metamong(Screen):
    num = NumericProperty(0) 

        # 매개변수에서 num을 가져옴
    def __init__(self, **kwargs):
        super(Metamong, self).__init__(**kwargs)
        self.num = kwargs.get('num', 0)
        
    
    def on_pre_enter(self):
        
        # boxlayout 부분에 label과 btton 추가
        self.label = Label(text=f'Days {self.num}', font_size = 44, size_hint = (2, 1))
        self.ids.box_layout.add_widget(self.label)
        btn = Button(text = 'feedback', font_size = 25)
        btn.bind(on_release = self.go_feedback)
        self.ids.box_layout.add_widget(btn)
        # gridlayout 부분에 textinput 추가
        self.ids.grid_layout.clear_widgets()
        self.tpt = TextInput(text = '', font_size = 20, pos = (0,0), size_hint = (1, 1))
        self.ids.grid_layout.add_widget(self.tpt)
        if not os.path.isfile(f"C:\\venv\\Page\\{self.num} day"):
            with open(f"C:\\venv\\Page\\{self.num} day", 'w') as f:
                f.write('')

        with open(f"C:\\venv\\Page\\{self.num} day", 'r') as f:
            self.text = f.read()
            self.tpt.text = self.text
        
    def on_text(self, instance, value):
        with open(f"C:\\venv\\Page\\{self.num} day", "a") as f:
            f.write(value)

    def on_leave(self):
        with open(f"C:\\venv\\Page\\{self.num} day", "w") as f:
            f.write(self.tpt.text)




class Goals(Screen):
    def on_enter(self, **args):
        self.ids.goal_layout.clear_widgets()
        for i in range(4):
            self.ids.goal_layout.add_widget(Button(text = a[i], font_size = 44))
        
class FeedBack(Screen):
    pass

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
        size_hint: 0.95, 0.95
        spacing: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        BoxLayout:
            orientation: "vertical"
            size: root.width, root.height * 8/9
            size_hint: 0.95, 0.95
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

        BoxLayout: 
            orientation: "horizontal"
            size: root.width, root.height * 1/9
            size_hint: 0.8, 0.05
            spacing: 100
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Button:
                text: "<"
                font_size : 50
                on_release:
                    app.root.current = "first"
                    root.manager.transition.direction = "right"

            
            Button:
                text: ">"
                font_size : 50
        

<Todolist>:
    name:"list"
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        size_hint: 0.95, 0.95
        spacing: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        GridLayout:
            size_hint: 0.96, 0.96
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            id: grid_layout
            cols: 7
            rows: 5
            spacing: 5
        
        BoxLayout: 
            orientation: "horizontal"
            size: root.width, root.height * 1/9
            size_hint: 0.8, 0.05
            spacing: 100
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Button:
                text: "<"
                font_size : 50
                on_release:
                    app.root.current = "first"
                    root.manager.transition.direction = "right"

            
            Button:
                text: ">"
                font_size : 50
        

            
<Goals>:
    name: 'Goals'
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        size_hint: 0.95, 0.95
        spacing: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        GridLayout:
            size_hint: 0.96, 0.96
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            id: goal_layout
            cols: 1
            spacing: 12

        BoxLayout: 
            orientation: "horizontal"
            size: root.width, root.height * 1/9
            size_hint: 0.8, 0.05
            spacing: 100
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Button:
                text: "<"
                font_size : 50
                on_release:
                    app.root.current = "first"
                    root.manager.transition.direction = "right"

            
            Button:
                text: ">"
                font_size : 50

<Metamong>:
    name: "metamong"
    BoxLayout:    
        orientation: "vertical"
        size_hint: 0.95, 0.95
        spacing: 10
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        BoxLayout:
            id: box_layout
            orientation: "horizontal"
            size_hint: 1, 0.1
            pos_hint: {"center_x": 0.5, "center_y": 0.5}



        GridLayout:
            id: grid_layout
            cols: 1
            size: root.width, root.height
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        BoxLayout: 
            orientation: "horizontal"
            size: root.width, root.height * 1/9
            size_hint: 0.8, 0.05
            spacing: 100
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Button:
                text: "<"
                font_size : 50
                on_release:
                    app.root.current = "list"
                    root.manager.transition.direction = "right"

            
            Button:
                text: ">"
                font_size : 50

<FeedBack>:
    name: "feedback"

    boxlayout:
        orientation: "vertical"
        size: root.width, root.height
        size_hint: 0.95, 0.95
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

          
<Advice>:
    name: "advice"

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        size_hint: 0.95, 0.95
        spacing: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        BoxLayout:
            id: box_layout 
            orientation: "vertical"
            size: root.width, root.height


        BoxLayout: 
            orientation: "horizontal"
            size: root.width, root.height * 1/9
            size_hint: 0.8, 0.05
            spacing: 100
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Button:
                text: "<"
                font_size : 50
                on_release:
                    app.root.current = "first"
                    root.manager.transition.direction = "right"

            
            Button:
                text: ">"
                font_size : 50
        

""")


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.page_name = None
        self.num = None

    def build(self):
        return kv
        
    

    def on_stop(self):
        advice_screen = self.root.get_screen('advice')
        if advice_screen.text_input is not None and advice_screen.text_input.text:
            with open("C:\\venv\\Page\\advice to me", 'w') as f:
                f.write(advice_screen.text_input.text)

        page_name = self.page_name # page_name에 입력이 있을 때만 실행하도록
        if page_name:
            text_input = self.root.get_screen(page_name).tpt
            with open(f"C:\\venv\\page\\{self.num} day", "w") as f:
                f.write(text_input.text)



if __name__ == "__main__":
    MyApp().run()