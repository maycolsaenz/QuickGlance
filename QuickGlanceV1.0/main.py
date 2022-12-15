#%% Importing libraries

import tkinter
#%%
window = tkinter.Tk()
# This places the main window on top of other programs
window.attributes('-topmost',True)
window.geometry("700x100")
window.title("QuickGlance")
window.configure(bg='#DDE4EA')

# Testing archor phrase
displayed_phrase = 'This is a dummy phrase wich is really long on the screen'

############# Main label to display anchor phrases##########
MainLabel = tkinter.Label(window, 
text = displayed_phrase,
bg = '#EAC950',
font=("Helvetica", 20),
#fg = '#EAC950' This sets font color
)

# MainLabel placing
#MainLabel.grid(row = 0, column = 1)
MainLabel.pack(side="top")

##################### Secondary label #######################

# Second_label = tkinter.Label(window, 
# text = displayed_phrase,
# bg = '#FF6501',
# font=("Helvetica", 11),
# fg = '#0C0E13'
# )

# Secondary label placing
#Second_label.grid(row = 1, column = 0)



window.mainloop()
# %%
