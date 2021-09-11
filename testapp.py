import random,requests,os
from tkinter import *
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import ImageTk, Image

url = 'https://www.imdb.com/chart/top'
List_main = []
img = ''
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
def imgf():
    global img
    img_url = "https://cdn.radiofrance.fr/s3/cruiser-production/2020/09/e60f0dcf-46ad-4289-aa05-61230e7c3926/838_gettyimages-566435049.webp"
    response = requests.get(img_url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))


root = Tk()
root.minsize(300, 200);root.maxsize(500, 400);
root.title('Movie Suggester')

##background##
imgf()
backpanel = Label(root, image=img)
#backpanel.pack(side="bottom", fill="both")
##background##
label0 = Label(root,text='Click the button to get a movie suggestion..!',font=('Ariel','15'),fg='orange')
label0.pack();start();
button0 = Button(root,activeforeground= 'red', activebackground='blue', width=42,height=2, text="Click me",command=click,fg='white',bg='black',font=('Helvetica','10'))
button0.pack();

root.mainloop()