from tkinter import *

#menu
Menu = Tk()
Menu.title("Paper Scissors Rock")
Menu.configure(width=1920, height=1080)




#Multiplayer Button


multiplayer_game = Tk()
multiplayer_game.title("Paper Scissors Rock")


multiplayer = Button(Menu, text="Multiplayer")
multiplayer.place(x=1500, y=400,width=200,height=100)
if multiplayer == "Multiplayer":
    multiplayer_game = Tk()
    multiplayer_game.title("Paper Scissors Rock")
    multiplayer_game.configure(width=1920, height=1080)





#Bot Button
def Bot():
    print("LOL Too obvious")



Bot = Button(Menu, text="Bot", command=Bot)
Bot.place(x=450, y=400,width=70,height=40)




#Exit the game
def Exit():
    Menu.quit()

Exit = Button(Menu, text="Exit", command=Exit)
Exit.place(x=50, y=100,width=70,height=40)






Menu.mainloop()









