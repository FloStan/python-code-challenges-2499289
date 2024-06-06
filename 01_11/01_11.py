from tkinter import *
import time

fenster=Tk()
fenster.title('Uhrzeit')

uhr = Label(master=fenster,

            font=('Arial', 30),

            fg='blue',

            width=15)

uhr.pack()

zeit = ''

def tick():
  global zeit
  neuezeit = time.strftime('%H:%M:%S')
  if neuezeit != zeit:
    zeit=neuezeit
    uhr.config(text=zeit)
  uhr.after(1000, tick)

tick()

uhr.mainloop()