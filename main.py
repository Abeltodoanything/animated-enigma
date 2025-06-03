import customtkinter

window = customtkinter.CTk()
window.title("ANIMATED-ENIGMA")
window.geometry("500x700")
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('theme.json')

font1 = 'Helvetica'

# =CANVAS QUIZ BOT========================================================================= #


# Title
customtkinter.CTkLabel(window, 
      width=500,
      text="Canvas quiz bot",
      font=(font1, 25, 'bold'),
      ).pack()
# INFO
customtkinter.CTkLabel(window, 
      text="Username:", 
      font=(font1, 15),
      ).pack(pady=5)
customtkinter.CTkEntry(window, 
      font=(font1, 15)).pack()

customtkinter.CTkLabel(window, 
      text="Password:", 
      font=(font1, 15),
      ).pack(pady=5)
customtkinter.CTkEntry(window, 
      font=(font1, 15),
      show='*').pack()

customtkinter.CTkLabel(window, 
      text="Canvas quiz link:", 
      font=(font1, 15),
      ).pack(pady=5)
customtkinter.CTkEntry(window, 
      font=(font1, 15)).pack()

customtkinter.CTkButton(window, 
       text="Start", 
       width=20
       ).pack(pady=25)

customtkinter.CTkTextbox(window, 
     width=400,
     height=200,
     border_width=2,
     corner_radius=10,
     border_color='#505050',
     font=('Monaco', 12),
     activate_scrollbars=True, 
     ).pack()
# =AUTOCLICKER========================================================================= #

# =CALCULATOR========================================================================= #
# ========================================================================== #
# ========================================================================== #
# ========================================================================== #

window.mainloop()
