# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:33:53 2023

@author: ghada
"""
#calling libraries
import socket
from tkinter import *
from tkinter import messagebox
import random
import threading

#define gui
window = Tk()
window.title("Client side")
window.geometry("400x400")
frame = Frame(window)
frame.pack(pady = 20)

#define game
matches = [1, 1, 2, 2, 3, 3]
random.shuffle(matches)
count=0
answer_list = []
answer_dict = {}

inc2 =0
def Matching(btn, index):
    global count, answer_list, answer_dict
    if btn['text'] == ' ' and count < 2:
        btn['text'] = matches[index]
        answer_list.append(index)
        answer_dict[btn] = matches[index]
        count += 1
    
    if len(answer_list) == 2 :
                if matches[answer_list[0]] == matches[answer_list[1]]:
                    for key in answer_dict:
                        key['bg'] = 'green'
                        key['fg'] = 'white'
                    c.send('match'.encode('UTF-8'))
                    count = 0
                    answer_list = []
                    answer_dict = {}
                else:
                    c.send("wrong match".encode('UTF-8'))
                    messagebox.showinfo("incorrect", "Wrong Match !!!!!")
                    count = 0
                    answer_list = []
                    for key in answer_dict:
                        key['text'] = ' '
                    answer_dict = {}
            
                    
#button definations        
btn1 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn1, 0))
btn2 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn2, 1))
btn3 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn3, 2))
btn4 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn4, 3))
btn5 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn5, 4))
btn6 = Button(frame, text=' ', height=5, width=10, command=lambda: Matching(btn6, 5))
#button place
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
#label for matching
my_label = Label(window, text="")
my_label.pack(side= BOTTOM, pady = 10)

player2 = Label(window, text="Player2: 0")
player2.pack(pady = 10)

            
def handler():
    global inc2
    while True:
        x = c.recv(1024)
        x = x.decode("UTF-8")
        if x == "match":
         my_label.config(text="Correct Match!\n play again...")
         inc2 += 1
         player2.config(text= "player2: {inc2}".format(inc2=inc2))
         if inc2 == 3:
             messagebox.showinfo("Congratulation", "*** player1 win ***")
             window.destroy()
        elif x == "wrong match":
            my_label.config(text="Wrong Match!")
           
        

#define socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 7002
c.connect((host,port))

ithread=threading.Thread(target=handler)
#ithread.daemon=True
ithread.start()

    
window.mainloop()