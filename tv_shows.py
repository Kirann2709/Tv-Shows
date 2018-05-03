from tkinter import *
from tkinter import messagebox
import os
f=open("database_shows",'a+')
root = Tk()
root.configure(background='light blue')
ijklm=-1

def add():
    global ijklm
    num_lines = 0
    with open("database_shows", 'r') as f10:
        for line in f10:
            num_lines += 1
    ijklm=num_lines-1
    e1= name.get()
    e2=dur.get()
    e3=num.get()
    e4=category.get()
    e5=rating.get()
    if (e1=="" or e2=="" or e3=="" or e4=="" or e5==""):
        error()
    else:
        f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
        name.delete(0, END)
        dur.delete(0, END)
        num.delete(0, END)
        category.delete(0, END)
        rating.delete(0, END)

def update():
    e1 = name.get()
    e2 = dur.get()
    e3 = num.get()
    e4 = category.get()
    e5 = rating.get()
    with open(r"database_shows") as f1, open(r"database_shows1", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4}'.format(str(e1), e2, e3, str(e4), e5))
    os.remove(r"database_shows")
    os.rename(r"database_shows1", r"database_shows")


def search():
    i=0
    e11 = name.get()
    with open(r"database_shows") as working:
        for line in working:
            i=i+1
            if str(e11) in line:
                break
        try:
            jkl = list(line.split(" "))
            name.delete(0, END)
            dur.delete(0, END)
            num.delete(0, END)
            category.delete(0, END)
            rating.delete(0, END)
            name.insert(0, str(jkl[0]))
            dur.insert(0, str(jkl[1]))
            num.insert(0, str(jkl[2]))
            category.insert(0, str(jkl[3]))
            rating.insert(0, str(jkl[4]))
        except:
            messagebox.showinfo("Title", "Error!")
    working.close()

