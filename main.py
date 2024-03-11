from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from PIL import Image as PILImage
from kivy.graphics.texture import Texture
import pickle

Window.size = (400, 500)

class TodoApp(App):
    def build(self):
        self.tasks = []

        # Entry for adding tasks
        self.task_entry = TextInput(font_size=18, multiline=False)

        # Button to add tasks
        add_button = Button(text="Add Task", on_press=self.add_task)

        # Listview to display tasks
        self.task_listview = ScrollView()
        self.task_listbox = BoxLayout(orientation="vertical", spacing=5, size_hint_y=None)
        self.task_listview.add_widget(self.task_listbox)

        # Button to remove selected task
        remove_button = Button(text="Remove Task", on_press=self.remove_task)

        # Load icons
        self.add_icon = self.resize_icon("add_icon.png", 20, 20)
        self.remove_icon = self.resize_icon("remove_icon.png", 20, 20)

        # Set up UI
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.task_entry)
        layout.add_widget(add_button)
        layout.add_widget(self.task_listview)
        layout.add_widget(remove_button)

        return layout

    def resize_icon(self, filename, width, height):
        original_image = PILImage.open(filename)
        resized_image = original_image.resize((width, height))
        texture = Texture.create(size=(resized_image.width, resized_image.height), colorfmt='rgba')
        texture.blit_buffer(resized_image.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
        return Image(texture=texture)

    def add_task(self, instance):
        task_text = self.task_entry.text
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.add_widget(Label(text=task_text, font_size=18))
            self.task_entry.text = ""
            self.save_data()

    def remove_task(self, instance):
        if self.tasks:
            removed_task = self.tasks.pop()
            self.task_listbox.remove_widget(self.task_listbox.children[-1])
            self.show_popup(f"Removed Task: {removed_task}")
            self.save_data()

    def save_data(self):
        with open("todo_data.pkl", "wb") as file:
            pickle.dump(self.tasks, file)

    def show_popup(self, message):
        popup = ModalView(size_hint=(0.7, 0.3))
        popup.add_widget(Label(text=message, font_size=18))
        popup.open()

if __name__ == "__main__":
    TodoApp().run()
