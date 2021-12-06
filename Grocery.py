from tkinter import *
from tkinter import messagebox
import time
import os.path
from os import path
from threading import *


def openList(root, filename): 

    items_names = []
    items_quantity = []
    nameLabel = {}
    quantityLabel = {}

    mainlist =Toplevel(root)
    mainlist.geometry("350x300")
    mainlist.title("Grocery List")

    add_list= LabelFrame(mainlist,width=350,height=300)
    add_list.place(x=1,y=1)

    count = 1

    itemname = Label(add_list, text="Item").grid(row=0, column=0)
    quantity = Label(add_list, text="Quantity").grid(row=0, column=1)

    nameLabel[count] = Entry(add_list, width=20)
    nameLabel[count].grid(row=count, column=0)

    quantityLabel[count] = Entry(add_list, width=10)
    quantityLabel[count].grid(row=count, column=1)

    itm = ''
    quan = ''
     
    def addentry():
       nonlocal itemname; nonlocal quantity; nonlocal itm; nonlocal quan; nonlocal count
       
       itm= nameLabel[count].get()
       quan=quantityLabel[count].get()

       if itm == '' and quan == '': 
        messagebox.showerror("Grocery List" , "Enter item details before adding new item")   
       else: 
        
        if itm not in items_names:     
            items_names.append(itm)           
            items_quantity.append(quan)   

        nameLabel[count].config(state = 'disabled')
        quantityLabel[count].config(state = 'disabled')

        count += 1
        
        nameLabel[count] =Entry(add_list,width=20)
        nameLabel[count].grid(row=count,column=0)

        quantityLabel[count] = Entry(add_list,width=10)
        quantityLabel[count].grid(row=count,column=1)
        
    add_entry=Button(add_list,text="Add Entry", command = addentry).grid(row=900,column=0)

    def delete_entry():
        nonlocal count; nonlocal itemname; nonlocal quantity; nonlocal itm; nonlocal quan; nonlocal items_names; nonlocal items_quantity
        if count >1:
            nameLabel[count].destroy()
            quantityLabel[count].destroy()

            nameLabel[count-1].config(state = 'normal')
            quantityLabel[count-1].config(state = 'normal')

            if len(items_names)==count:
                items_names.pop()
                items_quantity.pop()
            
            print(items_names)
            count -= 1  
    
    photo = PhotoImage(file = r"C:\Users\zainr\Downloads\cross_button.png")
    deleteEntry = Button(add_list, image = photo, command = delete_entry, width = 20, height = 20 ).grid(row = 900, column = 1)


    def savelist():
        n = open(filename, 'a')
        r = open(filename, 'r')
        if itm == '':
            messagebox.showerror('Grocery List', "Please add items before saving")
        else:    
            for i in range(0,len(items_names)):
                 if items_names[i] not in r.read():
                    print(items_names[i], items_quantity[i], file = n)
            messagebox.showinfo("Grocery List", "List has been saved successfully")     

    save=Button(mainlist,text="Save List",command=savelist).place(x = 275, y = 20)



    def view_list():
        
        if not path.exists(filename):
            messagebox.showerror("Grocery List" , "No list created")
        else:    
            readList = open(filename, 'r+')
            
            displayList = Toplevel(mainlist)
            displayList.geometry("200x200")
            
            sb = Scrollbar(displayList)  
            sb.place(x = 185, relheight = 1.0)  

            mylist = Listbox(displayList, yscrollcommand = sb.set , width = 23)  
            
            itemname = Label(displayList, text="Item").place(x = 0, y = 0)
            quantity = Label(displayList, text="Quantity").place(x = 50, y = 0)

            data = readList.readline()
            
            mylist.place(x = 0, y = 20)
            
            items_list = []
            while data:
                items_list = data.split()
                mylist.insert(END, "{:-<12}".format(items_list[0]) + items_list[1]) 
                data = readList.readline()
                
            sb.config( command = mylist.yview ) 
            
            def clear_list():
                mylist.delete(0, 'end')
                readList.truncate(0)
            clearButton = Button(displayList, text = "Clear", command = clear_list).place(x=140, y = 30)

            displayList.mainloop()

    viewList = Button(mainlist, text = 'View List', command = view_list).place(x = 275, y = 70)

    def simul():
        Thread(target = logout).start()
        Thread(target = remind).start()


    def logout():
        
        mainlist.destroy()
        root.deiconify() 
        

    #function to remind user a week after they exit
    def remind():
        localtime = 10
        time.sleep(localtime)

        readdata = open(filename, 'r+')
        recom = readdata.readline()

        while recom:
                recom_list = recom.split()
                items_names.append(recom_list[0]) 
                recom = readdata.readline()
        

        rem = filename[:(len(filename)-4)] + " add items to your list!\n " + "recommended items include: " + ','.join(items_names)
        messagebox.showinfo("Create A List", rem)
        mainlist.destroy()
  
        
    Logout = Button(mainlist, text = "Logout", command = simul).place(x= 275,y=120)

    mainlist.mainloop()

