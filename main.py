# Библиотека для создания GUI
import tkinter as tk


# Класс главного окна
class Main(tk.Frame):
    # Создаем конструктор класса
    def __init__(self, root):
        super().__init__(root)


# Если скрипт запущен как основная программа
if __name__ == '__main__':
    # Создание корневого окна программы
    root = tk.Tk()
    # Упаковка содержимого окна
    app = Main(root)
    app.pack()
    # Указываем название окна
    root.title('Drom.ru')
    # Указываем размеры окна
    root.geometry('650x450+300+200')
    # Блокируем изменение размеров окна
    root.resizable(False, False)
    # Запуск цикла работы GUI
    root.mainloop()
    