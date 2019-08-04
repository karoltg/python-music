# Load the required library

from kivy.app import App
from kivy.uix.button import Button
from pygame import mixer


class TestApp(App):
    def build(self):
        return Button(text='Hello World')

# muzyka działa trzeba zmienić ścieżkę
mixer.init()
mixer.music.load('c:/10. Feeling Good.mp3')
mixer.music.play()
TestApp().run()




