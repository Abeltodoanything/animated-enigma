import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
# import os
# from dotenv import load_dotenv
# from playwright.sync_api import Playwright, sync_playwright
# from openai import OpenAI

# window = ctk.CTk()
window = tk.Tk()
window.title("ANIMATED-ENIGMA")
window.geometry("500x400")
# ctk.set_appearance_mode('dark')
# ctk.set_default_color_theme('theme.json')
font1 = 'Helvetica'

# =TKINTER GUI========================================================================= #

# ctk.CTkLabel(window, width=500, text="Canvas quiz bot", font=(font1, 25, 'bold')).pack()

# ctk.CTkLabel(window, text="Username:", font=(font1, 15)).pack(pady=5)
# username1 = ctk.CTkEntry(window, font=(font1, 15))
# username1.pack()

# ctk.CTkLabel(window, text="Password:", font=(font1, 15)).pack(pady=5)
# password2 = ctk.CTkEntry(window, font=(font1, 15), show='*')
# password2.pack()

# ctk.CTkLabel(window, text="Canvas quiz link:", font=(font1, 15)).pack(pady=5)
# link1 = ctk.CTkEntry(window, font=(font1, 15))
# link1.pack()

# ctk.CTkLabel(window, text="Number of questions in quiz:", font=(font1, 15)).pack(pady=5)
# quiznum = ctk.CTkEntry(window, font=(font1, 15))
# quiznum.pack()

# ctk.CTkButton(window, text="Start", width=100).pack(pady=25)

# ctk.CTkTextbox(window, width=400, height=200, font=('Monaco', 12), activate_scrollbars=True).pack()

# #=====================================#
title_label = tk.Label(master=window, text="Miles to kilometers", font=(font1, 24, 'bold')).pack()

input_frame = tk.Frame(master=window)
input_frame.pack()
tk.Entry(master=input_frame).pack(side='left', pady=10)
tk.Button(master=input_frame, text='Convert').pack(side='left',pady=10)
window.mainloop()