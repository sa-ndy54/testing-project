from tkinter import*


root = Tk()
root.geometry("1366x768")
root.title("Login Page")
root.config(bg="Cadet Blue")

photo2 = PhotoImage(file='D://1.gif')
photo = Label(root,image=photo2,bg="cadet blue")
photo.pack()


texta = Label(root, text="Viva La India", font=('Times New Roman', 42, 'bold','underline'),bg="cadet blue",fg="Black")
texta.place(x=0, y=0)

textb = Label(root, text="Please Login:", font=('Helvetica', 28, 'bold'), fg="Black",bg="cadet blue")
textb.place(x=10, y=250)

textc = Label(root, text="User Name", font=('Helvetica', 12, 'bold'), fg="Black",bg="cadet blue")
textc.place(x=270, y=320)

textd = Label(root, text="Password", font=('Helvetica', 12, 'bold'), fg="Black",bg="cadet blue")
textd.place(x=270, y=360)

entry1 = Entry(root, font=12)
entry1.place(x=400, y=320)

entry2 = Entry(root, font=12, show="*")
entry2.place(x=400, y=360)

button2 = Button(root,text = "cancel" )
button2.place(x=270, y=440)


texte = Label(root, text="Copyright Sandy Scorpion Sting @ 2018", font=('Arial', 9, 'bold'), fg="Black", bg="cadet blue")
texte.place(x=270, y=400)

root.mainloop()
