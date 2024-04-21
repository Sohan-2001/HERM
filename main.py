from tkinter import *
def splash():
    new=Tk()
    new.state('zoomed')
    new.config(bg='black')
    new.title('Welcome From @MASK')
    try:
        import getpass
        user=getpass.getuser()          
        label=Label(text='Welcome\n\n'+user,
                    bg='black',
                    fg='white',
                    font=('Arial',20))
        label.place(relx=0.5,rely=0.5,anchor=CENTER)
    except:
        pass
    new.after(1000,lambda:new.destroy())
    new.mainloop()
splash()

ws=Tk()

ws.state('zoomed')
ws.config(bg='black')
ws.title('Human Eye Rest Management (HERM)')

# Help
def need_help():
    import webbrowser
    url="https://wa.me/6295400770"
    webbrowser.open(url)

# Label
Heading=Label(ws,
              text='H-U-M-A-N   E-Y-E   N-E-E-D-S   R-E-S-T',
              bg='black',
              fg='white',
              font=('Serif',20))
Heading.place(relx=0.5,rely=0.025,anchor=CENTER)

# Menu
menubar=Menu(ws)
help=Menu(menubar,tearoff=0,background='lightyellow',activebackground='darkred')
menubar.add_cascade(label='Help',menu=help)
help.add_command(label='Ask Help',command=need_help)
ws.config(menu=menubar)

import time

def rest_time():
    new=Tk()
    new.state('zoomed')
    new.config(bg='dark green')
    new.title('Rest Screen')
    destr = Button(new, text = 'Exit!', bd = '2', command = new.destroy)
    destr.place(relx=0.1,rely=0.1,anchor='nw')
    try:
        import getpass
        user=getpass.getuser()          
        label=Label(new,
                    text='5 Minute Rest For Your Eyes\n\nClose Your Eyes For 1 Minute\n\nLook At Infinity For 1 Minute\n\nTry Looking At Green For 1 Minute\n\nRotate Your Shoulder\n\nDrink Water If Requirred',
                    bg='dark green',
                    fg='white',
                    font=('Arial',20))
        label.place(relx=0.5,rely=0.5,anchor=CENTER)
    except:
        pass
    new.after(1000,lambda:new.destroy())
    new.mainloop()

def dark_for_five():
    label=Label(ws,
                    text='Function Started',
                    bg='black',
                    fg='white',
                    font=('Arial',20))
    label.place(relx=0.5,rely=0.6,anchor=CENTER)
    i=1
    while i<=3:
        time.sleep(0.2)
        rest_time()
        i+=1
        

onOff = Button(ws, text = 'Turn On', bd = '2', command = dark_for_five)
onOff.place(relx=0.5,rely=0.5,anchor=CENTER) 



ws.mainloop()
