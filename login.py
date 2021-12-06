# GUI Interface for login
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from  Grocery import *


def logindisplay():
  
  username_list = []
  password_list = []


  def getdata():
      data = open("info.txt",'r')
      rows = data.readline()

      while rows:
        data_list = rows.split()
        username_list.append(data_list[0])
        password_list.append(data_list[1])
        rows = data.readline()

  root = Tk()#login window
  root.title("Grocery List")
  root.geometry("350x300")

  Login = Label(root, text='Login', font=Font(size=20)).place(x= 150, y=1)#Login label

  Username = Label(root, text = "Username", font= Font(size=14)).place(x = 1, y = 75)#Username label
  Username_entry = Entry(root,font=Font(size=12))#entry where user enters username
  Username_entry.place(x = 95, y = 78)

  Password = Label(root, text="Password", font=Font(size=14)).place(x=1, y= 125)#Password label
  Password_entry = Entry(root, show = '*', font=Font(size=12))#entry where user enters password
  Password_entry.place(x=93, y=128)

  #function that takes user to login page
  def loggedin():
    getdata()
    usname = Username_entry.get()#obtains username entered
    passwd = Password_entry.get()#obtains password entered

    if (usname in username_list) and (password_list[username_list.index(usname)]== passwd):#checks if username and password exists and if they match
      root.withdraw()
      openList(root, usname+".txt")    
      
    else:
      messagebox.showerror("Grocery List", "Username or password entered is incorrect")


  Enter = Button(root, text = 'Enter', width = 10, command = loggedin)#button that takes user to main page
  Enter.place(x = 150, y = 160)


  #Creating function to add new user
  def newuser():

      adduser = LabelFrame(root, width = 350, height = 300)#creates frame that contains widgets and covers window
      adduser.place(x = 1, y = 1)

      CreateUser = Label(adduser, text='Create New User', font=Font(size=15)).place(x=100, y=1)

      NewUsername = Label(adduser, text="Username", font=Font(size=12)).place(x=1, y=75)#New user label
      NewUsername_entry = Entry(adduser, font=Font(size=10), width = 27)#entry where user enters username
      NewUsername_entry.place(x=95, y=78)

      NewPassword = Label(adduser, text="Password", font=Font(size=12)).place(x=1, y=125)#Password label
      NewPassword_entry = Entry(adduser, show='*', font=Font(size=10), width = 27)#entry where user enters password
      NewPassword_entry.place(x=93, y=128)

      ConfirmPassword = Label(adduser, text="Confirm Password", font=Font(size=12)).place(x=1, y=175)#Confirm password label
      ConfirmPassword_entry = Entry(adduser, show='*', font=Font(size=10))#entry where user enters previously entered password
      ConfirmPassword_entry.place(x=143, y=178)

      def back():#function that removes frame and takes user back to login window
        adduser.destroy()

      Back = Button(adduser, text='Back', width = 5, command = back).place(x=100, y = 210)#button used to implement back() function

      def add():#function that adds new user

        getdata()
        if NewPassword_entry.get() != ConfirmPassword_entry.get():#checks if entered passwords match
          messagebox.showerror("Grocery List","Passwords do not match")
        elif NewPassword_entry.get() == '':#checks if password is entered
          messagebox.showerror("Grocery List", "Please enter a password")
        else:
            if NewUsername_entry.get() in username_list:#checks if username is already entered
              messagebox.showerror("Grocery List", "Username already taken")
            else:#adds user to a file called
              write = open("info.txt", 'a' )
              print(NewUsername_entry.get() , NewPassword_entry.get(), file = write)
              messagebox.showinfo("Grocery List", "Account has been created")
              back()


      Enter = Button(adduser, text='Enter', width=10, command= add).place(x=200, y=210)
      #end of function adduser

  AddUser = Button(root, text = 'Add User', width = 15, command = newuser).place(x = 130, y=200)


  root.mainloop()