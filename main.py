from tkinter import *

# Menu Window

Menu = Tk()
Menu.title("Paper Scissors Rock")
Menu.attributes('-fullscreen', True)
Menu['bg'] = '#333d79'

#alpha, -transparentcolor, -disabled, -fullscreen, -toolwindow, or -topmost

# Big Title of the game picture in the menu window



# Multiplayer Window Open
def multiplayer_win():

    Menu.destroy()          # Close Menu Window

    # Makes Multiplayer game window
    Multiplayer_win = Tk()
    Multiplayer_win.title("Paper Scissors Rock")
    Multiplayer_win['bg'] = '#333d79'
    Multiplayer_win.attributes('-fullscreen', True)

    def back():
        Multiplayer_win.destroy()

    #Back to menu button
    mp_back_btn = Button(Multiplayer_win, text="Back", command=back)



# Multiplayer Button
multiplayer_btn = Button(Menu, text="Multiplayer", command=multiplayer_win)
multiplayer_btn['bg'] = 'yellow'      #faebef
multiplayer_btn['fg'] = '#333d79'
multiplayer_btn['bd'] = 15

multiplayer_btn.config(font=("Alumni Sans Collegiate One", 30, "italic", "bold"))
multiplayer_btn.place(relx=0.6, rely=0.1, width=500, height=100)

# function that changes the colour of the Multiplayer button when mouse is on it
def multi_button_color_ent(e):
    multiplayer_btn['bg'] = '#FFCD00'

def multi_button_color_lea(e):
    multiplayer_btn['bg'] = "yellow"

# When Mouse Courser is on Multiplayer button
multiplayer_btn.bind("<Enter>", multi_button_color_ent)
multiplayer_btn.bind("<Leave>", multi_button_color_lea)



#Bot Button
def Bot():
    Menu.destroy()          # Close Menu Window
    # Makes Bot game window
    bot_game = Tk()
    bot_game.title("Paper Scissors Rock")
    bot_game['bg'] = '#333d79'
    bot_game.attributes('-fullscreen', True)

# Bot Button
bot_btn = Button(Menu, text="Play Agianst Bot", command=Bot)
bot_btn['bg'] = 'yellow'      #faebef
bot_btn['fg'] = '#333d79'
bot_btn['bd'] = 15
bot_btn.config(font=("Alumni Sans Collegiate One", 30, "italic", "bold"))
bot_btn.place(relx=0.6, rely=0.4, width=500, height=100)

# function that changes the colour of the Bot button when mouse is on it
def bot_button_color_ent(e):
    bot_btn['bg'] = '#FFCD00'

def bot_button_color_lea(e):
    bot_btn['bg'] = "yellow"

# When Mouse Courser is on Bot button
bot_btn.bind("<Enter>", bot_button_color_ent)
bot_btn.bind("<Leave>", bot_button_color_lea)



# Exit the game
def Exit():
    Menu.quit()

# Exit Button
exit_btn = Button(Menu, text="Exit", command=Exit)
exit_btn['bg'] = 'red'      #faebef
exit_btn['fg'] = '#333d79'
exit_btn['bd'] = 15
exit_btn.config(font=("Alumni Sans Collegiate One", 30, "italic", "bold"))
exit_btn.place(relx=0.6, rely=0.7, width=500, height=100)

# function that changes the colour of the Exit button when mouse is on it
def exit_button_color_ent(e):
    exit_btn['bg'] = '#D90000'

def exit_button_color_lea(e):
    exit_btn['bg'] = "red"

# When Mouse Courser is on Exit button
exit_btn.bind("<Enter>", exit_button_color_ent)
exit_btn.bind("<Leave>", exit_button_color_lea)








Menu.mainloop()









