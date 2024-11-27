#!/usr/bin/env python3
# -*- coding: utf-8 -

import tkinter as tk


class RainbowColor:
    def __init__(self, master: tk.Tk):
        self.master = master

        self.color_code_entry = tk.Entry(master)
        self.color_code_entry.pack()

        self.color_label = tk.Label(master)
        self.color_label.pack()

        self.colors = {
            "красный": "#ff0000",
            "оранжевый": "#ff7d00",
            "желтый": "#ffff00",
            "зеленый": "#00ff00",
            "голубой": "#007dff",
            "синий": "#0000ff",
            "фиолетовый": "#7d00ff",
        }

        for color, color_code in self.colors.items():
            button = tk.Button(
                master,
                width=2,
                bg=color_code,
                borderwidth=0,
                command=lambda name=color, code=color_code: self.set_color(
                    name, code
                ),
            )
            button.pack(side="left", padx=1)

    def set_color(self, color: str, color_code: str):
        self.color_code_entry.delete(0, tk.END)
        self.color_code_entry.insert(0, color_code)

        self.color_label.config(text=color)


if __name__ == "__main__":
    root = tk.Tk()
    rainbow = RainbowColor(root)
    root.mainloop()
