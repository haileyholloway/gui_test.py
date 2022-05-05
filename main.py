from guizero import App, Text, TextBox, PushButton, Slider, Picture

app=App(title="Hello World")
welcome_message = Text(app, text= "Welcome to my app", size=40, font="Times New Roman", color="lightblue")
my_name = TextBox(app)

def say_my_name():
  welcome_message.value = my_name.value
  
update_text = PushButton(app, command=say_my_name, text="Display my name")

def change_text_size(slider_value):
  welcome_message.size = slider_value

text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="cat.gif")


app.display()