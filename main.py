from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Hello Prince Sir!\nJarvis AI is Ready.", font_size='24sp', halign='center')
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    JarvisApp().run()
