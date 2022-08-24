from tkinter import *
from PIL import ImageTk, Image



# Menu Window
def main_menu():
    Menu = Tk()
    Menu.title("Weapon Clash")
    Menu.attributes('-fullscreen', True)
    Menu['bg'] = '#333d79'


    # Multiplayer Window Open
    def multiplayer_win():
        Menu.destroy()  # Close Menu Window
        # Makes Multiplayer game window
        Multiplayer_win = Tk()
        Multiplayer_win.title("Weapon Clash")
        Multiplayer_win['bg'] = '#333d79'
        Multiplayer_win.attributes('-fullscreen', True)


        # Back to main menu Button in Multiplayer mode
        def back():
            Multiplayer_win.destroy()
            main_menu()
        # Back to menu button
        mp_back_btn = Button(Multiplayer_win, text="Back", command=back)
        mp_back_btn.place(relx=-0.0004, rely=-0.0004, width=150, height=90)
        mp_back_btn['bg'] = 'red'
        mp_back_btn['fg'] = '#333d79'
        mp_back_btn['bd'] = 15
        mp_back_btn.config(font=("Alumni Sans Collegiate One", 30, "bold"))
        # function that changes the colour of the Back button when mouse is on it
        def back_button_color_ent(e):
            mp_back_btn['bg'] = '#D90000'
        def back_button_color_lea(e):
            mp_back_btn['bg'] = "red"
        # When Mouse Courser is on Exit button
        mp_back_btn.bind("<Enter>", back_button_color_ent)
        mp_back_btn.bind("<Leave>", back_button_color_lea)

        def mp_tutorial():
            Multiplayer_tutorial_win = Tk()
            Multiplayer_tutorial_win.title("Weapon Clash")
            Multiplayer_tutorial_win.attributes('-fullscreen', True)
            Multiplayer_tutorial_win['bg'] = '#333d79'

        mp_tutorial_btn = Button(Multiplayer_win, text="Tutorial", command=mp_tutorial)
        mp_tutorial_btn.place(relx=0.25, rely=0.75, width=280, height=90)
        mp_tutorial_btn['bg'] = 'red'  # faebef
        mp_tutorial_btn['fg'] = '#333d79'
        mp_tutorial_btn['bd'] = 15
        mp_tutorial_btn.config(font=("Alumni Sans Collegiate One", 30, "bold"))
        # function that changes the colour of the Back button when mouse is on it
        def tutorial_button_color_ent(e):
            mp_tutorial_btn['bg'] = '#D90000'
        def tutorial_button_color_lea(e):
            mp_tutorial_btn['bg'] = "red"
        # When Mouse Courser is on Exit button
        mp_tutorial_btn.bind("<Enter>", tutorial_button_color_ent)
        mp_tutorial_btn.bind("<Leave>", tutorial_button_color_lea)






    # Multiplayer Button
    multiplayer_btn = Button(Menu, text="Multiplayer", command=multiplayer_win)
    multiplayer_btn['bg'] = 'yellow'  # faebef
    multiplayer_btn['fg'] = '#333d79'
    multiplayer_btn['bd'] = 15
    multiplayer_btn.config(font=("Alumni Sans Collegiate One", 30, "bold"))
    multiplayer_btn.place(relx=0.6, rely=0.1, width=500, height=100)
    # function that changes the colour of the Multiplayer button when mouse is on it
    def multi_button_color_ent(e):
        multiplayer_btn['bg'] = '#FFCD00'
    def multi_button_color_lea(e):
        multiplayer_btn['bg'] = "yellow"
    # When Mouse Courser is on Multiplayer button
    multiplayer_btn.bind("<Enter>", multi_button_color_ent)
    multiplayer_btn.bind("<Leave>", multi_button_color_lea)





    # Bot Button
    def Bot():
        Menu.destroy()  # Close Menu Window
        # Makes Bot game window
        bot_game = Tk()
        bot_game.title("Weapon Clash")
        bot_game['bg'] = '#333d79'
        bot_game.attributes('-fullscreen', True)

        # Back to main menu Button in Multiplayer mode
        def back():
            bot_game.destroy()
            main_menu()
        # Back to menu button
        bt_back_btn = Button(bot_game, text="Back", command=back)
        bt_back_btn.place(x=1, y=1, width=150, height=90)
        bt_back_btn['bg'] = 'red'  # faebef
        bt_back_btn['fg'] = '#333d79'
        bt_back_btn['bd'] = 15
        bt_back_btn.config(font=("Alumni Sans Collegiate One", 30, "bold"))
        # function that changes the colour of the Back button when mouse is on it
        def back_button_color_ent(e):
            bt_back_btn['bg'] = '#D90000'
        def back_button_color_lea(e):
            bt_back_btn['bg'] = "red"
        # When Mouse Courser is on Exit button
        bt_back_btn.bind("<Enter>", back_button_color_ent)
        bt_back_btn.bind("<Leave>", back_button_color_lea)

    # Bot Button
    bot_btn = Button(Menu, text="Play Agianst Bot", command=Bot)
    bot_btn['bg'] = 'yellow'  # faebef
    bot_btn['fg'] = '#333d79'
    bot_btn['bd'] = 15
    bot_btn.config(font=("Alumni Sans Collegiate One", 30, "bold"))
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
        Menu.destroy()
    # Exit Button
    exit_btn = Button(Menu, text="🚪Exit🚪", command=Exit)
    exit_btn['bg'] = 'red'  # faebef
    exit_btn['fg'] = '#333d79'
    exit_btn['bd'] = 15
    exit_btn.config(font=("Alumni Sans Collegiate One", 30, "bold"))
    exit_btn.place(relx=0.85, rely=0.85, width=200, height=100)
    # function that changes the colour of the Exit button when mouse is on it
    def exit_button_color_ent(e):
        exit_btn['bg'] = '#D90000'
    def exit_button_color_lea(e):
        exit_btn['bg'] = "red"
    # When Mouse Courser is on Exit button
    exit_btn.bind("<Enter>", exit_button_color_ent)
    exit_btn.bind("<Leave>", exit_button_color_lea)

    Menu.mainloop()





main_menu()