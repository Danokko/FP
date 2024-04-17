import tkinter as tk


def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command)
    button.pack()#//размещение
    return button

def create_label(parent, text):
    label = tk.Label(parent, text=text)
    label.pack()
    return label

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Мое приложение")
        self.geometry("400x300")

        # Создание компонентов
        self.label = create_label(self, "Пример модульного подхода к UI")
        self.button = create_button(self, "Нажми меня", self.on_button_click)

    def on_button_click(self):
        self.label.config(text="Кнопка была нажата!")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

