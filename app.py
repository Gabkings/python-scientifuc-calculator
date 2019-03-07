from tkinter import*
import math
import parser
import tkinter.messagebox

'''Create the name of the application'''
root = Tk()
root.title("Scientific Calculator")
root.config(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("600x560+0+0")
'''creating the frame of the calculator'''
#============================menu====================
def iExit():
    option = tkinter.messagebox.askyesno("Scientific Calculator","Confirm Exit")
    if option > 0:
        root.destroy()
        return


def Scientific():
        root.resizable(width=False,height=False)
        root.geometry("980x560+0+0")

def Standard():
        root.resizable(width=False,height=False)
        root.geometry("600x600+0+0")



calc = Frame(root)
calc.grid()

'''Button functionality'''
class Calc():
        def __init__(self):
                self.total = 0
                self.current = ""
                self.input_value = True
                self.check_sum = False
                self.op = ""
                self.result = False

        def numberEnter(self,num):
                self.result = False
                firstnum = textDisplay.get()
                secondnum = str(num)
                if self.input_value:
                        self.current = secondnum
                        self.input_value = False
                else:
                        if secondnum == ".":
                                if secondnum in firstnum:
                                        return
                        self.current = firstnum + secondnum
                self.display(self.current)
        def sum_of_total(self):
                self.result = True
                self.current = float(self.current)
                if self.check_sum == True:
                        self.valid_function()
                else:
                        self.total = float(textDisplay.get())
        def display(self, value):
                textDisplay.delete(0, END)
                textDisplay.insert(0, value)

        def valid_function(self):
                if self.op == "add":
                        self.total += self.current
                if self.op == "sub":
                        self.total -= self.current
                if self.op == "multi":
                        self.total *= self.current
                if self.op == "div":
                        self.total /= self.current
                if self.op == "mod":
                        self.total %= self.current
                self.input_value = True
                self.check_sum = False
                self.display(self.total)
        def operation(self, op):
                self.current = float(self.current)
                if self.check_sum:
                        self.valid_function()
                elif not self.result:
                        self.total = self.current
                        self.input_value = True
                self.check_sum = True
                self.op = op
                self.result = False

        def sqr(self):
                self.result = False
                self.current = float(textDisplay.get())
                self.answer = self.current * self.current
                self.display(self.answer)

        def pi(self):
                self.result = False
                self.current = math.pi
                self.display(self.current)

        def plus_minus(self):
                self.result = False
                self.current = -(float(textDisplay.get()))
                self.display(self.current)

        def tau(self):
                self.result = False
                self.current = math.tau
                self.display(self.current)

        def e(self):
                self.result = False
                self.current = math.e
                self.display(self.current)
        def cos(self):
                self.result = False
                self.current = math.cos(math.radians(float(textDisplay.get())))
                self.display(self.current)

        def sin(self):
                self.result = False
                self.current = math.sin(math.radians(float(textDisplay.get())))
                self.display(self.current)

        def tan(self):
                self.result = False
                self.current = math.tan(math.radians(float(textDisplay.get())))
                self.display(self.current)

        def cosh(self):
                self.result = False
                self.current = math.cosh(math.radians(float(textDisplay.get())))
                self.display(self.current)

        def sinh(self):
                self.result = False
                self.current = math.sinh(math.radians(float(textDisplay.get())))
                self.display(self.current)

        def tanh(self):
                self.result = False
                self.current = math.tanh(math.radians(float(textDisplay.get())))
                self.display(self.current)
        def sqrt(self):
                self.result = False
                self.current = math.sqrt(float(textDisplay.get()))
                self.display(self.current)
        def clear_entry(self):
                self.result = False
                self.current = 0
                self.display(0)
                self.input_value = True
        def clear_all_entry(self):
                self.clear_entry()
                self.total = 0
        def asinh(self):
                self.result = False
                self.current = math.asinh(float(textDisplay.get()))
                self.display(self.current)

        def acosh(self):
                self.result = False
                self.current = math.acosh(float(textDisplay.get()))
                self.display(self.current)

        def expm1(self):
                self.result = False
                self.current = math.expm1(float(textDisplay.get()))
                self.display(self.current)

        def lgamma(self):
                self.result = False
                self.current = math.lgamma(float(textDisplay.get()))
                self.display(self.current)

        def degrees(self):
                self.result = False
                self.current = math.degrees(float(textDisplay.get()))
                self.display(self.current)

        def log10(self):
                self.result = False
                self.current = math.log10(float(textDisplay.get()))
                self.display(self.current)

        def log(self):
                self.result = False
                self.current = math.log(float(textDisplay.get()))
                self.display(self.current)
        def expo(self):
                self.result = False
                self.current = math.exp(float(textDisplay.get()))
                self.display(self.current)

        def log1p(self):
                self.result = False
                self.current = math.log1p(float(textDisplay.get()))
                self.display(self.current)

        def log2(self):
                self.result = False
                self.current = math.log2(float(textDisplay.get()))
                self.display(self.current)
added_value = Calc()
menubar = Menu(calc)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label = "Standard", command=Standard)
filemenu.add_command(label = "Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command=iExit)
'''create the cut,edit and copy options '''
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")
'''creating the help menu options'''
helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="View Help", menu=helpmenu)
helpmenu.add_command(label = "Help")
root.configure(menu = menubar)

#========================widgets=======================
textDisplay = Entry(calc, font=("arial",20,"bold"),bg="powder blue",bd=10,width=33,justify=RIGHT)
textDisplay.grid(row=0, column=0,columnspan=4,pady=1)
textDisplay.insert(0,"0")
labelTitle = Label(calc,font=("arial",20,"bold") , text="Scientific Calculator", bg="powder blue",bd=5,width=29,
justify=CENTER).grid(row=0, column=4,columnspan=4,pady=1)

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
        for k in range(3):
                btn.append(Button(calc, width=6,height=2, bg="powder blue", font=("arial",20,"bold"),bd=2,text=numberpad[i]))
                btn[i].grid(row=j,column=k,pady=1)
                btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
                i += 1



