# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:25:47 2023

@author: ghada
"""
from tkinter import *
from tkinter import messagebox
import random
window = Tk()
window.title("Matching Game")
window.geometry("400x400")

matches = [1,1,2,2,3,3]
random.shuffle(matches)

frame = Frame(window)
frame.pack(pady=30)

inc=0
count=0

#store index of each button
answer_list = []
#store button and its value
answer_dict = {}

def Matching(btn, index):
    global count, answer_list, answer_dict, inc 
    if btn['text'] == ' ' and count < 2:
        btn['text'] = matches[index]
        answer_list.append(index)
        answer_dict[btn] = matches[index]
        count += 1
    
    if len(answer_list) == 2 :
        if matches[answer_list[0]] == matches[answer_list[1]]:
            label_match.config(text="Correct Match!")
            inc += 1
            player1.config(text = "player1: {inc}".format(inc = inc))
            for key in answer_dict:
                key['bg'] = 'green'
                key['fg'] = 'white'
            count = 0
            answer_list = []
            answer_dict = {}
        else:
            label_match.config(text="Wrong Match!")
            count = 0
            answer_list = []
            messagebox.showinfo("incorrect", "Wrong Match !!!!!")
            for key in answer_dict:
                key['text'] = ' '
            answer_dict = {}

                 
#button definations        
btn1 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn1,0))
btn2 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn2,1))
btn3 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn3,2))
btn4 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn4,3))
btn5 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn5,4))
btn6 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn6,5))
#button place
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
#label for matching
label_match = Label(window, text="")
label_match.pack(side= BOTTOM, pady=10)
player1 = Label(window, text="player1: 0")
player1.pack(side= LEFT, pady=10)
window.mainloop()