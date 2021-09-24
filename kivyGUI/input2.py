from re import MULTILINE
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructure
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))
        # Add Input
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # Add widgets
        self.add_widget(Label(text="Favorite Pizze: "))
        # Add Input
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # Add widgets
        self.add_widget(Label(text="Favorite color: "))
        # Add Input
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        # Create a submit button
        self.submit = Button(text="Submit", font_size=40)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'Hello {name}, you like {pizza} pizza and your favoriate color is {color}!')
        # Print it to the screen
        speech = f'Hello {name}, you like {pizza} pizza and your favoriate color is {color}!'
        self.add_widget(Label(text=speech))

        # Clear the input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()