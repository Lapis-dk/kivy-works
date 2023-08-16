from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivymd.uix.pickers import MDDatePicker

Window.size = (350, 700)




class Demo1(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flag = False
        d_items = ['cse','ece','eee','mech','civil']
        self.Screen = Builder.load_file("work.kv")
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
        if not self.menu_opened:
            self.menu.open()
            self.menu_opened = True


    def on_save(self, instance, value, date_range):
        self.Screen.ids.calendar.text=str(value)
        self.flag=False

    def on_cancel(self, instance, value):
        self.flag = False

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        if not self.flag:
            self.flag=True
            date_dialog.open()
    def build(self):
        return self.Screen

Demo1().run()