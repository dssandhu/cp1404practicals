from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicWidget(App):
    def build(self):
        self.title = "My Dynamic Widget"
        self.root = Builder.load_file('my_dynamic_widget.kv')


DynamicWidget().run()
