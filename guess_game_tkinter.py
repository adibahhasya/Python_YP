# Guess a number game 
from tkinter import * 
import random 
w = Tk()
w.title('Guess A number Game')
w.geometry('600x400') 

# background colour for window 
w.config(bg='#065569')
w.resizable(width=False, height =False)

#main logic 
ranNum=random.randint(1,10)
chance = 4
displayResult = StringVar()

def check_guess():
    global ranNum
    global chance
    userInput = int(user_input.get())
    if chance > 0: 
        if userInput == ranNum:
            msg = "Congratulations. You Won! " + str(ranNum) + " is the right number"
            user_input.config(state='disabled')
            guess_button.config(state='disabled')
        elif userInput > ranNum:
            chance = chance - 1
            msg = "Your Guess Is Too High. Think of a smaller number"
            user_input.delete(0,END)
        elif userInput < ranNum:
            chance = chance - 1
            msg = "Your Guess Is Too Low. Think of a higher number"
            user_input.delete(0,END)
    else: 
        msg = "Game Over! 0 Attempts Left. The Correct Number Was " + str(ranNum)
        user_input.config(state='disabled')
        guess_button.config(state='disabled')

    displayResult.set(msg)

#Create Widgets 
title=Label(w,text='Guess A number Game', font=('Arial', 20), fg='#fffcbd',bg='#065569')
gameInstruction=Label(w,text='Guess A number between 1 to 10 in 4 attempts', font=('Arial', 13), fg='#fffcbd',bg='#065569')
user_input=Entry(w,font=('Arial', 12))
guess_button = Button(w,text='Guess',font=('Arial',13),fg='#13d675',bg='black',command=check_guess)
exit_button = Button(w,text='Exit Game',font=('Arial',13),fg='white',bg='#b82741',command=w.destroy)
outputLabel = Label(w,text='Hints/Result', font=('Arial', 14), fg='#fffcbd',bg='#065569', textvariable=displayResult)
      
#Place Widgets
title.place(x=140,y=50)
gameInstruction.place(x=95,y=95)
user_input.place(x=180,y=150)
guess_button.place(x=370,y=147)
exit_button.place(x=300,y=300)
outputLabel.place(x=100,y=220)

w.mainloop()
