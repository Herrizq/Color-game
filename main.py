from tkinter import *
import random
root = Tk()

#int, str etc.
Colors = ["red", "green", "blue", "pink", "orange", "yellow", "black", "grey","magenta"]
score_number = IntVar()
score_number.set(0)
time_num = IntVar()
time_num.set(60)

#Commands
def change(x):
    global text
    if time_num.get() == 60:
        root.after(1000, timer)
    if enter.get() == text['foreground']:
        score_number.set(score_number.get()+1)
        print(score_number.get())
        score = Label(root, text="Score : " + str(score_number.get()), font=(12))
        score.grid(row=1, column=0, columnspan=3)
        text.destroy()
        text = Label(root, text=random.sample(Colors, 1)[0], font=(12))
        text.grid(row=2, column=0, columnspan=3)
        text.config(foreground=random.sample(Colors, 1)[0])
    else:
        text.destroy()
        text = Label(root, text=random.sample(Colors, 1)[0], font=(12))
        text.grid(row=2, column=0, columnspan=3)
        text.config(foreground=random.sample(Colors, 1)[0])
    enter.delete(0, END)

def timer():
    global time
    if time_num.get() == 0:
        time = Label(root, text="Game Over!", font = (12))
        time.grid(row=3, column=0)
        enter = Entry(root, state=DISABLED)
        enter.grid(row=4, column=1)

    else:
        time.destroy()
        time_num.set(time_num.get() - 1)
        root.after(1000, timer)
        time = Label(root, text="Time left: " + str(time_num.get()), font = (12))
        time.grid(row=3, column=0)

def restart():
    time.destroy()
    time_num.set(61)
    score_number.set(0)
    score = Label(root, text="Score : " + str(score_number.get()), font=(12))
    score.grid(row=1, column=0, columnspan=3)
    enter = Entry(root)
    enter.grid(row=4, column=1)
    root.after(1000, timer)

#Display instruction
instruction = Label(root, text = "Write name of color that you can see.", font = (40))
instruction.grid(row = 0, column = 0, columnspan = 3)

#Display color
text = Label(root, text = random.sample(Colors, 1)[0], font = (12))
text.grid(row = 2, column = 0, columnspan = 3)
text.config(foreground = random.sample(Colors,1)[0])

#Enter an answear
enter = Entry(root)
enter.grid(row = 4, column = 1)
enter.bind("<Return>", (lambda event: change(enter.get())))

#Score
score = Label(root, text = "Score : " + str(score_number.get()), font =(12))
score.grid(row = 1, column = 0, columnspan =3 )

#Timer
time = Label(root, text = "Time left: " + str(time_num.get()), font = (12))
time.grid(row = 3, column = 0,columnspan =3)

#Restart
restart = Button(root, text = "Restart", command =restart)
restart.grid(row =5, column = 0)

root.mainloop()