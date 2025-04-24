import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import numpy as np

class CalculatorGrid(GridLayout):

    def __init__(self, **kwargs):
        super(CalculatorGrid, self).__init__(**kwargs)
        self.cols = 4
        self.display = TextInput(multiline=False, readonly=True, font_size=32, size_hint=(1, 0.2))
        self.add_widget(self.display)
        self.operators = ['+', '-', '*', '/', '.', '(', ')']
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]
        for button in buttons:
            self.add_widget(Button(text=button, on_press=self.on_button_press))
        self.add_widget(Button(text='Clear', on_press=self.clear))

    def on_button_press(self, instance):
        current = self.display.text
        pressed = instance.text

        if pressed == '=':
            try:
                result = str(eval(current))
                self.display.text = result
            except:
                self.display.text = 'Error'
        else:
            self.display.text += pressed

    def clear(self, instance):
        self.display.text = ''


class CalculatorApp(App):
    def build(self):
        return CalculatorGrid()


if __name__ == '__main__':
    CalculatorApp().run()
