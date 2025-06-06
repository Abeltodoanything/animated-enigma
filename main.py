import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
import os
from dotenv import load_dotenv 
from playwright.sync_api import sync_playwright
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"))

window = ttk.Window(themename='darkly')
window.attributes('-topmost', True)
window.title("CQBv2")
window.resizable(False,False)
window.bind('<Escape>', lambda event: window.quit())

window_width = 505
window_height = 740
comp_width = window.winfo_screenwidth()
comp_height = window.winfo_screenheight()

left = int(comp_width /2 - window_width /2)
top = int(comp_height /2 - window_height /2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')


def start_script():
    with sync_playwright() as playwright:
        run(playwright)

def run(playwright):    
    output_box._textbox.configure(state='normal')
    output_box.insert('end', f"STARTED {cvs_usr.get()}+{cvs_pas.get()}+{cvs_link.get()}+{qtn_num.get()}\n")
    output_box._textbox.configure(state='disabled')
    print("Current text:", output_box.get("0.0", "end"))

    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()
    page.goto(cvs_link.get())
    
    # Login sequence
    page.get_by_role("textbox", name="Username").fill(cvs_usr.get())
    page.get_by_role("textbox", name="Password").fill(cvs_pas.get())
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Yes, this is my device").click()
    
    context.close()
    browser.close()

# Variables
cvs_usr = ttk.StringVar()
cvs_pas = ttk.StringVar()
cvs_link = ttk.StringVar()
qtn_num = ttk.IntVar()
display_output = ctk.StringVar()

# Title
title = ttk.Label(window, text= 'C.Q.B.v2', font=("Helvetica", 20, 'bold' ))
title.pack(pady=10, padx=10, anchor='nw')
# Sign in Frame
sign_in = ttk.Labelframe(window, borderwidth=1, relief='solid', text='Sign in')
sign_in.pack(pady=10, padx=10, anchor='nw', fill='x')

# Canvas Username
usr_title = ttk.Label(sign_in, text='Canvas Username')
usr_title.grid(column=0, row=0, pady=10, padx=10)

usr_entry = ttk.Entry(sign_in, textvariable=cvs_usr)
usr_entry.grid(column=1, row=0, pady=10, padx=10)

# Canvas Password
pas_title = ttk.Label(sign_in, text='Canvas Password')
pas_title.grid(column=0, row=2,pady=10, padx=10)

pas_entry = ttk.Entry(sign_in, show='*', textvariable=cvs_pas)
pas_entry.grid(column=1, row=2,pady=10, padx=10)

# Quiz Information Frame
quiz_info = ttk.Labelframe(window, borderwidth=1, relief='solid', text= 'Quiz information')
quiz_info.pack(padx=10, anchor='nw', fill='x')
# Link & number of questions
link_title = ttk.Label(quiz_info, text='URL to Canvas Quiz')
link_title.grid(column=0,row=0,pady=10, padx=10)
link_entry = ttk.Entry(quiz_info, textvariable=cvs_link)
link_entry.grid(column=1,row=0,pady=10, padx=10)

ques_title = ttk.Label(quiz_info, text='# of questions')
ques_title.grid(column=0,row=1,pady=10, padx=10)
ques_entry = ttk.Spinbox(quiz_info, from_=0, to=50, textvariable=qtn_num)
ques_entry.grid(column=1, row=1,pady=10, padx=10)

# Start & Output
end_frame = ttk.Frame(window)
end_frame.pack(pady=5, padx=10)
start_btn = ctk.CTkButton(end_frame, text='Start', command= start_script)
start_btn.pack(pady=10)

output_box = ctk.CTkTextbox(end_frame,height=450,width= 730, font=("Consolas", 12), activate_scrollbars=True)
output_box._textbox.configure(wrap='word', state='disabled')
output_box.pack()

# run
window.mainloop()