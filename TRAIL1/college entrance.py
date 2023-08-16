from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

Window.size = (300, 700)
Window.clearcolor = (1, 1, 1, 1)

class MyApp(App):
    def build(self):
        return Builder.load_file("aa.kv")

if __name__ == '__main__':
    MyApp().run()