btnClear = Button(calc, font=("arial",20,"bold"), text=chr(67), width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.clear_entry ).grid(row=1,column=0,pady=1)
btnAllClear = Button(calc, font=("arial",20,"bold"), text=chr(67) + chr(69), width=6, height=2,bd=2,
 bg="powder blue", command= added_value.clear_all_entry ).grid(row=1,column=1,pady=1)
btnSqrt = Button(calc, font=("arial",20,"bold"), text="sqrt", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.sqrt  ).grid(row=1,column=2,pady=1)
btnTimes = Button(calc, font=("arial",20,"bold"), text="*", width=6, height=2,bd=2,
 bg="powder blue", command = lambda : added_value.operation("multi") ).grid(row=1,column=3,pady=1)
btnDivide = Button(calc, font=("arial",20,"bold"), text="/", width=6, height=2,bd=2,
 bg="powder blue" , command = lambda : added_value.operation("div") ).grid(row=2,column=3,pady=1)

btnAdd = Button(calc, font=("arial",20,"bold"), text="+", width=6, height=2,bd=2,
 bg="powder blue" , command = lambda : added_value.operation("add") ).grid(row=3,column=3,pady=1)
btnMinus = Button(calc, font=("arial",20,"bold"), text="-", width=6, height=2,bd=2,
 bg="powder blue" , command = lambda : added_value.operation("sub") ).grid(row=3,column=3,pady=1)

btnSqr = Button(calc, font=("arial",20,"bold"), text="sqr", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.sqr  ).grid(row=4,column=3,pady=1)

btnZero = Button(calc, font=("arial",20,"bold"), text="0", width=6, height=2,bd=2,
 bg="powder blue" ,command = lambda : added_value.numberEnter(0)).grid(row=5,column=0,pady=1)
btnDot = Button(calc, font=("arial",20,"bold"), text=".", width=6, height=2,bd=2,
 bg="powder blue", command = lambda : added_value.operation(".") ).grid(row=5,column=1,pady=1)

btnALert = Button(calc, font=("arial",20,"bold"), text=chr(177), width=6, height=2,bd=2,
 bg="powder blue" , command=added_value.plus_minus ).grid(row=5,column=2,pady=1)
btnEquals = Button(calc, font=("arial",20,"bold"), text="=", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.sum_of_total ).grid(row=5,column=3,pady=1)

#====================scientific calculator =============
btnPi = Button(calc, font=("arial",20,"bold"), text="pi", width=6, height=2,bd=2,
 bg="powder blue" , command = added_value.pi ).grid(row=1,column=4,pady=1)
btnCos = Button(calc, font=("arial",20,"bold"), text="cos", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.cos ).grid(row=1,column=5,pady=1)
btnTan = Button(calc, font=("arial",20,"bold"), text="tan", width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.tan ).grid(row=1,column=6,pady=1)
btnSine = Button(calc, font=("arial",20,"bold"), text="sin", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.sin ).grid(row=1,column=7,pady=1)
#========================================================
btn2Pi = Button(calc, font=("arial",20,"bold"), text="2pi", width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.tau ).grid(row=2,column=4,pady=1)
btnCosh = Button(calc, font=("arial",20,"bold"), text="cosh", width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.cosh ).grid(row=2,column=5,pady=1)
btnTanh = Button(calc, font=("arial",20,"bold"), text="tanh", width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.tanh ).grid(row=2,column=6,pady=1)
btnSinh = Button(calc, font=("arial",20,"bold"), text="sinh", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.sinh ).grid(row=2,column=7,pady=1)
#=========================================================
btnLog = Button(calc, font=("arial",20,"bold"), text="log", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.log ).grid(row=3,column=4,pady=1)
btnExpo = Button(calc, font=("arial",20,"bold"), text="Exp", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.expo ).grid(row=3,column=5,pady=1)
btnMod = Button(calc, font=("arial",20,"bold"), text="Mod", width=6, height=2,bd=2,
 bg="powder blue" ).grid(row=3,column=6,pady=1)
btnE = Button(calc, font=("arial",20,"bold"), text="e", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.e ).grid(row=3,column=7,pady=1)
#==========================================================
btnLog2 = Button(calc, font=("arial",20,"bold"), text="log2", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.log2 ).grid(row=4,column=4,pady=1)
btnDeg = Button(calc, font=("arial",20,"bold"), text="Deg", width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.degrees ).grid(row=4,column=5,pady=1)
btnAcos = Button(calc, font=("arial",20,"bold"), text="acosh", width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.acosh ).grid(row=4,column=6,pady=1)
btnAsin = Button(calc, font=("arial",20,"bold"), text="asin", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.asinh ).grid(row=4,column=7,pady=1)

#===========================================================
btnLog10 = Button(calc, font=("arial",20,"bold"), text="log10", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.log10 ).grid(row=5,column=4,pady=1)
btnlog1p = Button(calc, font=("arial",20,"bold"), text="log1p", width=6, height=2,bd=2,
 bg="powder blue" , command= added_value.log1p).grid(row=5,column=5,pady=1)
btnExpm1 = Button(calc, font=("arial",20,"bold"), text="expm1", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.expm1 ).grid(row=5,column=6,pady=1)
btnlgamma = Button(calc, font=("arial",20,"bold"), text="lgamma", width=6, height=2,bd=2,
 bg="powder blue", command= added_value.lgamma ).grid(row=5,column=7,pady=1)
root.mainloop()