#!/usr/bin/env python3
# -*- coding: utf-8 -

import tkinter as tk


class RainbowColor:
    def __init__(self, master):
        self.master = master

        self.color_code_entry = tk.Entry(master)
        self.color_code_entry.pack()

        self.color_name_label = tk.Label(master)
        self.color_name_label.pack()

        self.colors = {
            "красный": "#ff0000",
            "оранжевый": "#ff7d00",
            "желтый": "#ffff00",
            "зеленый": "#00ff00",
            "голубой": "#007dff",
            "синий": "#0000ff",
            "фиолетовый": "#7d00ff"
        }

        for color_name, color_code in self.colors.items():
            button = tk.Button(master, text=color_name, bg=color_code,
                               command=lambda name=color_name, code=color_code: self.set_color(name, code))
            button.pack()

    def set_color(self, color_name, color_code):
        self.color_code_entry.delete(0, tk.END)
        self.color_code_entry.insert(0, color_code)

        self.color_name_label.config(text=color_name)


if __name__ == '__main__':
    root = tk.Tk()
    rainbow = RainbowColor(root)
    root.mainloop()
