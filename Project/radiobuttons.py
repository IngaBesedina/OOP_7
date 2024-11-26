#!/usr/bin/env python3
# -*- coding: utf-8 -


from tkinter import Tk, StringVar, Radiobutton, END
from tkinter.ttk import Frame, Label


class WorkWithRBtn(Frame):
    def __init__(self):
        super().__init__()
        
        self.data = {
            'Вася': '+79869889496',
            'Петя': '+79045496076',
            'Маша': '+79701714479'
        }

        self.initUI()

    def initUI(self):
        self.master.title('Работа с радиокнопками')
        self.pack(fill='both', expand=True)

        frame1 = Frame(self)
        frame1.pack(side='left')

        phone_number = Label(self)
        phone_number.pack(side='left', padx=10, pady=10)

        var = StringVar(value="")
        for name, phone in self.data.items():
            radiobtn = Radiobutton(frame1, text=name, variable=var, 
                                   value=phone, 
                                   indicatoron=0,
                                   width=10,
                                   height=3,
                                   command=lambda: 
                                   self.update_label(var, phone_number))
            radiobtn.pack(anchor='w')

    @staticmethod
    def update_label(var: str, label: Label):
        selected = var.get()
        label.config(text=selected)


def main():
    root = Tk()
    WorkWithRBtn()
    root.mainloop()


if __name__ == '__main__':
    main()