def delete():
    e1=name.get()
    with open(r"database_shows") as f, open(r"database_shows1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(r"database_shows")
    os.rename(r"database_shows1", r"database_shows")
    f.close()
    working.close()
    name.delete(0, END)
    dur.delete(0, END)
    num.delete(0, END)
    category.delete(0, END)
    rating.delete(0, END)

def clear():
    name.delete(0, END)
    dur.delete(0, END)
    num.delete(0, END)
    category.delete(0, END)
    rating.delete(0, END)

def error():
    name.delete(0, END)
    dur.delete(0, END)
    num.delete(0, END)
    category.delete(0, END)
    rating.delete(0, END)
    messagebox.showinfo("Title", "Error! Please fill all the fields.")

def firstentry():
    global ijklm
    ijklm=0
    f.seek(ijklm)
    c=f.readline()
    jkl=list(c.split(" "))
    name.delete(0, END)
    dur.delete(0, END)
    num.delete(0, END)
    category.delete(0, END)
    rating.delete(0, END)
    name.insert(0,str(jkl[0]))
    dur.insert(0,str(jkl[1]))
    num.insert(0,str(jkl[2]))
    category.insert(0,str(jkl[3]))
    rating.insert(0,str(jkl[4]))

def nextentry():
    global ijklm
    ijklm = ijklm + 1
    f.seek(ijklm)
    try:
        c=f.readlines()
        xyz = c[ijklm]
        jkl = list(xyz.split(" "))
        name.delete(0, END)
        dur.delete(0, END)
        num.delete(0, END)
        category.delete(0, END)
        rating.delete(0, END)
        name.insert(0, str(jkl[0]))
        dur.insert(0, str(jkl[1]))
        num.insert(0, str(jkl[2]))
        category.insert(0, str(jkl[3]))
        rating.insert(0, str(jkl[4]))
    except:
        messagebox.showinfo("Title", "No more records present!")

def previousentry():
        global ijklm
        ijklm=ijklm-1
        f.seek(ijklm)
        try:
            z = f.readlines()
            xyz=z[ijklm]
            jkl = list(xyz.split(" "))
            name.delete(0, END)
            dur.delete(0, END)
            num.delete(0, END)
            category.delete(0, END)
            rating.delete(0, END)

            name.insert(0, str(jkl[0]))
            dur.insert(0, str(jkl[1]))
            num.insert(0, str(jkl[2]))
            category.insert(0, str(jkl[3]))
            rating.insert(0, str(jkl[4]))
        except:
            messagebox.showinfo("Title", "No more records present!")


def lastentry():
    global ijklm
    f4=open("database_shows",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_shows", 'r') as f8:
        for line in f8:
            num_lines += 1
    ijklm=num_lines-1
    print(last_line)
    try:
        jkl = list(last_line.split(" "))
        name.delete(0, END)
        dur.delete(0, END)
        num.delete(0, END)
        category.delete(0, END)
        rating.delete(0, END)

        name.insert(0, str(jkl[0]))
        dur.insert(0, str(jkl[1]))
        num.insert(0, str(jkl[2]))
        category.insert(0, str(jkl[3]))
        rating.insert(0, str(jkl[4]))
    except:
        messagebox.showinfo("Title", "No more records present!")


l0= Label(root,text="TV SHOWS DATABASE", font=("Helvetica", 25))
l1=Label(root,text="Name:", font=("Helvetica", 12))
name=Entry(root , font=("Helvetica", 12))
l2=Label(root, text="Duration:", font=("Helvetica", 12))
dur= Entry(root, font=("Helvetica", 12))
l3=Label(root, text="No. of seasons:", font=("Helvetica", 12))
num= Entry(root, font=("Helvetica", 12))
l4=Label(root, text="Category:", font=("Helvetica", 12))
category= Entry(root, font=("Helvetica", 12))
l5=Label(root, text="Rating:", font=("Helvetica", 12))
rating= Entry(root, font=("Helvetica", 12))
badd= Button(root, text="Add", width=10, bg = 'black', fg = 'white', font=("Helvetica", 12), command=add)
bdelete= Button(root, text="Delete", bg = 'black', fg = 'white', width =10, font=("Helvetica", 12), command=delete)
bfirst= Button(root, text="|<" , bg = 'grey', fg = 'white', width =10, font=("Helvetica", 12), command=firstentry)
bnext= Button(root, text=">" , bg = 'grey', fg = 'white', width =10, font=("Helvetica", 12), command=nextentry)
bprevious= Button(root, text="<", bg = 'grey', fg = 'white', width =10, font=("Helvetica", 12), command=previousentry)
blast= Button(root, text=">|", bg = 'grey', fg = 'white', width =10, font=("Helvetica", 12), command=lastentry)
bupdate= Button(root, text="Update", bg = 'black', fg = 'white', width =10, font=("Helvetica", 12), command=update)
bsearch= Button(root, text="Search", bg = 'black', fg = 'white', width =10, font=("Helvetica", 12), command=search)
bclear= Button(root, text="Clear", bg = 'black', fg = 'white', width=10, font=("Helvetica", 12), command=clear)
l0.grid(columnspan=5)
l1.grid(row=6,column=1, sticky=W, padx=2, pady=5)
l2.grid(row=7,column=1, sticky=W, padx=2, pady=5)
l3.grid(row=8,column=1, sticky=W, padx=2, pady=8)
l4.grid(row=9,column=1, sticky=W, padx=2, pady=8)
l5.grid(row=10,column=1, sticky=W, padx=4, pady=10)
name.grid(row=6,column=2, padx=2, pady=5)
dur.grid(row=7,column=2, padx=2, pady=5)
num.grid(row=8,column=2, padx=2, pady=5)
category.grid(row=9,column=2, padx=2, pady=5)
rating.grid(row=10,column=2, padx=2, pady=5)
badd.grid(row=12,column=0, padx=2, pady=5)
bdelete.grid(row=12,column=1, padx=2, pady=5)
bupdate.grid(row=12,column=2, padx=2, pady=5)
bsearch.grid(row=12,column=3, padx=2, pady=5)
bfirst.grid(row=13,column=0, padx=2, pady=5)
bprevious.grid(row=13,column=1, padx=2, pady=5)
bnext.grid(row=13,column=2, padx=2, pady=5)
blast.grid(row=13,column=3, padx=2, pady=5)
bclear.grid(row=14,column=1, padx=2, pady=5, columnspan = 2)
root.mainloop()
