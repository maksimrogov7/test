from tkinter import *
from tkinter import messagebox
def abc():
    
    a['text']= str(int(a['text'])+1)
    if int(a['text'])%10 == 0:
        messagebox.showerror('молодец', 'ты нажал еще 10 раз')

root = Tk()
a = Label(text = '0')
a.pack()
b = Button(bg='cyan', text='Нажми', command =abc)
b.pack()

root.resizable(False, False)
root.title('Rogov Maxim')
root.geometry('200x100')
root.mainloop()
