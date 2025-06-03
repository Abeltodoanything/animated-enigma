import tkinter
import customtkinter as ctk

window = ctk.CTk()
window.title("ANIMATED-ENIGMA")
window.iconbitmap('icon.png')
window.geometry("500x700")
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('theme.json')

font1 = 'Helvetica'

# =CANVAS QUIZ BOT========================================================================= #
def print_info():
    getinfo = userentry0.get()
    print(getinfo)

# Title
ctk.CTkLabel(window, 
      width=500,
      text="Canvas quiz bot",
      font=(font1, 25, 'bold'),
      ).pack()
# INFO
ctk.CTkLabel(window, 
      text="Username:", 
      font=(font1, 15),
      ).pack(pady=5)
userentry0 = ctk.CTkEntry(window, 
      font=(font1, 15),
      ).pack()

ctk.CTkLabel(window, 
      text="Password:", 
      font=(font1, 15),
      ).pack(pady=5)
userentry1 = ctk.CTkEntry(window, 
      font=(font1, 15),
      show='*').pack()

ctk.CTkLabel(window, 
      text="Canvas quiz link:", 
      font=(font1, 15),
      ).pack(pady=5)
userentry2 = ctk.CTkEntry(window, 
      font=(font1, 15)).pack()

ctk.CTkButton(window, 
       text="Start",
       width=100,
       command=print_info
       ).pack(pady=25)

ctk.CTkTextbox(window, 
     width=400,
     height=200,
     font=('Monaco', 12),
     activate_scrollbars=True, 
     ).pack()

# =AUTOCLICKER========================================================================= #

# =CALCULATOR========================================================================= #
# ========================================================================== #
# ========================================================================== #
# ========================================================================== #

window.mainloop()
