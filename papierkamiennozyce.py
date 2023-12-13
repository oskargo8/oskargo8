from random import choice
from tkinter import *

dostepne_opcje = ["papier", "kamien", "nozyce"]
clicks1=0
clicks2=0
clicks3=0
clicks4=0
def play(player, cpu):
    win_with = {"papier": "kamien", "nozyce": "papier", "kamien": "nozyce"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


def play_cmd(player):
    global text_label
    cpu = choice(dostepne_opcje)

    is_user_winner = play(player, cpu)

    if is_user_winner is None:
        text_label.config(text="remis", fg="black")
    elif is_user_winner:
        text_label.config(text="wygrales", fg="green")
    else:
        text_label.config(text="przegrales", fg="red")

    global clicks1
    global clicks2
    global clicks3
    global clicks4
    if is_user_winner is None:
        clicks2 +=1
    elif is_user_winner:
        clicks1 +=1
    else:
        clicks3 +=1

    while True:
        clicks4 += 1
        if clicks4 == 20:
            lab7.config(text="gra zakonczona", font=('Helvetica bold',30))
        if clicks4<21:
            break



    lab1.config(text=clicks1)
    lab2.config(text=clicks2)
    lab3.config(text=clicks3)
    lab4.config(text=clicks4)
    lab5.config(text=round(clicks1/(clicks4+0.000001),2))

    global text_label2
    if clicks1/(clicks4+0.000001) >0.4:
        text_label2.config(text="jestes bardzo dobrym graczem", fg="green")
    elif clicks1/(clicks4+0.000001) >0.35:
        text_label2.config(text = "jestes dobrym graczem", fg="blue")
    else:
        text_label2.config(text="jestes słabym graczem", fg="red")





root = Tk()
root.title("Papier, kamien, nozyce")
root.geometry("700x500")

text_label1 = Label(root, text="zagrajmy w gre. Gra toczy się do 20 gier", font=30)
text_label1.pack()

text_label = Label(root, text="", font=30)
text_label.pack()


prz1=Button(root, text="Papier", font=40, width=10, command=lambda: play_cmd("papier")).pack()
prz2=Button(root, text="Kamien", font=40, width=10, command=lambda: play_cmd("kamien")).pack()
prz3=Button(root, text="Nozyce", font=40, width=10, command=lambda: play_cmd("nozyce")).pack()

#ilosc klikniec
lab10= Label(root, text="ilosc wygranych", font=30, fg="green")
lab1= Label(root, text="", font=30, fg="green")
lab10.pack()
lab1.pack()
lab20 = Label(root, text="ilosc remisów", font=30, fg="black")
lab2 = Label(root, text=" ", font=30, fg="black")
lab20.pack()
lab2.pack()
lab30 = Label(root, text="ilosc przegranych", font=30, fg="red")
lab3 = Label(root, text="", font=30, fg="red")
lab30.pack()
lab3.pack()

#liczba gier
lab40 = Label(root, text="liczba gier", font=30, fg="black")
lab40.pack()
lab4 = Label(root, text="", font=30, fg="black")
lab4.pack()

#wspolczynnik wygranych
lab6 = Label(root, text="twoj wspolczynnik wygranych to", font=30, fg="black")
lab6.pack()
lab5 = Label(root, text=clicks1/(clicks4+0.000001), font=30, fg="black")
lab5.pack()
lab7 = Label(root, text="", font=60, fg="Blue")
lab7.pack()
#jestes dobrym/zlym graczem
text_label2 = Label(root, text="", font=30)
text_label2.pack()


root.mainloop()
