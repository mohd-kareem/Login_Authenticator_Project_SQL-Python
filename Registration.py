import mysql.connector
from tkinter import *


def register_user():
    username=entry_username.get()
    password=entry_password.get()
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="kareem123",
            database="kareem",
            auth_plugin="mysql_native_password")
        cursor=db.cursor()
        q1="insert into reg_table(username,password) values(%s,%s)"
        cursor.execute(q1,(username,password))
        db.commit()
        q2="select * from reg_table"
        cursor.execute(q2)
        result=cursor.fetchall()
        if result:
            for row in result:
                print(row)
                msg_label.config(text=" Registration done......")

    except mysql.connector.Error as err:
        print(f"Error:{err}")
        msg_label.config(text=f"Error:{err}")
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()
            print("connection closed")
def login_user():
    username=entry_username_login.get()
    password=entry_password_login.get()

    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="kareem123",
            database="kareem",
            auth_plugin="mysql_native_password")
        cursor=db.cursor()
        cursor.execute("use kareem")
        q3="select * from reg_table where username=%s and password=%s"
        cursor.execute(q3,(username,password))
        result=cursor.fetchone()
        if result:
            msg_label.config(text="Login sucessful")
        else:
            msg_label.config(text="Invalid username or password")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
        msg_label.config(text=f"Error{err}")
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()
            print("Connection closed")
root=Tk()
root.title("Registration and login window")
root['background']='#87CEEB'
width=300
height=250
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

label_username=Label(root,text="username", background='red')
label_username.grid(row=0,column=0,padx=10,pady=10)
entry_username=Entry(root)
entry_username.grid(row=0,column=1,padx=10, pady=10)

label_password=Label(root, text="Password:")
label_password.grid(row=1,column=0,padx=10, pady=10)
entry_password=Entry(root, show="*")
entry_password.grid(row=1,column=1,padx=10, pady=10)

button_register=Button(root, text="Register", command=register_user,bg='#ffffff', activebackground='#00ff00')  
button_register.grid(row=2,column=0,columnspan=2,pady=10)



label_username_login=Label(root, text="Username:")

label_username_login.grid(row=3,column=0,padx=10, pady=10)

entry_username_login=Entry(root)
entry_username_login.grid(row=3,column=1,padx=10, pady=10)

label_password_login=Label(root, text="Password:")
label_password_login.grid(row=4,column=0,padx=10, pady=10)

entry_password_login=Entry(root, show="*")
entry_password_login.grid(row=4,column=1,padx=10, pady=10)

button_login=Button(root, text="Login", command=login_user)
button_login.grid(row=5,column=0,columnspan=2,pady=10)

msg_label=Label(root, text="")
msg_label.grid(row=6,column=0,columnspan=2,pady=10)

root.mainloop()