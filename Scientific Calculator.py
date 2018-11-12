from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background ="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568")

calc = Frame(root)
calc.grid()

#======================Menu and Functions=========================

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
    
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("950x568")
    
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568")
def unit():
    root.resizable(width=False, height=False)
    root.geometry("1317x568")

menubar = Menu(calc)

menubar.add_cascade(label = "Standard",font=('arial',30,'bold'), command = Standard)
menubar.add_cascade(label = "Scientific", command = Scientific)
menubar.add_cascade(label = "Unit Conversion", command = unit)

menubar.add_cascade(label = "Exit", command = iExit)


#============================= Functions ==========================

class Calc():
    
    def __init__(self):
        self.total=0
        self.current= ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
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
              self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
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

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def squared(self):
        self.result = False
        self.current = math.sqrt (float(txtDisplay.get()))
        self.display(self.current)

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
        
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)
        
    def acosh(self):
        self.result = False
        self.current = math.acosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def asinh(self):
        self.result = False
        self.current = math.asinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def expm1(self):
        self.result = False
        self.current = math.expm1(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def degrees(self):
        self.result = False
        self.current = math.degrees(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def log(self):
        self.result = False
        self.current = math.log(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def log2(self):
        self.result = False
        self.current = math.log(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def exp(self):
        self.result = False
        self.current = math.exp(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def log10(self):
        self.result = False
        self.current = math.log10(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def log1p(self):
        self.result = False
        self.current = math.log1p(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def mod(self):
        self.result = False
        self.current = math.mod(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
        
    def mins(self):
        self.result =False
        self.current = 60*(float(txtDisplay.get()))
        self.display(self.current)
        
    def smin(self):
        self.result =False
        self.current =(float(txtDisplay.get()))/60
        self.display(self.current)
    
    def ftc(self):
        self.result =False
        self.current = ((float(txtDisplay.get()))-32)*(5/9)
        self.display(self.current)
        
    def ctf(self):
        self.result =False
        self.current = (9/5)*(float(txtDisplay.get()))+32
        self.display(self.current)
        
    def ktp(self):
        self.result =False
        self.current = 2.20462*(float(txtDisplay.get()))
        self.display(self.current)
        
    def ptk(self):
        self.result =False
        self.current = (float(txtDisplay.get()))/2.20462
        self.display(self.current)
        
    def hta(self):
        self.result =False
        self.current = (float(txtDisplay.get()))*2.47105407
        self.display(self.current)
        
    def ath(self):
        self.result =False
        self.current = (float(txtDisplay.get()))/2.47105407
        self.display(self.current)
    def ftm(self):
        self.result =False
        self.current =(float(txtDisplay.get()))/3.281
        self.display(self.current)
    def mtf(self):
        self.result =False
        self.current =(float(txtDisplay.get()))*3.281
        self.display(self.current)
added_value = Calc()

#========================== Entrybox ============================

txtDisplay = Entry(calc, font=('arial',20,'bold'), bg="green", fg="#ffffff", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#========================= NumberPad ============================

numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,font=('arial',20,'bold'), bd=4,text =numberpad[i]))
        btn[i].grid(row =j, column=k, pady=1)
        btn[i]["command"]=lambda x= numberpad [i]:added_value.numberEnter(x)
        i +=1
        
#======================== Standard ==============================

#======================== Row[1] =================================

btnClear = Button(calc, text=chr(67), width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.Clear_Entry).grid(row=1, column=0, pady=1)

btnPM = Button(calc, text=chr(177), width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.mathsPM).grid(row=1, column=1, pady=1)

btnSq = Button(calc, text="√", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.squared).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

#======================== Row[2,3,4] =================================

btnSub = Button(calc, text="-", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)

btnMult = Button(calc, text="*", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text=chr(247), width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

#======================== Row[5] =================================

btnZero = Button(calc, text="0", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

btnDot = Button(calc, text=".", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

#btnPM = Button(calc, text=chr(177), width=6, height=2,font=('arial',20,'bold'), bd=4, bg="magenta3",command= added_value.mathsPM).grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text="=", width=13, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.sum_of_total).grid(row=5, column=2,columnspan=2, pady=1)

#======================== Scientific =============================
lblDisplay = Label(calc, text="Scientific Calculator", bd=30, font=('arial',30,'bold'), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)

#======================== Row[1] ==================================
btnPi = Button(calc, text="π", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command=added_value.pi).grid(row=1, column=4, pady=1)

btnCos = Button(calc, text="cos", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.cos).grid(row=1, column=5, pady=1)

btntan = Button(calc, text="tan", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.tan).grid(row=1, column=6, pady=1)

btnsin = Button(calc, text="sin", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.sin).grid(row=1, column=7, pady=1)

#======================== Row[2] ==================================

btn2Pi = Button(calc, text="2π", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.tau).grid(row=2, column=4, pady=1)

btnCosh = Button(calc, text="cosh", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.cosh).grid(row=2, column=5, pady=1)

btntanh = Button(calc, text="tanh", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.tanh).grid(row=2, column=6, pady=1)

btnsinh = Button(calc, text="sinh", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.sinh).grid(row=2, column=7, pady=1)

#======================== Row[3] ==================================

btnlog = Button(calc, text="log", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.log).grid(row=3, column=4, pady=1)

btnExp = Button(calc, text="Exp", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.exp).grid(row=3, column=5, pady=1)

btnMod = Button(calc, text="Mod", width=6, height=2,font=('arial',20,'bold'), bd=4,command= lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)

btnE = Button(calc, text="e", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.e).grid(row=3, column=7, pady=1)

#======================== Row[4] ==================================

btnlog2 = Button(calc, text="log2", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.log2).grid(row=4, column=4, pady=1)

btndeg = Button(calc, text="deg", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.degrees).grid(row=4, column=5, pady=1)

btnacosh = Button(calc, text="acosh", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.acosh).grid(row=4, column=6, pady=1)

btnasinh = Button(calc, text="asinh", width=6, height=2,font=('arial',20,'bold'), bd=4,command= added_value.asinh).grid(row=4, column=7, pady=1)

#======================== Row[5] ==================================

btnlog10 = Button(calc, text="log10", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.log10).grid(row=5, column=4, pady=1)

btnlog1p = Button(calc, text="log1p", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.log1p).grid(row=5, column=5, pady=1)

btnexpm1 = Button(calc, text="expm1", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.expm1).grid(row=5, column=6, pady=1)

btnlgamma = Button(calc, text="lgamma", width=6, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.lgamma).grid(row=5, column=7, pady=1)

#======================== Unit Conversion =============================

uniplay = Label(calc, text="Conversion", font=('arial',30,'bold'), bd=30, justify=CENTER)
uniplay.grid(row=0, column=9, columnspan=4)

btnmins = Button(calc, text="min/sec", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="green",command= added_value.mins).grid(row=1, column=9, columnspan=2, pady=1)
btnsmin = Button(calc, text="sec/min", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.smin).grid(row=2, column=9, columnspan=2, pady=1)

btnfc = Button(calc, text="far/celius", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="green",command= added_value.ftc).grid(row=3, column=9, columnspan=2, pady=1)
btncf = Button(calc, text="celius/far", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.ctf).grid(row=4, column=9, columnspan=2, pady=1)

btnkp = Button(calc, text="kg/pound", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="green",command= added_value.ktp).grid(row=5, column=9, pady=1)
btnpk = Button(calc, text="pound/kg", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.ptk).grid(row=1, column=11, columnspan=2, pady=1)

bthpa = Button(calc, text="hectare/acre", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="green",command= added_value.hta).grid(row=2, column=11, columnspan=2, pady=1)
btaph = Button(calc, text="acre/hectare", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.ath).grid(row=3, column=11, columnspan=2, pady=1)

btmy = Button(calc, text="meter/feet", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="orange",command= added_value.mtf).grid(row=5, column=11, columnspan=2, pady=1)
btym = Button(calc, text="feet/meter", width=10, height=2,font=('arial',20,'bold'), bd=4, bg="green",command= added_value.ftm).grid(row=4, column=11, columnspan=2, pady=1)

root.config(menu=menubar)
root.mainloop()
