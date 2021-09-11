import random,requests,os
from tkinter import *
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import ImageTk, Image

url = 'https://www.imdb.com/chart/top'
List_main = []
def start():
    global List_main
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    movietags = soup.select ('td.titleColumn')
    List_main = movietags
def out():
    movietag0 = List_main[random.randint(1,249)]
    moviesplit = movietag0.text.split()
    moviesplit.pop(0)
    a = ' '.join(moviesplit)
    return a
def click():
    label0=Label(root,text='{}'.format(out()),bg= '#488ddb',font = ('Tahoma','11'))
    label0.pack()

root = Tk()
bg= '#000000'

root.title('Movie Suggester')
#root.geometry("480x300")
#root.configure(background = bg)
label0 = Label(root,text='Click the button to get a movie suggestion..!',font=('Ariel','15'),bg= bg,fg='orange')
label0.pack();start();
button0 = Button(root,activeforeground= 'red', activebackground='blue', width=42,height=2, text="Click me",command=click,fg='white',bg='black',font=('Helvetica','10'))
button0.pack();

root.mainloop()