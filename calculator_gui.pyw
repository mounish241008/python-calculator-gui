import tkinter as tk
root = tk.Tk()
root.title("CALCULATOR.v2")
root.geometry("300x250")
display = tk.Entry(root,width=30,font=("Arial",12))
display.grid(row=0,column=0,columnspan=5,padx=15,pady=15)
root.resizable(False,False)
def add_1() :
    display.insert(tk.END ,"1")
button_1 = tk.Button(root, text= "1",command= add_1,width=5,height=2)
button_1.grid(row=1,column=1,padx=2,pady=2)
def add_2() :
    display.insert(tk.END,"2",)
button_2 = tk.Button(root, text="2",command= add_2,width=5,height=2)
button_2.grid(row=1,column=2,padx=2,pady=2)
def add_3() :
    display.insert(tk.END ,"3")
button_3 = tk.Button(root,text= "3",command=add_3,width=5,height=2)
button_3.grid(row=1,column=3,padx=2,pady=2)
def add_4() :
    display.insert(tk.END,"4")
button_4 = tk.Button(root,text= "4",command= add_4,width=5,height=2)
button_4.grid(row=2,column=1,padx=2,pady=2)
def add_5() :
    display.insert(tk.END,"5")
button_5 = tk.Button(root,text= "5",command= add_5,width=5,height=2)
button_5.grid(row=2,column=2,padx=2,pady=2)
def add_6() :
    display.insert(tk.END,"6")
button_6 = tk.Button(root,text= "6",command= add_6,width=5,height=2)
button_6.grid(row=2,column=3,padx=2,pady=2)
def add_7() :
    display.insert(tk.END,"7")
button_7 = tk.Button(root,text= "7",command= add_7,width=5,height=2)
button_7.grid(row=3,column=1,padx=2,pady=2)
def add_8() :
    display.insert(tk.END,"8")
button_8 = tk.Button(root,text= "8",command= add_8,width=5,height=2)
button_8.grid(row=3,column=2,padx=2,pady=2)
def add_9():
    display.insert(tk.END,"9")
button_9 = tk.Button(root,text= "9",command= add_9,width=5,height=2)
button_9.grid(row=3,column=3,padx=2,pady=2)
def add_0():
    display.insert(tk.END,"0")
button_0 = tk.Button(root,text= "0",command= add_0,width=5,height=2)
button_0.grid(row=4,column=2,padx=2,pady=2)
def add_plus() :
    display.insert(tk.END,"+")
plus_button = tk.Button(root,text= "+",command= add_plus,width=5,height=2)
plus_button.grid(row=1,column=4,padx=2,pady=2)
def add_minus():
    display.insert(tk.END,"-")
minus_button = tk.Button(root,text= "-",command= add_minus,width=5,height=2)
minus_button.grid(row=2,column=4,padx=2,pady=2)
def add_into():
    display.insert(tk.END,"*")
into_button = tk.Button(root,text="*",command=add_into,width=5,height=2)
into_button.grid(row=3,column=4,padx=2,pady=2)
def add_divide() :
    display.insert(tk.END,"/")
divide_button = tk.Button(root,text="/",command=add_divide,width=5,height=2)
divide_button.grid(row=4,column=4,padx=2,pady=2 )
def clear() :
    display.delete(0,tk.END)
clear_button = tk.Button(root,text="C",command=clear,width=5,height=2)
clear_button.grid(row=1,column=0,padx=2,pady=2)
def calculate() :
    result = eval(display.get())
    display.delete(0,tk.END)
    display.insert(tk.END,result)
equal_button = tk.Button(root,text="=",command= calculate,width=5,height=2)
equal_button.grid(row=4,column=3,padx=2,pady=2)
def del_num() :
    result = display.get()
    new = result[:-1]
    display.delete(0,tk.END)
    display.insert(0,new)
delete_button = tk.Button(root,text="del",command= del_num,width=5,height=2)
delete_button.grid(row=4,column=1,padx=2,pady=2)
root.mainloop()