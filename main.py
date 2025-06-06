import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

font1 = "Helvetica"
font2 = "Consolas"

window = ttk.Window(themename='darkly')
window.attributes('-topmost', True)
window.title("CQBv2")
window.resizable(False,False)
window.bind('<Escape>', lambda event: window.quit())

window_width = 505
window_height = 630
comp_width = window.winfo_screenwidth()
comp_height = window.winfo_screenheight()

left = int(comp_width /2 - window_width /2)
top = int(comp_height /2 - window_height /2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# Title
title = ttk.Label(window, text= 'C.Q.B.v2', font=(font1, 20, 'bold' ))
title.pack(pady=10, padx=10, anchor='nw')
# Sign in Frame
sign_in = ttk.Labelframe(window, borderwidth=1, relief='solid', text='Sign in')
sign_in.pack(pady=10, padx=10, anchor='nw', fill='x')

# Canvas Username
usr_title = ttk.Label(sign_in, text='Canvas Username')
usr_title.grid(column=0, row=0, pady=10, padx=10)

usr_entry = ttk.Entry(sign_in)
usr_entry.grid(column=1, row=0, pady=10, padx=10)

# Canvas Password
pas_title = ttk.Label(sign_in, text='Canvas Password')
pas_title.grid(column=0, row=2,pady=10, padx=10)

pas_entry = ttk.Entry(sign_in, show='*')
pas_entry.grid(column=1, row=2,pady=10, padx=10)

# Quiz Information Frame
quiz_info = ttk.Labelframe(window, borderwidth=1, relief='solid', text= 'Quiz information')
quiz_info.pack(padx=10, anchor='nw', fill='x')
# Link & number of questions
link_title = ttk.Label(quiz_info, text='URL to Canvas Quiz')
link_title.grid(column=0,row=0,pady=10, padx=10)
link_entry = ttk.Entry(quiz_info)
link_entry.grid(column=1,row=0,pady=10, padx=10)

ques_title = ttk.Label(quiz_info, text='# of questions')
ques_title.grid(column=0,row=1,pady=10, padx=10)
ques_entry = ttk.Spinbox(quiz_info, from_=0, to=50)
ques_entry.grid(column=1, row=1,pady=10, padx=10)

# Start & Output
start_btn = ctk.CTkButton(window, text='Start')
start_btn.pack(pady=10)

output_box = ctk.CTkTextbox(window, height=300, width=490, font=(font2, 12), corner_radius=5)
output_box._textbox.configure(wrap="word", state="disabled")
output_box.pack()

# run
window.mainloop()