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
import os


folder_path = r"C:\venv\Page"

screen_width = 500
screen_height = 800

Window.size = (screen_width, screen_height)

slide_button_width = 50
slide_button_height = 50

a = ["month goals", "1years goals", "5years Goals", "final goals"]



class FirstWindow(Screen):
    pass


class Advice(Screen):
    # text_input = StringProperty(None)

    def on_pre_enter(self):
        self.ids.box_layout.clear_widgets()
        self.label = Label(text='Adive To ME', font_size= 50, size_hint = (1, 0.18))
        self.ids.box_layout.add_widget(self.label)
        self.text_input = TextInput(text='')
        self.ids.box_layout.add_widget(self.text_input)

        if not os.path.isfile("C:\\venv\\advice to me"):
            with open("C:\\venv\\advice to me", 'w') as f:
                f.write('')

        with open("C:\\venv\\advice to me", 'r') as f:
            self.text = f.read()
            self.text_input.text = self.text

    def on_text(self, instance, value):
        with open("C:\\venv\\advice to me", 'a') as f:
            f.write(value)
    
    def on_leave(self):
        with open("C:\\venv\\advice to me", 'w') as f:
            f.write(self.text_input.text)

    

class Todolist(Screen):
    def on_enter(self, *args):
        self.ids.grid_layout.clear_widgets()
        for i in range(1, 32):
            btn = Button(text=f'{i} day', height = self.height/5)
            btn.bind(on_release = self.go_to_metamong)
            self.ids.grid_layout.add_widget(btn)
        clear_btn = Button(text='Clear')
        clear_btn.bind(on_release = self.go_clear_btn)
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

    def go_clear_btn(self, instance):
        self.manager.current = 'clear_page'
        self.manager.transition.direction = 'left'

        


class Clear_page(Screen):
    def on_pre_enter(self):
        self.ids.box_layout_1.clear_widgets()
        btn = Button(text = 'real??', font_size = 70, pos_hint = {"center_x": 0.5,  "center_y": 0.5 }, size_hint = (0.5, 0.3))
        btn.bind(on_release = self.byebye)
        self.ids.box_layout_1.add_widget(btn)


    def byebye(self, instance):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename) # folder_path\filename 라는 경로를 만들어줌
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"오류 발생: {e}")


class Metamong(Screen):
    num = NumericProperty(0) 

        # 매개변수에서 num을 가져옴
    def __init__(self, **kwargs):
        super(Metamong, self).__init__(**kwargs)
        self.num = kwargs.get('num', 0)
        
    
    def on_pre_enter(self):
        
        # boxlayout 부분에 label과 btton 추가
        self.ids.box_layout.clear_widgets()
        self.label = Label(text=f'Days {self.num}', font_size = 44, size_hint = (2, 1))
        self.ids.box_layout.add_widget(self.label)
        btn = Button(text = 'feedback', font_size = 25)
        btn.bind(on_release = self.go_to_feedback)
        self.ids.box_layout.add_widget(btn)
        # gridlayout 부분에 textinput 추가
        self.ids.grid_layout.clear_widgets()
        self.tpt = TextInput(text = '', font_size = 20, pos = (0,0), size_hint = (1, 1))
        self.ids.grid_layout.add_widget(self.tpt)


        if not os.path.isdir("C:\\venv\\Page"):
            os.makedirs("Page")

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

    def go_to_feedback(self, instance):
        feed_name = f'{self.num} feedback'

        app = App.get_running_app()
        app.feedback_page = FeedBack(name = feed_name, num = self.num)
        app.root.add_widget(app.feedback_page)

        self.manager.current = feed_name
        self.manager.transition.direction = "left"


class Goals(Screen):
    def on_enter(self, **args):
        self.ids.goal_layout.clear_widgets()
        for i in range(len(a)):
            self.btn = Button(text = a[i], font_size = 44)
            self.btn.bind(on_release = self.go_to_goals)
            self.ids.goal_layout.add_widget(self.btn)

    def go_to_goals(self, instance):
        title = instance.text.split(" ")[0]
        title_name = f"{title} goals"

        if not self.manager.has_screen(title_name):
            goals_page = Goals_2(name = title_name, title = title)
            self.manager.add_widget(goals_page)

        app = App.get_running_app()
        app.title_name = title_name
        app.title = title

        self.manager.current = title_name
        self.manager.transition.direction = 'left'


class Goals_2(Screen):
    title = StringProperty("")

    def __init__(self, **kwargs):
        super(Goals_2, self).__init__(**kwargs)
        self.title = kwargs.get('title', '')

    def on_pre_enter(self):
        self.ids.box_layout.clear_widgets()
        label = Label(text = f'{self.title} goals', font_size = 44, size_hint=(1, 0.13))
        self.tpt = TextInput(text = '', font_size = 20 )
        self.ids.box_layout.add_widget(label)
        self.ids.box_layout.add_widget(self.tpt)

        if not os.path.isdir("C:\\venv\Goals"):
            os.makedirs("Goals")

        if not os.path.isfile(f"C:\\venv\Goals\\{self.title} goals"):
            with open(f"C:\\venv\Goals\\{self.title} goals", 'w') as f:
                f.write('')

        with open(f"C:\\venv\Goals\\{self.title} goals", 'r') as f:
            self.text = f.read()
            self.tpt.text = self.text

    def on_text(self, instance, value):
        with open(f"C:\\venv\Goals\\{self.title} goals", 'r', "a") as f:
            f.write(value)

    def on_leave(self):
        with open(f"C:\\venv\Goals\\{self.title} goals", "w") as f:
            f.write(self.tpt.text)


        
