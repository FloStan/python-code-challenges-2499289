from tkinter import *
import time
class Application(Frame):
   
    def __init__(self,master=None):
        Frame.__init__(self, master)
        Label(master,text=str(datetime.datetime.now())).grid(row=0)
 

root=Tk()
root.title('Uhrzeit')
app=Application(master=root)
app.mainloop()