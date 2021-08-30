# IMPORTS  -----------
from guizero import App, Text, Picture, PushButton
# from random import choice


# FUNCTIONS -----------
def choose_name():     # a function to choose a random name
    print("Button was pressed")


# App  -----------
# This is the title of UI Window
app = App(title="Hello World")
# or we can use App("Hello world")


# WIDGETS  -----------
# The message
message = Text(app, text="Welcome my first gui window")

# This adds a background color to the UI Window
app.bg = '#BBF643'

# This Puts the local image.png on the screen
pic = Picture(app, image="download.png")

# Another text want
want = Text(app, text="hey you , got outta here !!")

# This defines the text size, Color, Font type for want (text)
want.text_size = 34
want.text_color = '#0DB1F6'
want.font = 'Times New Roman'

# This function is used to add a clickable button
button = PushButton(app, choose_name, text="Tell me!")


# DISPLAY  -----------
# This displays all the above defined properties and texts
app.display()
