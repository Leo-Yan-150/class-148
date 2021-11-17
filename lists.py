from tkinter import *
import random

root=Tk()

root.title("Random Lists Generator")
root.geometry("400x400")
root.configure(background = 'snow')

random_number_list=Label(root)
random_number_sorted_list=Label(root)

def randomlist():
    numberlist = random.sample(range(0, 100),5)
    random_number_list['text'] = 'Random list: '+str(numberlist)
    numberlist.sort()
    random_number_sorted_list['text'] = 'Numbers sorted: '+str(numberlist)
    
btn = Button(root, text='Generate random list', command=randomlist)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

random_number_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)
random_number_sorted_list.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()