from tkinter import *

root=Tk()
root.title("Simple calculator")
root.geometry('383x375')
root.resizable(0,0)
e = Entry(root,width=30,borderwidth=5,font='bold')
e.grid(row=0, column = 0, columnspan=4,padx='20',pady='10')

def button_clk(number):
    current=e.get()
    e.delete(0, END)                                        #to delete the prev value
    e.insert(END,current+str(number))                    # to print numbers one after other

def clear():
    e.delete(0,END)

def btn_equal():
    
    expression = e.get()
    result = eval(expression)
    e.delete(0, END)
    e.insert(END, result)



button_0=Button(root,text='0',padx='86',pady='20',command=lambda: button_clk(0),bg='peach puff')
button_1=Button(root,text='1',padx='40',pady='20',command=lambda: button_clk(1),bg='peach puff')
button_2=Button(root,text='2',padx='40',pady='20',command=lambda: button_clk(2),bg='peach puff')
button_3=Button(root,text='3',padx='40',pady='20',command=lambda: button_clk(3),bg='peach puff')
button_4=Button(root,text='4',padx='40',pady='20',command=lambda: button_clk(4),bg='peach puff')
button_5=Button(root,text='5',padx='40',pady='20',command=lambda: button_clk(5),bg='peach puff')
button_6=Button(root,text='6',padx='40',pady='20',command=lambda: button_clk(6),bg='peach puff')
button_7=Button(root,text='7',padx='40',pady='20',command=lambda: button_clk(7),bg='peach puff')
button_8=Button(root,text='8',padx='40',pady='20',command=lambda: button_clk(8),bg='peach puff')
button_9=Button(root,text='9',padx='40',pady='20',command=lambda: button_clk(9),bg='peach puff')
button_add=Button(root,text="+",padx='40',pady='20',command=lambda: button_clk('+'),bg='beige')
button_sub=Button(root,text='-',padx='40',pady='20',command=lambda: button_clk('-'),bg='beige')
button_div=Button(root,text='/',padx='40',pady='20',command=lambda: button_clk('/'),bg='beige')
button_mul=Button(root,text='*',padx='40',pady='20',command=lambda: button_clk('*'),bg='beige')
button_dec=Button(root,text='.',padx='40',pady='20',command=lambda: button_clk('.'),bg='beige')
button_clear=Button(root,text='CLC',padx='33',pady='53',command=clear,bg='ivory')
button_eq=Button(root,text="=",padx='86',pady='20',command=btn_equal,bg='ivory')

button_1.grid(row=1 ,column=0 )
button_2.grid(row=1 ,column=1)
button_3.grid(row=1 ,column=2)

button_4.grid(row=2 ,column=0 )
button_5.grid(row=2 ,column=1 )
button_6.grid(row=2 ,column=2 )

button_7.grid(row=3 ,column=0 )
button_8.grid(row=3 ,column=1 )
button_9.grid(row=3 ,column=2 )

button_0.grid(row=4 ,column=0,columnspan=2 )

button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)

button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_dec.grid(row=5,column=3)

button_eq.grid(row=5,column=0,columnspan=2)
button_clear.grid(row=4,column=2,rowspan=2)




root.mainloop()
