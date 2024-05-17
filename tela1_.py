from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

class TelaInicial(Screen):
    pass

class App(App):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaInicial(name='tela1'))
        return sm


if __name__ == '__main__':
    App().run()