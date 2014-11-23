import random


def WhereToEat(n):
    if n < 20:
        print 'Eat Chipotle!!'
        return 
    elif n < 40 and n > 21:
        print 'Eat Noodles!!'
        return 
    elif n < 60 and n > 41:
        print 'Eat Pizza!!'
        return 
    elif n < 80 and n > 61:
        print 'Eat Jimmy Johns!!'
        return
    elif n < 100 and n > 81:
        print 'Eat Culvers!!!'
        return
    
intTest = random.randint(0,100)


WhereToEat(intTest)




# ''' GUI Imports '''
# from Tkinter import *
# 
# 
# 
# uGUI = Tk()
# userNameInput = StringVar()
# 
# uGUI.geometry('400x400')
# uGUI.title('Create User Profile')
# 
# uLabel = Label(uGUI, text = 'Please Input Your Name: ').pack()
# 
# uName = Entry(uGUI, textvariable=userNameInput).pack()
# 
# uGUI.mainloop()