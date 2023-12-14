from tkinter import *
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title("Rock Paper scissor")
root.configure(background="#9b59b6")

#picture including
rock_pic  = ImageTk.PhotoImage(Image.open("rock_symbol.png"))
paper_pic = ImageTk.PhotoImage(Image.open("paper_symbol.png"))
scissor_pic = ImageTk.PhotoImage(Image.open("scissor_symbol.png"))
rock_pic_comp = ImageTk.PhotoImage(Image.open("rock_symbol.png"))
paper_pic_comp = ImageTk.PhotoImage(Image.open("paper_symbol.png"))
scissor_pic_comp = ImageTk.PhotoImage(Image.open("scissor_symbol.png"))

#inserting pictures
user_label = Label(root, image=rock_pic,bg="#9b59b6")
comp_label = Label(root, image=rock_pic_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#score display
player_score = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
comp_score = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
comp_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

#inidicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white").grid(row=0,column=3)
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white").grid(row=0,column=1)

#Result messages
msg = Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)


def update_msg(n):
    msg["text"]= n

def update_score():
    score = int(player_score["text"])
    score+=1
    player_score["text"] = str(score)

def update_comp_score():
    score = int(comp_score["text"])
    score+=1
    comp_score["text" ] = str(score)


def checkwin(player,computer):
    if player==computer:
        update_msg("Its a tie!!!")
    elif player=="rock":
        if computer=="paper":
            update_msg("You Loose")
            update_comp_score()
        else:
            update_msg("You Win")
            update_score()
    elif player=="paper":
        if computer=="rock":
            update_msg("You Win")
            update_score()
        else:
            update_msg("You Loose")
            update_comp_score()
    elif player=="scissor":
        if computer=="rock":
            update_msg("you Loose")
            update_comp_score()
        else:
            update_msg("You Win")
            update_score()
    
        
        
#updating choices
choice = ["rock","paper","scissor"]
def update_choices(n):
    #for user
    if n=="rock":
        user_label.configure(image=rock_pic)
    elif n=="paper":
        user_label.configure(image=paper_pic)
    else:
        user_label.configure(image=scissor_pic)

    #for computer
    comp = choice[randint(0,2)]
    if comp =="rock":
        comp_label.configure(image=rock_pic_comp)
    elif comp=="paper":
        comp_label.configure(image=paper_pic_comp)
    else:
        comp_label.configure(image=scissor_pic_comp)

    checkwin(n,comp)


#button for options
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command= lambda:update_choices("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command= lambda:update_choices("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command= lambda:update_choices("scissor")).grid(row=2,column=3)

root.mainloop()