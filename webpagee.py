
from tkinter import*
from tkinter import messagebox
import MySQLdb as sql
def connection(user,passw):
    host='localhost'
    user='root'
    pw='vijay123'
    port=3306
    db='tutorial'
    conn=mysql.connect(host=host,user=user,password=pw,port=port,db=db)
    query="select id from login where username=%s and password=%s"
    vals=(user,passw)
    cur=conn.cursor()
    cur.execute(query,vals)
    result=cur.fetchall()
    conn.close()
    return result
def check():
    u_name=un.get()
    pass_word=pw.get()
    data=connection(u_name,pass_word)
    if len(data>0):
                    messagebox.showinfo(title="hello root",message=" welcome..your login page")
    else:
                    messagebox.showinfo(title="hello user",message="please enter correct credential")
                    

root=Tk()
un=StringVar()
pw=StringVar()
root.geometry("500x250")
root.title("sastra web page")
t=Label(root, text = "login Form",font=('arial',14),bd=15)
t.pack()
form=Frame(root)
form.pack(side=TOP,fill=X)
nameL=Label(form,text="UserName:",font=('arial',14),bd=15)
passL=Label(form,text="passwordL:",font=('arial',14),bd=15)
nameL.grid(row=1,sticky=W)
passL.grid(row=2,sticky=W)

nameE=Entry(form,textvariable=un)
passE=Entry(form,textvariable=pw,show="*")

nameE.grid(row=1,column=2)
passE.grid(row=2,column=2)
login=Button(root,text="Login",command=check)
login.pack()
register=Button(root,text="register",command=check)
register.pack()
forgetpassword=Button(root,text="ForgetPassword?",command=check)
forgetpassword.pack()
root.mainloop()

