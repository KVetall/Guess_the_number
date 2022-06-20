from tkinter import *
from random import randint
from tkinter import messagebox as mb

root = Tk()

root.title('Числовая угадайка')
root.resizable(False, False)
root.geometry('500x300')

welcome = Label(text='Добро пожаловать в числовую угадайку!\n', font='50')
welcome.pack()

enter_num = Label(text='Я загадал число от 1 до 100, отгадай и введи его ниже:\n', font='20')
enter_num.pack()


def getNumEnter():  # функция проверки введённых данных
    num = numEnter_field.get()
    if num.isdigit() and 0 < int(num) < 100:
        return int(num)
    else:
        result.config(text='Что-то вы ввели не то, нужно целое число от 1 до 100!')
        numEnter_field.delete(0, END)


numEnter_field = Entry(root, font='50', justify=CENTER)
numEnter_field.pack()

result = Label(root, font='50', justify=CENTER, fg='red')
result.pack()


def game():
    global try_count

    num = getNumEnter()
    if num is None:  # Функция ничего не вернула, значит была ошибка ввода
        return

    if num < rand_num:
        result.config(text='Загаданное число больше, попробуйте ещё разок')
        numEnter_field.delete(0, END)
        try_count += 1
    elif num > rand_num:
        result.config(text='Загаданное число меньше, попробуйте ещё разок')
        numEnter_field.delete(0, END)
        try_count += 1
    elif num == rand_num:
        result.config(text=f'Вы угадали, поздравляем! Количество ваших попыток: {try_count}')
        new_game()


def new_game():
    numEnter_field.delete(0, END)
    answer = mb.askyesno('Вопрос', 'Сыграем ещё разок?')
    if not answer:
        exit(0)


btnRead = Button(root, height=1, width=10, text="Угадать", command=game)
btnRead.pack()

try_count = 1
rand_num = randint(1, 100)

root.mainloop()
