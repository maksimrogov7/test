from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    
    def build(self):

        
        boxlayout = BoxLayout(orientation='vertical')
        

        
        
        
        btn1 = TextInput(multiline=False)
        btn2 = TextInput(multiline=False)
        btn4 = Label()
        btn3 = Button(text='Сложить', on_press=lambda instanse: setattr(btn4, "text", str(float(btn1.text) + float(btn2.text))))
        


        
        
        boxlayout.add_widget(btn1) 
        boxlayout.add_widget(btn2)
        boxlayout.add_widget(btn3)
        boxlayout.add_widget(btn4)

        return boxlayout


app = MyApp()
app.run()
