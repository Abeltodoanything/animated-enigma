from tkinter import *

window = Tk()
window.title("ANIMATED-ENIGMA")
window.geometry("500x700")
window.configure(bg='#1C1C1C')

font1 = 'Helvetica'

# =CANVAS QUIZ BOT========================================================================= #



cqb = Frame(window, bg='#1C1C1C').pack()

# Title
Label(cqb, 
      width=500,
      text="Canvas quiz bot",
      font=(font1, 15),
      fg="#ffffff",
      bg="#1C1C1C",
      
      
      ).pack()
# INFO
cqbinfo = Frame(window, bg='#1C1C1C').pack()
Label(cqbinfo, 
      text="Username:", 
      font=(font1, 11, 'bold'),
      fg='#ffffff',
      bg='#1C1C1C'
      ).pack(pady=5)
Entry(cqbinfo, 
      width=20,
      font=(font1, 15)).pack()

Label(cqbinfo, 
      text="Password:", 
      font=(font1, 11, 'bold'),
      fg='#ffffff',
      bg='#1C1C1C'
      ).pack(pady=5)
Entry(cqbinfo, 
      width=20,
      font=(font1, 15),
      show='*').pack()

Label(cqbinfo, 
      text="Canvas quiz link:", 
      font=(font1, 11, 'bold'),
      fg='#ffffff',
      bg='#1C1C1C'
      ).pack(pady=5)
Entry(cqbinfo, 
      width=20,
      font=(font1, 15)).pack()

Button(cqbinfo, 
       text="Start", 
       width=20,
       bg='gray'
       ).pack(pady=25)

Text(cqbinfo, 
     width=40,
     height=15,
     font='Monaco'
     ).pack()
# =AUTOCLICKER========================================================================= #

# =CALCULATOR========================================================================= #
# ========================================================================== #
# ========================================================================== #
# ========================================================================== #

window.mainloop()