class FeedBack(Screen):
    # page_name = StringProperty(None)
    num = NumericProperty(0)

    def __init__(self, **kwargs):
        super(FeedBack, self).__init__(**kwargs)
        self.num = kwargs.get('num', 0)


    def on_pre_enter(self):
        self.ids.grid_layout.clear_widgets()
        label = Label(text=f'{self.num} days feedback', font_size = 44, size_hint = (1, 0.1))
        self.tpt = TextInput(text = '', font_size = 20, pos = (0,0), size_hint = (1, 1))
        self.ids.grid_layout.add_widget(label)
        self.ids.grid_layout.add_widget(self.tpt)

        # boxlayout 추가하기
        self.ids.box_layout.clear_widgets()
        btn = Button(text='<', font_size = 50)
        btn.bind(on_release = self.go_back)
        label = Label(text='', font_size = 44)
        self.ids.box_layout.add_widget(btn)
        self.ids.box_layout.add_widget(label)


        if not os.path.isfile(f"C:\\venv\\Page\\feedback {self.num} day"):
            with open(f"C:\\venv\\Page\\feedback {self.num} day", 'w') as f:
                f.write('')
        
        with open(f"C:\\venv\\Page\\feedback {self.num} day", 'r') as f:
            self.text = f.read()
            self.tpt.text = self.text

    def on_text(self, instance, value):
        with open(f"C:\\venv\\Page\\feedback {self.num} day", "a") as f:
            f.write(value)

    def on_leave(self):
        with open(f"C:\\venv\\Page\\feedback {self.num} day", "w") as f:
            f.write(self.tpt.text)

    def go_back(self, instance):
        self.manager.current = f"{self.num} days"
        self.manager.transition.direction = "right"



class WindowManager(ScreenManager):
    pass


kv = Builder.load_string("""

WindowManager:
    FirstWindow:
    Advice:
    Todolist:
    Goals:
    Clear_page:
    Goals_2:


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

            Label:
                text: ""
                font_size : 50

            
<Goals_2>:
    name: "goals_2"
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        size_hint: 0.95, 0.95
        spacing: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        BoxLayout: 
            id: box_layout
            orientation: "vertical"
            size_hint: 1, 1
            spacing: 20
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        BoxLayout:
            id: box_layout_2
            orientation: "horizontal"
            size_hint: 0.8, 0.05
            spacing: 20
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Button:
                text: "<"
                font_size : 50
                on_release:
                    app.root.current = "Goals"
                    root.manager.transition.direction = "right"

            
            Label:
                text: ""
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
            spacing: 20
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Button:
                text: "<"
                font_size : 50
                on_release:
                    app.root.current = "first"
                    root.manager.transition.direction = "right"

            
            Label:
                text: ""
                font_size : 50

<Clear_page>:
    name: 'clear_page'
    BoxLayout:
        orientation: "vertical"
        spacing: 100
        size_hint: 0.95, 0.95
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        FloatLayout:
            id: box_layout_1
            size_hint: 1, 1
            spacing: 20
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

            
            Label:
                text: ""
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

            
            Label:
                text: ""
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

            
            Label:
                text: ""
                font_size : 50

<FeedBack>:
    name: "feedback"

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        size_hint: 0.95, 0.95
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        spacing: 10

        GridLayout:
            cols: 1
            id: grid_layout
            size_hint: 1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        BoxLayout:
            id: box_layout 
            orientation: "horizontal"
            size: root.width, root.height * 1/9
            size_hint: 0.8, 0.05
            spacing: 100
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

            
            Label:
                text: ""
                font_size : 50

""")


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.page_name = None
        self.num = None
        self.title_name = None

    def build(self):
        return kv
        
    

    def on_stop(self):
        advice_screen = self.root.get_screen('advice')
        if advice_screen.text_input is not None and advice_screen.text_input.text:
            with open("C:\\venv\\advice to me", 'w') as f:
                f.write(advice_screen.text_input.text)

        page_name = self.page_name # page_name에 입력이 있을 때만 실행하도록
        if page_name:
            text_input = self.root.get_screen(page_name).tpt
            with open(f"C:\\venv\\page\\{self.num} day", "w") as f:
                f.write(text_input.text)

        feed_text = self.root.get_screen(self.feedback_page.name).tpt
        with open(f'C:\\venv\\Page\\feedback {self.num} day', 'w') as f:
            f.write(feed_text.text)

        goals_text = self.root.get_screen(self.title_name).tpt
        with open(f"C:\\venv\Goals\\{self.title} goals", "w") as f:
            f.write(goals_text.text)


if __name__ == "__main__":
    MyApp().run()