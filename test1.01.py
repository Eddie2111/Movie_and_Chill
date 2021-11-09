from random         import randint
from requests       import get 
from tkinter.ttk    import Progressbar
from tkinter        import Label, Button, Tk, ttk, Frame
from bs4            import BeautifulSoup
from io             import BytesIO
from PIL            import ImageTk, Image
import time

pro         = ttk.Progressbar
w           = Tk()

url         = 'https://www.imdb.com/chart/top'
List_main   = []
img         = ''

def start():
    global List_main
    if len(List_main)==0:
        response    = get(url)
        html        = response.text
        soup        = BeautifulSoup(html,'html.parser')
        movietags   = soup.select ('td.titleColumn')
        List_main   = movietags
def out():
    movietag0       = List_main[randint(1,249)]
    moviesplit      = movietag0.text.split()
    moviesplit.pop(0)
    a               = ' '.join(moviesplit)
    return a
def click():
    label0          = Label(
                            root,
                            text    = '{}'.format(out()),
                            bg      = '#488ddb',
                            font    = ('Tahoma','11')
                           )
    label0.pack()

width_of_window         = 427
height_of_window        = 250
screen_width            = w.winfo_screenwidth()
screen_height           = w.winfo_screenheight()
x_coordinate            = (screen_width/2)-(width_of_window/2)
y_coordinate            = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)

s           = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#07fa18')
progress    = pro(
                    w,
                    style   = "red.Horizontal.TProgressbar",
                    orient  = 'horizontal',
                    length  = 500,
                    mode    = 'determinate',
                )

#############  progressbar  ###############
def new_win():
    return ''

def bar():
    l4      =Label(
                    w,
                    text    = 'Loading...',
                    fg      = 'white',
                    bg      = a
                )
    lst4    = ('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    r       = 0
    
    for i in range(100):
        progress['value']   = r
        w.update_idletasks()
        if len(List_main)==0:
            start()
        if len(List_main)!=0:pass;
        time.sleep(0.01)
        r   = r+1
    w.destroy()
        
progress.place(x=-10,y=235)



a           = '#0a52f0'
Frame(
    w,
    width   = 427,
    height  = 241,
    bg      = a
                    ).place(x=0,y=0) 

b1          = Button(
                        w,
                        width   = 10,
                        height  = 1,    
                        text    = 'Get Started',
                        command = bar,
                        border  = 0,
                        fg      = a,    
                        bg      = 'white'
                    )

b1.place(x=170,y=200)

l1      =Label(w,text='Movie',fg='white',bg=a)
lst1    =('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)
l2      =Label(w,text='Suggester',fg='white',bg=a)
lst2    =('Calibri (Body)',18,'bold')
l2.config(font=lst2)
l2.place(x=123,y=80)

l3      =Label(w,text='',fg='white',bg=a)
lst3    =('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)
w.mainloop()

root    = Tk()
root.minsize(300, 200);root.maxsize(500, 400);
root.title('Movie Suggester')
root.configure(bg='Grey')

Alabel0 = Label(
                root,
                text    = 'Click the button to get a movie suggestion..!',
                font    = ('Ariel','15'),
                fg      = 'orange',
                bg      = 'Grey'
                )

Alabel0.pack();
Abutton0 = Button(
                root,
                activeforeground    = 'red', 
                activebackground    = 'blue', 
                width               = 42,
                height              = 2, 
                text                = "Click me",
                command             = click,
                fg                  = 'white',
                bg                  = 'black',
                font                =('Helvetica','10')
                )

Abutton0.pack();
root.mainloop()
new_win()
