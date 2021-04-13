from kivy.app import App
from kivy.uix.button import  Button
class LangLearnApp(App):
    def build(self ):
        return Button(text = "hello dumbass")

if __name__== "__main__":
    LangLearnApp().run()