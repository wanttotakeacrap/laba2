import tkinter as tk
import random
import sys
import os


class Gallows(tk.Tk):  # игровой класс


    def __init__(self):  # конструктор

        super().__init__()
        self.title("Guess the word")
        self.geometry("1000x500")

        self.sentence = {
            "солнце": "Звезда, вокруг которой вращается Земля и другие планеты; источник света и тепла.",
            "дерево": "Высокое растение с деревянным стволом и ветвями.",
            "книга": "Печатное или письменное произведение, состоящее из страниц.",
            "вода": "Жидкость, необходимая для жизни; без цвета и вкуса.",
            "дом": "Здание, в котором живут люди.",
            "яблоко": "Сладкий плод, обычно красного, зеленого или желтого цвета, с хрустящей мякотью.",
            "собака": "Домашнее животное, известное своей преданностью и дружелюбным характером.",
            "река": "Естественный поток воды, текущий по земле.",
            "стол": "Предмет мебели с плоской поверхностью, поддерживаемый одним или несколькими ножками.",
            "кошка": "Домашнее животное, известное своим независимым характером и ловкостью.",
            "автомобиль": "Транспортное средство с мотором, предназначенное для перевозки людей и грузов.",
            "школа": "Учебное заведение, где обучаются дети и подростки.",
            "птица": "Животное с перьями, способное летать.",
            "цветок": "Разнообразная часть растения, обычно яркая и ароматная, используемая для размножения.",
            "горы": "Высокие возвышенности на земле, образованные геологическими процессами.",
            "море": "Большая часть соленой воды, меньшая по сравнению с океаном, окружающая сушу.",
            "луна": "Естественный спутник Земли, видимый ночью, отражающий солнечный свет.",
            "звезда": "Огненное небесное тело, светящееся из-за термоядерных реакций в его центре.",
            "музыка": "Искусство организации звуков и тишины во времени, создающее гармонию и ритм.",
            "фильм": "Визуальное искусство, состоящее из последовательности движущихся изображений, рассказывающее историю.",
            "компьютер": "Электронное устройство, способное выполнять вычисления и обрабатывать данные.",
            "друг": "Человек, с которым у вас близкие отношения, основанные на доверии и взаимопонимании.",
            "путешествие": "Перемещение из одного места в другое, часто с целью отдыха или исследования.",
            "наука": "Система знаний, основанная на наблюдениях, экспериментах и логическом анализе.",
            "искусство": "Творческое выражение, которое может принимать различные формы, такие как живопись, музыка, театр."
        }

        self.right_word = random.choice(list(self.sentence))
        self.word = []
        self.popatka = 0

        self.result_message = tk.StringVar(self)

        self.difficulty_var = tk.StringVar(self)
        self.difficulty_var.set("Mid")

        self.option = None

        self.frame = tk.Frame(self, width=1000, height=600, background="#66287F")
        self.entry = None

        self.label = tk.Label(self.frame, text="Welcome to guess the world game!", font=("Helvetica", 15),
                              bg="#66287F")
        self.label1 = None
        self.button = tk.Button(self.frame, text="Start!", command=self.select_difficulty,
                                background="#DEB4EF", font=("Helvetica", 15, "bold"), foreground="#000000")

        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.label.place(relx=0.5, rely=0.4, anchor="center")
        self.button.place(relx=0.5, rely=0.5, anchor="center", width=100, height=50)


    def select_difficulty(self):  # уровень сложности

        self.frame.place_forget()
        self.frame = tk.Frame(self, width=1000, height=600, background="#66287F")

        self.label = tk.Label(self.frame, text="Choose a difficulty", font=("Helvetica", 15),
                              background="#66287F")

        self.option = tk.OptionMenu(self.frame, self.difficulty_var,
                                    "Easy", "Mid", "Hard")

        self.button = tk.Button(self.frame, text="Ready", command=self.level,
                                background="#DEB4EF", font=("Helvetica", 15, "bold"), foreground="#000000")

        self.label.place(relx=0.5, rely=0.4, anchor="center")
        self.option.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.button.place(relx=0.5, rely=0.6, anchor="center")


    def level(self):

        if self.difficulty_var.get() == "Easy":
            self.popatka = 8
        elif self.difficulty_var.get() == "Mid":
            self.popatka = 4
        else:
            self.popatka = 2

        self.start_game()


    def start_game(self):  # сама игра

        self.frame.place_forget()

        self.frame = tk.Frame(self, width=1000, height=600, background="#66287F")

        self.label = tk.Label(self.frame, text= f"Guess the word in {self.popatka} attempts", font=("Helvetica", 15),
                              background="#66287F")

        self.label1 = tk.Label(self.frame, text= self.sentence[self.right_word], font=("Helvetica", 14),
                              background="#66287F")


        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.label.place(relx=0.5, rely=0.2, anchor="n")
        self.label1.place(relx=0.5, rely=0.3, anchor="n")

        self.update_popatka()


    def update_popatka(self):  # попытки

        self.popatka -= 1
        self.create_entry_fields()


    def proverka(self): # проверка ответа

        self.word = str(self.entry.get()).lower()

        if self.right_word == self.word:
            self.popatka = -1

        self.result()


    def result(self): # результат

        if self.popatka == -1:
            self.result_message.set("You win")
            self.result_frame()
        elif self.popatka == 0:
            self.result_message.set("You lose")
            self.result_frame()
        else:
            self.start_game()


    def create_entry_fields(self):  # ввод ответа

        self.entry = tk.Entry(self.frame, width=40)

        self.button = tk.Button(self.frame, text="Ok", command=self.proverka,
                                background="#DEB4EF", font=("Helvetica", 15, "bold"), foreground="#000000")

        self.button.place(relx=0.5, rely=0.6, anchor="center")
        self.entry.place(rely=0.48, relx=0.38)


    def result_frame(self):  # выход или ресстарт

        self.frame.place_forget()

        self.frame = tk.Frame(self, width=1000, height=600, background="#66287F")

        self.label = tk.Label(self.frame, textvariable=self.result_message,
                              font=("Helvetica", 15),
                              background="#66287F")

        self.label1 = tk.Label(self.frame, text=self.right_word, font=("Helvetica", 14),
                               background="#66287F")

        self.button = tk.Button(self.frame, text="Exit", command=self.quit,
                                background="#DEB4EF", font=("Helvetica", 15, "bold"), foreground="#000000")

        restart_button = tk.Button(self.frame, text="Restart", command=self.restart_game,
                                   background="#DEB4EF", font=("Helvetica", 15, "bold"), foreground="#000000")

        self.button.place(rely=0.5, relx=0.473)
        restart_button.place(rely=0.6, relx=0.456)
        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.label.place(relx=0.5, rely=0.25, anchor="n")
        self.label1.place(relx=0.5, rely=0.35, anchor="n")


    @staticmethod
    def restart_game():  # ресстарт игры
        python = sys.executable
        os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    app = Gallows()
    app.mainloop()
