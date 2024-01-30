import tkinter as tk

lines = 6
columns = 7
player = 1
results = [[0]*columns for _ in range(lines)]  # таблица результатов
buttons = [[None]*columns for _ in range(lines)]  # ссылки на кнопки

window = tk.Tk()

window.title("Puissance 4")
window.minsize(columns*50+200, lines*50+200)

label = tk.Label(window, text="Puissance 4")
label.pack()

label2 = tk.Label(window, text="Joueur " + str(player), width=10, height=2, bg="red", fg="white")
label2.pack()

frame = tk.Frame(master=window,width=columns*50+100, height=lines*50+100, bg="blue")
frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

def on_click(j):
    global player
    for i in reversed(range(lines)):  # проверяем с нижней кнопки
        if results[i][j] == 0:  # если кнопка не закрашена
            results[i][j] = player
            buttons[i][j].config(bg="red" if player == 1 else "yellow")
            player = 3 - player  # меняем игрока
            label2.config(text="Joueur " + str(player), bg="red" if player == 1 else "yellow")
            break

for i in range(lines):
    for j in range(columns):
        frame.columnconfigure(j, weight=1, minsize=25)
        frame.rowconfigure(i, weight=1, minsize=25)
        button = tk.Button(master=frame, width=3, height=2, bg='white')
        button.grid(row=i, column=j, padx=0, pady=0)
        button.bind('<Button-1>', lambda event, j=j: on_click(j))
        buttons[i][j] = button

window.mainloop()