# first-project
Calculator

from tkinter import *

expression=" "
def press_equal(number,equation):
	global expression
	
	expression = expression + str(number)
	equation.set(expression)

def press_clear():
	global expression
	expression = " "
	equation.set(' Enter Problem ')
	
def solve_problem(equation):
	global expression
			
	try:
		total =str(eval(expression))
		equation.set(total)
		
	except:
			equation.set("Error")
			expression = " "

root = Tk()
root.geometry("300x300")
equation = StringVar()

main_frame = Frame(root, bg="blue")
main_frame.place(x=100,y=20)

title = Label(main_frame,text="MOGANDIN'S CALCULATOR", width=35,height=2,bg="yellow").pack()

screen = Entry(main_frame,font=("arial",11,"bold"), textvariable =equation, bg="pink",justify=CENTER)
screen.pack()

btn_frame=Frame(main_frame, bg="yellow").place(y=100)


btn1=Button(btn_frame,text="1", command=lambda:press_equal(1, equation),activebackground="lightblue", width=4,height=2, bg="yellow").place(y=170,x=100)

btn2=Button(btn_frame,text="2", command=lambda:press_equal(2, equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=170,x=250)


btn3=Button(btn_frame,text="3", command=lambda:press_equal(3,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=170,x=400)


btn_clear=Button(btn_frame,text="CLEAR", command=lambda: press_clear(), width=4,height=1,bg="orange").place(y=170,x=565)

btn4=Button(btn_frame,text="4", command=lambda:press_equal(4,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=270,x=100)

btn5=Button(btn_frame,text="5", command=lambda:press_equal(5,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=270,x=250)


btn6=Button(btn_frame,text="6", command=lambda:press_equal(6,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=270,x=400)

btnx=Button(btn_frame,text="x", command=lambda:press_equal("*",equation),activebackground="lightblue", width=4,height=1,bg="orange").place(y=240,x=565)

btn7=Button(btn_frame,text="7", command=lambda:press_equal(7,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=370,x=100)

btn8=Button(btn_frame,text="8", command=lambda:press_equal(8,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=370,x=250)

btn9=Button(btn_frame,text="9", command=lambda:press_equal(9,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=370,x=400)

btnplus=Button(btn_frame,text="+",command=lambda:press_equal("+",equation), bg="orange", width=4,height=1).place(y=320,x=565)

btn_comma=Button(btn_frame,text=",", command=lambda:press_equal(".",equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=470,x=100)

btn_0=Button(btn_frame,text="0", command=lambda:press_equal(0,equation),activebackground="lightblue", width=4,height=2,bg="yellow").place(y=470,x=250)

btn_egual=Button(btn_frame,text="=", command=lambda:solve_problem(equation),activebackground="lightblue", width=4,height=2,bg="red").place(y=470,x=400)

btn_div=Button(btn_frame,text="%", command=lambda:press_equal("/",equation),activebackground="lightblue", width=4,height=1,bg="orange").place(y=400,x=565)

btn_minus=Button(btn_frame,text="-", command=lambda:press_equal("-",equation),activebackground="lightblue", width=4,height=2,bg="orange").place(y=470,x=565)

root.mainloop()
