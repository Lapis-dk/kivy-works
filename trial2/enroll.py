from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu

Window.size = (350, 700)
class Demo1(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Screen = Builder.load_file("demo.kv")
        d_items = ['Snapshot','Settings','History','Logout','Exit']
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_release": lambda x=i: self.set_item(x),
            } for i in d_items
        ]
        self.menu = MDDropdownMenu(
            caller=self.Screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=2,
            max_height=200
        )

        self.menu_opened = False  # Variable to track menu state

    def set_item(self, text_item):
        self.Screen.ids.drop_item.text=text_item
        self.menu.dismiss()
        self.menu_opened = False
    def on_text(self,instance):
        print(instance_id)
        if not self.menu_opened:
            self.menu.open()
            self.menu_opened = True

    def build(self):
        return self.Screen

    def on_start(self):
        self.fps_monitor_start()

Demo1().run()