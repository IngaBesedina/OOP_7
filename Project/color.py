#!/usr/bin/env python3
# -*- coding: utf-8 -

import tkinter as tk


class RainbowColor:
    def __init__(self, root: tk.Tk):
        self.root = root

        self.color_code_entry = tk.Entry(root)
        self.color_code_entry.pack()

        self.color_label = tk.Label(root)
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
                root,
                width=13,
                text=color,
                bg=color_code,
                command=lambda name=color, code=color_code: self.set_color(
                    name, code
                ),
            )
            button.pack()

    def set_color(self, color: str, color_code: str):
        self.color_code_entry.delete(0, tk.END)
        self.color_code_entry.insert(0, color_code)

        self.color_label.config(text=color)


if __name__ == "__main__":
    root = tk.Tk()
    rainbow = RainbowColor(root)
    root.mainloop()
