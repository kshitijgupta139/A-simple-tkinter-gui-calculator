#!/usr/bin/env python3



from tkinter import *

expression = ""

def press(num):

	global expression

	expression = expression + str(num)

	equation.set(expression)



def equalpress():
	try:

		global expression

		total = str(eval(expression))

		equation.set(total)

		expression = ""

	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")


if __name__ == "__main__":

	gui = Tk()

	gui.configure(background="#99d6ff")

	gui.title("Your Calculator")

	gui.geometry("270x150")

	equation = StringVar()

	expression_field = Entry(gui, textvariable=equation, font="lucida 15 bold")

	expression_field.grid(columnspan=4, ipadx=70)

	equation.set('0')
	button1 = Button(gui, text=' 1 ', fg='black', bg='#66c2ff',
					command=lambda: press(1), height=1, width=7, font="lucida 15 bold")
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='#66c2ff',
					command=lambda: press(2), height=1, width=7, font="lucida 15 bold")
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='#66c2ff',
					command=lambda: press(3), height=1, width=7, font="lucida 15 bold")
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='#66c2ff',
					command=lambda: press(4), height=1, width=7, font="lucida 15 bold")
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='#66c2ff',
					command=lambda: press(5), height=1, width=7, font="lucida 15 bold")
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='#66c2ff',
					command=lambda: press(6), height=1, width=7, font="lucida 15 bold")
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='#66c2ff',
					command=lambda: press(7), height=1, width=7, font="lucida 15 bold")
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='#66c2ff',
					command=lambda: press(8), height=1, width=7, font="lucida 15 bold")
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='#66c2ff',
					command=lambda: press(9), height=1, width=7, font="lucida 15 bold")
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='#66c2ff',
					command=lambda: press(0), height=1, width=7, font="lucida 15 bold")
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='#66c2ff',
				command=lambda: press("+"), height=1, width=7, font="lucida 15 bold")
	plus.grid(row=5, column=1)

	minus = Button(gui, text=' - ', fg='black', bg='#66c2ff',
				command=lambda: press("-"), height=1, width=7, font="lucida 15 bold")
	minus.grid(row=5, column=2)

	multiply = Button(gui, text=' * ', fg='black', bg='#66c2ff',
					command=lambda: press("*"), height=1, width=7, font="lucida 15 bold")
	multiply.grid(row=6, column=0)

	divide = Button(gui, text=' / ', fg='black', bg='#66c2ff',
					command=lambda: press("/"), height=1, width=7, font="lucida 15 bold")
	divide.grid(row=6, column=1)

	equal = Button(gui, text=' = ', fg='black', bg='#66c2ff',
				command=equalpress, height=1, width=7, font="lucida 15 bold")
	equal.grid(row=6, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='#66c2ff',
				command=clear, height=1, width=7, font="lucida 15 bold")
	clear.grid(row=7, column=0)

	Decimal= Button(gui, text='.', fg='black', bg='#66c2ff',
					command=lambda: press('.'), height=1, width=7, font="lucida 15 bold")
	Decimal.grid(row=7, column=1)
	Blank= Button(gui, text='', fg='black', bg='#66c2ff',
					command=lambda: press(), height=1, width=7, font="lucida 15 bold")
	Blank.grid(row=7, column=2)
	gui.resizable(False, False)
	gui.geometry("350x290")
	gui.mainloop()
