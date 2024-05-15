from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
class Estudo1App(App):
    def build(self):
            Window.clearcolor=(0.82, 0.41, 0.12, 1)
    pass
janela = Estudo1App()
janela.run()