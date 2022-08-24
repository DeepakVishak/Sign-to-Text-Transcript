from tkinter import *
class Application():

    def __init__(self, master=None):
        '''Create a 'master' frame of 1 row x 1 column'''
        self.master = master
        button = Button(self.master, text = 'Button', command = self.test)
        button.pack()
        #This Binding works
        self.master.bind('<Return>', self.test)
        #this Binding produces Error
        self.master.bind('<Control_L><o>', self.test)


    def test(self, event = None):
        print("Succesful Event")

root = Tk()
app = Application(master=root)
