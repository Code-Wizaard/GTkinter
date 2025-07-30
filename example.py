from GTkinter import App, Window, Button, Label, VBox
from GTkinter.enums import Events

app = App()
win = Window("Hello GTkinter", 300, 200)

layout = VBox()
label = Label("Click the button")
btn = Button("Click me")

def on_click(button):
    label.set_text("You clicked me!")

btn.connect(Event.CLICKED, on_click)

layout.add(label)
layout.add(btn)
win.set_child(layout)

win.connect(Event.DESTROY, lambda w: exit(0))

app.run(win)
