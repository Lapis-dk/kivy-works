from kivymd.app import MDApp
from kivymd.uix.swiper import MDSwiperItem
from kivy.properties import StringProperty
from kivy.lang import Builder


class MySwiper(MDSwiperItem):
    image = StringProperty()


class MainApp(MDApp):
    def build(self):
        self.title="KivyMD Travel App"
        self.theme_cls.primary_palette='BlueGray'
        return  Builder.load_file("tr.kv")

MainApp().run()