__author__ = 'Drew Masters'

from Tkinter import *
import tkMessageBox
import serial
import time

top = Tk()

def ait():
    N=E1.get()
    M=E2.get()
    k=E3.get()
    equation=E4.get()
    print(N+"\n")
    print(M+"\n")
    print(k+"\n")
    print(equation+"\n")
  #  input=N+"n"+M+"n"+k+"n"+equation
  #  print input

    arduino=serial.Serial(15, 115200, timeout=.1)
    time.sleep(1)

    arduino.write(N)
    print arduino.readline()[:-2]
    print arduino.readline()[:-2]
    print "printed N\n"

    arduino.write(M)
    print arduino.readline()[:-2]
    print arduino.readline()[:-2]
    print "printed M\n"

    arduino.write(k)
    print arduino.readline()[:-2]
    print arduino.readline()[:-2]
    print "printed k\n"

    arduino.write(equation)
    print arduino.readline()[:-2]
    print arduino.readline()[:-2]
    print "printed equation\n"

    line=[]
    count = 0
    while True:
        for c in arduino.read():
            line.append(c)
            if c=='\n':
                line.append(c)
                print(line)
                count+=1
                if line == 'unsuccessful':
                    tkMessageBox.FunctionName("Result", line)
                    break
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