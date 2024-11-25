#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Калькулятор')

        self.first_number = tk.Entry(master, width=12)
        self.first_number.pack()

        self.second_number = tk.Entry(master, width=12)
        self.second_number.pack(pady=2)

        self.add_button = tk.Button(
            master, text="+", width=13, command=self.add)
        self.add_button.pack(pady=2)

        self.sub_button = tk.Button(
            master, text="-", width=13, command=self.sub)
        self.sub_button.pack(pady=2)

        self.mul_button = tk.Button(
            master, text="*", width=13, command=self.mul)
        self.mul_button.pack(pady=2)

        self.div_button = tk.Button(
            master, text="/", width=13, command=self.div)
        self.div_button.pack(pady=2)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=2)

    def get_numbers(self):
        try:
            num1 = float(self.first_number.get())
            num2 = float(self.second_number.get())
            return num1, num2
        except ValueError:
            self.result_label.config(text="ошибка")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            res = num1 + num2
            self.result_label.config(text=str(res))

    def sub(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            res = num1 - num2
            self.result_label.config(text=str(res))

    def mul(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            res = num1 * num2
            self.result_label.config(text=str(res))

    def div(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                res = num1 / num2
                self.result_label.config(text=str(res))
            else:
                self.result_label.config(text="ошибка")


if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
