from tkinter import *
import random
import time
import tkinter.messagebox as tmsg

def getscore(event):
    global score,acolor,fgc,color
    if acolor.get() == fgc:
        score += 1
        fscore = f"Score : {score}"
        l1.config(text=fscore)
        l1.update()
        fgc = random.choice(color)
        l3.config(text=random.choice(color),fg=fgc)
        l3.update()

    acolor.set("")

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x400")
    root.minsize(500,400)
    root.maxsize(500,400)

    l0 = Label(text="Type in the color of word and not the word text!",font="lucida 15 bold")
    l0.pack(pady=20)

    score =0
    Timeleft = IntVar()
    Timeleft.set(60)

    color = ['blue', 'black', 'red', 'orange', 'white', 'purple', 'pink','yellow']
    ltext = f"Time left : {Timeleft.get()}"
    qcolor = random.choice(color)
    fgc = random.choice(color)

    l1 = Label(text=f"Score : {score}",font="lucida 12 bold")
    l1.pack()

    l2 = Label(text=ltext , font="lucida 12 bold")
    l2.pack()

    l3 = Label(text=qcolor, font="lucida 45 bold",fg=fgc)
    l3.pack(pady=20)

    acolor = StringVar()
    in_color = Entry(root, textvariable = acolor)
    in_color.pack()
    root.bind('<Return>', getscore)

    for i in range(61):
        Timeleft.set(60-i)
        ltext = f"Time left : {Timeleft.get()}"
        l2.config(text=ltext)
        l2.update()
        time.sleep(1)

    l0.config(text=" ")
    l0.update()
    l1.config(text=" ")
    l1.update()
    l2.config(text=" ")
    l2.update()
    l3.config(text=" ")
    l3.update()
    in_color.pack_forget()
    in_color.update()

    l4 = Label(text="Game Over!",font="lucida 40 bold",fg="red")
    l4.pack()
    l4.configure(anchor="center")

    tmsg.showinfo("Game status",f"Game Over! , Your score is {score}")

    root.mainloop()