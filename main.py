from tkinter import *

#Doing puissance 4 gam with only three functions: placerSupport to make canvas and all main graphic details, placerPion(i,j,couleur) to place the token, and main function show() to launch game, change players and check if someone has won

column = 8
lines = 6
grille = [[0 for j in range(lines)] for i in range(column)]
joueur = 1
gameState = True

#Function to place the support of the game and clickable circles for placing tokens
def placerSupport():
    global canvas, grille
    canvas = Canvas(fenetre, width = 700, height = 600, bg = 'blue')
    canvas.pack()
    for i in range(column):
        for j in range(lines):
            grille[i][j] = 0
            canvas.create_oval(50+80*i,50+80*j,110+80*i,110+80*j,fill='white',outline='white')
            canvas.create_oval(50+80*i,50+80*j,110+80*i,110+80*j,fill='white',outline='white')



#Function placerPion(i,j,couleur) to let players place the tokens on the support by clickng on the circles on board
def placerPion(i,j,couleur):
    global joueur, grille
    if gameState == True:
        if grille[i][j] == 0:
            canvas.create_oval(50+80*i,50+80*j,110+80*i,110+80*j,fill=couleur,outline=couleur)
            grille[i][j] = joueur
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1
        else:
            print('Case déjà occupée !')
    else:
        print('Partie terminée !')

#main function show() to launch game, let players play, change players and check if someone has won and pack everything 
def show():


fenetre = Tk()
placerSupport()
fenetre.mainloop()
