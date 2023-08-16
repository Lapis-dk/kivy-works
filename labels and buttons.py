import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class gridd(GridLayout):
    def __init__(self,**kwargs):
        super(gridd,self).__init__(**kwargs)
        self.cols=1
        self.topgrid=GridLayout()
        self.topgrid.cols=2

        self.topgrid.add_widget(Label(text="Name: "))
        self.name = TextInput()
        self.topgrid.add_widget(self.name)
        self.topgrid.add_widget(Label(text="No: "))
        self.no = TextInput()
        self.topgrid.add_widget(self.no)

        #to add the nested grid into the original 1 colnm grid
        self.add_widget(self.topgrid)

        self.submit=Button(text="submit", font_size=32)
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.press)

    def press(self,instance):
        name=self.name.text
        no=self.no.text
        self.add_widget(Label(text=f"hello my name is {name} and no is {no}"))

        #to clear the input boxes
        self.name.text=""

class hi(App):
    def build(self):
        return gridd()

#if __name__=='__main__':
hi().run()