from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
MDScreen:
    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: 'Select'
        on_release: app.menu.open()

'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        d_items = ['Snapshot','Settings','History','Logout','Exit']
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                #"height": dp(56),#size of the items
                "on_release": lambda x=i: self.set_item(x),
            } for i in d_items
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=2,
            max_height=dp(200)#tells the height of the drop down menu
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.screen.ids.drop_item.text=text_item
        self.menu.dismiss()


    def build(self):
        return self.screen

Test().run()