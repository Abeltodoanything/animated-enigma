import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename='simplex')
window.title("ANIMATED-ENIGMA")
window.geometry("600x700")

items = ['ice cream', 'pizza', 'broccoli']
foodstring = tk.StringVar(value= items[0])

combo = ttk.Combobox(window, textvariable=foodstring)
combo['values'] = items
combo.pack(pady=10)

combo.bind('<<ComboboxSelected>>', lambda event: print(foodstring.get()))

# run
window.mainloop()