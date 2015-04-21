__author__ = 'Drew Masters'

from Tkinter import *
import tkMessageBox
import serial
import time

top = Tk()

def ait():
    #reads values from GUI
    N=E1.get() #number of variables
    M=E2.get() #number of clauses
    k=E3.get() #k variable (number of variables per clause)
    equation=E4.get() #equation being processed passed to arduino as string

    arduino=serial.Serial(15, 115200, timeout=.1) #starts serial connection
    time.sleep(1)

    #writes variables to arduino
    arduino.write(N)
    arduino.write(M)
    arduino.write(k)
    arduino.write(equation)

    line=[]
    count = 0
    while True:
        #read one line a a time until finished
        for c in arduino.read():
            line.append(c)
            if c=='\n':
                line.append(c)
                print(line)
                count+=1
                #if line is unsuccessful print that to user
                if line == 'unsuccessful':
                    tkMessageBox.FunctionName("Result", line)
                    break
                #if line is successful continue reading until all variables are read
                if count == (N+1):
                    tkMessageBox.FunctionName("Result", line)
                    break

def close_window():
    top.destroy()

L1 = Label(top, text="Number of Variables(N)")
E1 = Entry(top, bd=5)
L1.pack()
E1.pack()

L2 = Label(top, text="Number of Clauses(M)")
E2 = Entry(top, bd=5)
L2.pack()
E2.pack()

L3 = Label(top, text="k")
E3 = Entry(top, bd=5)
L3.pack()
E3.pack()

L4 = Label(top, text="Equation")
E4 = Entry(top, bd=5)
L4.pack()
E4.pack()

B1 = Button(top, text="Submit", command=ait)
B1.pack()

B2 = Button(top, text="Close", command=close_window)
B2.pack()

top.mainloop()