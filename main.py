from tkinter import *

column = 8
lines = 6
grille = [[0 for j in range(lines)] for i in range(column)]
joueur = 1
gameState = True

def placerSupport():
    global canvas, grille
    canvas = Canvas(fenetre, width = 700, height = 600, bg = 'blue')
    canvas.pack()
    for i in range(column):
        for j in range(lines):
            grille[i][j] = 0
            canvas.create_oval(50+80*i,50+80*j,110+80*i,110+80*j,fill='white',outline='white')

def placerPion(event):
    global joueur, grille, gameState
    i = (event.x - 50) // 80
    if gameState == True and 0 <= i < column:  # Check that i is within the bounds of the array
        # Drop the piece and get the row number where it was dropped
        for j in range(lines-1, -1, -1):  # Start from the bottom and go up
            if grille[i][j] == 0:  # If the cell is empty
                grille[i][j] = joueur  # Drop the piece here
                break
        else:
            print('Column is full!')
            return
        couleur = 'red' if joueur == 1 else 'yellow'
        canvas.create_oval(50+80*i,50+80*j,110+80*i,110+80*j,fill=couleur,outline=couleur)
        canvas.update()  # Update the canvas to show the new piece
        # Check for a win
        for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:  # Directions to check
            for d in range(-3, 1):  # Distances to check
                x, y = i + d*dx, j + d*dy
                if all(0 <= x + k*dx < column and 0 <= y + k*dy < lines and grille[x + k*dx][y + k*dy] == joueur for k in range(4)):  # If all cells in the line are owned by the current player
                    print('Player', joueur, 'wins!')
                    gameState = False
                    return
        joueur = 1 if joueur == 2 else 2  # Switch player
    else:
        print('Game over!')

def show():
    global canvas, grille, gameState, joueur
    for i in range(column):
        for j in range(lines):
            grille[i][j] = 0
            canvas.create_oval(50+80*i,50+80*j,110+80*i,110+80*j,fill='white',outline='white')
    gameState = True
    joueur = 1
    canvas.bind_all('<Button-1>', placerPion)
    canvas.pack()

fenetre = Tk()
placerSupport()
show()
fenetre.mainloop()
