#!/usr/bin/env python3
# -*- coding: utf-8 -


from tkinter import Tk, Text, BOTH, X, N, LEFT, END
from tkinter.ttk import Frame, Button, Entry, Scrollbar


class WorkWithFiles(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Работа с файлами")
        self.pack(fill='both', expand=True)

        frame1 = Frame(self)
        frame1.pack(fill='x')

        file_name = Entry(frame1, width=30)
        file_name.pack(side='left', padx=10, pady=5)

        open_file = Button(frame1, text='Открыть', width=15,
                           command=lambda: self.open_file(file_name.get(), text))
        open_file.pack(side='left')

        save_file = Button(frame1, text='Сохранить', width=15,
                           command=lambda: self.save_file(file_name.get(), text))
        save_file.pack(side='left')

        frame2 = Frame(self)
        frame2.pack(fill='x')

        text = Text(frame2, width=50, height=20)
        text.pack(side='left')

        scroll = Scrollbar(frame2, command=text.yview)
        scroll.pack(side='left', fill='y')

        text.config(yscrollcommand=scroll.set)

    @staticmethod
    def open_file(file_name: str, text_area: Text):
        with open(file_name, 'r') as file:
            text_area.insert(1.0, file.read())

    @staticmethod
    def save_file(file_name: str, text_area: Text):
        with open(file_name, 'a') as file:
            file.write(text_area.get(1.0, END))


def main():
    root = Tk()
    WorkWithFiles()
    root.mainloop()


if __name__ == '__main__':
    main()
