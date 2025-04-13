import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
import os
import mysql.connector
import time
conn=mysql.connector.connect(host="localhost",username="root",password="1234")
c=conn.cursor()
try:
    c.execute("create database blog;")
    conn.commit()
except:
    pass
c.execute("use blog;")
try:
    os.mkdir("USERS")
except:
    pass
c.execute("create table if not exists records (name varchar(100), username varchar(50), password varchar(50));")
conn.commit()
c.execute("create table if not exists adminrecords (adminid varchar(50) primary key, password varchar(50));")
conn.commit()
"""ADMIN ID AND PASSWORD"""
try:
    c.execute("insert into adminrecords (adminid,password) values('blogadmin','blogpass');")
    conn.commit()
except:
    pass
def main():
    def signin():
        def back():
            signin_menu.destroy()
            main()
        main_menu.destroy()
        signin_menu=Tk()
        def submit():
            def proceed():
                try:
                    signin_menu.destroy()
                except:
                    pass            
                user_menu=Tk()
                user_menu.title("User Menu")
                user_menu.resizable(width=1,height=1)
                user_menu.config(background="Yellow")
                f1=('Cobrel',40,'bold')
                f2=('Cobrel',15,'italic bold')
                f3=('Cobrel',12,'italic bold')
                Label(user_menu,text="Sign In\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,sticky=W,padx=5,pady=5)
                Label(user_menu,text=f"Welcome, {user} !!!",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,sticky=W,padx=5,pady=5)
                Label(user_menu,text=f"What do you want to do ?\n",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,padx=5,pady=5,sticky=W)
                def userread():
                    user_menu.destroy()
                    def back():
                        user_read.destroy()
                        proceed()
                    user_read=Tk()
                    user_read.title("View Blogs")
                    user_read.resizable(width=1,height=1)
                    user_read.config(background="Yellow")
                    user_read.resizable(0,0)
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',12,'italic bold')
                    def submit():
                        bname=cb.get()
                        user_read.destroy()
                        blog_read=Tk()
                        def back():
                            blog_read.destroy()
                            proceed()
                        blog_read.title("View Blogs")
                        blog_read.resizable(width=1,height=1)
                        blog_read.config(background="Yellow")
                        f1=('Cobrel',40,'bold')
                        f2=('Cobrel',20,'italic bold')
                        f3=('Cobrel',12,'italic bold')
                        Label(blog_read,text="Here's your blog:----------\n",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)    
                        text_box=Text(blog_read,width=56,height=28)
                        text_box.grid(row=1,padx=5,pady=5,columnspan=2)
                        print("BLOG:",bname)
                        print("USER:",user)
                        fh=open(f"USERS/{user}/{bname}.txt","r")
                        content=fh.read()
                        fh.close()
                        text_box.insert(END,content)
                        Button(blog_read,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=2,padx=5,pady=5)
                        blog_read.resizable(0,0)
                        blog_read.mainloop()
                    Label(user_read,text="View Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                    Label(user_read,text=f"Select blog which you want to read:-----",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                    cb=ttk.Combobox(user_read,textvariable=StringVar(),width=30)
                    try:
                        blogs=os.listdir(f"USERS/{user}")
                        t=[]
                        try:
                            for i in blogs:
                                t.append(i.split(".")[0])
                            cb['values']=[x for x in t]
                            cb.current(0)       
                            cb.grid(row=1,column=1,columnspan=2)
                            Button(user_read,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                            Button(user_read,text="Read",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                        except:
                            user_read.withdraw()
                            messagebox.showwarning("Oops","You've never created a blog")
                            user_read.deiconify()
                            user_read.destroy()
                            proceed()
                    except:
                        user_read.withdraw()
                        messagebox.showerror("Oops","Something's Wrong")
                        user_read.deiconify()
                        user_read.destroy()
                        proceed()
                    user_read.mainloop()
                def create():
                    try:
                        signin_menu.destroy()
                    except:
                        pass
                    user_menu.destroy()
                    create_menu=Tk()
                    def back():
                        create_menu.destroy()
                        proceed()
                    create_menu.title("Blog Creation")
                    create_menu.resizable(width=3,height=3)
                    create_menu.config(background="Yellow")
                    create_menu.resizable(0,0)
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',12,'italic bold')    
                    def submit():
                        blogs=os.listdir(f"USERS/{user}")
                        blog_name=e1.get()
                        content=text_box.get(1.0,'end-1c')
                        print(content)                    
                        if (len(blog_name)<1 or len(content)<1):
                            messagebox.showerror("Error","All fields must be filled !!!")
                        else:
                            if blog_name in blogs:
                                messagebox.showwarning("Exists",f"{blog_name} exist !!!")
                            else:
                                fh=open(f"USERS/{user}/{blog_name}.txt","w")
                                fh.write(content)
                                fh.close()
                                messagebox.showinfo("Done",f'Blog named "{blog_name}" is created')                        
                                e1.delete(0,END)
                                text_box.delete(1.0,'end-1c')
                                create_menu.destroy()
                                proceed()
                                exit()
                    Label(create_menu,text="Blog Creation",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5,columnspan=2)
                    Label(create_menu,text="Name of Blog: ",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,column=0,padx=5,pady=5,sticky=W)
                    e1=Entry(create_menu,width=30)
                    e1.grid(row=1,column=1,padx=5,pady=5)
                    Label(create_menu,text="Write your blog below:",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,column=0,padx=5,pady=5,sticky=W)
                    text_box=Text(create_menu,width=40,height=20)
                    text_box.grid(row=3,column=1,padx=5,pady=5,columnspan=2)
                    Button(create_menu,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=4,column=0,padx=5,pady=5)
                    Button(create_menu,text="Submit",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=4,column=1,padx=5,pady=5)
                    create_menu.mainloop()
                def edit():
                    user_menu.destroy()
                    edit_menu=Tk()
                    def back():
                        edit_menu.destroy()
                        proceed()
                    edit_menu.title("Edit Blogs")
                    edit_menu.resizable(width=1,height=1)
                    edit_menu.config(background="Yellow")
                    edit_menu.resizable(0,0)
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',12,'italic bold')
                    def submit():
                        bname=cb.get()
                        edit_menu.destroy()
                        blog_edit=Tk()
                        def back():
                            blog_edit.destroy()
                            proceed()
                        blog_edit.title("View Blogs")
                        blog_edit.resizable(width=1,height=1)
                        blog_edit.config(background="Yellow")
                        f1=('Cobrel',40,'bold')
                        f2=('Cobrel',20,'italic bold')
                        f3=('Cobrel',12,'italic bold')
                        def submit():
                            updated_content=text_box.get(1.0,'end-1c')
                            fh=open(f"USERS/{user}/{bname}.txt","w")
                            fh.write(updated_content)
                            fh.close()
                            messagebox.showinfo("Done","Blog Updated !!!")
                        def back():
                            blog_edit.destroy()
                            proceed()
                        Label(blog_edit,text="Edit your blog:----------\n",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)    
                        text_box=Text(blog_edit,width=56,height=28)
                        text_box.grid(row=1,padx=5,pady=5,columnspan=3)
                        print("BLOG:",bname)
                        print("USER:",user)
                        fh=open(f"USERS/{user}/{bname}.txt","r")
                        content=fh.read()
                        fh.close()
                        text_box.insert(END,content)
                        Button(blog_edit,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=2,column=0,padx=5,pady=5)
                        Button(blog_edit,text="Update",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=2,column=2,padx=5,pady=5)
                        blog_edit.resizable(0,0)
                        blog_edit.mainloop()
                    Label(edit_menu,text="Edit Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                    cb=ttk.Combobox(edit_menu,textvariable=StringVar(),width=30)
                    Label(edit_menu,text=f"Select blog which you want to edit:-----",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                    try:
                        blogs=os.listdir(f"USERS/{user}")
                        t=[]
                        try:
                            for i in blogs:
                                t.append(i.split(".")[0])
                            cb['values']=[x for x in t]
                            cb.current(0)            
                            cb.grid(row=1,column=1,columnspan=2)
                            Button(edit_menu,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                            Button(edit_menu,text="Edit",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                        except:
                            edit_menu.withdraw()
                            messagebox.showwarning("Oops","You've never created a blog")
                            edit_menu.deiconify()
                            edit_menu.destroy()
                            proceed()
                    except:
                        edit_menu.withdraw()
                        messagebox.showwarning("Oops","Something's Wrong")
                        edit_menu.deiconify()
                        edit_menu.destroy()
                        proceed()
                    edit_menu.mainloop()
                def rewrite():
                    user_menu.destroy()
                    rewrite_menu=Tk()
                    def back():
                        rewrite_menu.destroy()
                        proceed()
                    rewrite_menu.title("Re-write Blog")
                    rewrite_menu.resizable(width=3,height=3)
                    rewrite_menu.config(background="Yellow")
                    rewrite_menu.resizable(0,0)
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',12,'italic bold') 
                    def submit():
                        bname=cb.get()
                        rewrite_menu.destroy()
                        blog_read=Tk()
                        def back():
                            blog_read.destroy()
                            proceed()
                        def submit():
                            updated_content=text_box.get(1.0,'end-1c')
                            if updated_content==content:
                                messagebox.showwarning("Warning","No Changes")
                            else:
                                fh=open(f"USERS/{user}/{bname}.txt","w")
                                fh.write(updated_content)
                                fh.close()
                                messagebox.showinfo("Done","Blog Changed")
                        blog_read.title("View Blogs")
                        blog_read.resizable(width=1,height=1)
                        blog_read.config(background="Yellow")
                        f1=('Cobrel',40,'bold')
                        f2=('Cobrel',20,'italic bold')
                        f3=('Cobrel',12,'italic bold')
                        Label(blog_read,text="Re-write your blog:----------\n",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)    
                        text_box=Text(blog_read,width=56,height=28)
                        text_box.grid(row=1,padx=5,pady=5,columnspan=2)
                        print("BLOG:",bname)
                        print("USER:",user)
                        fh=open(f"USERS/{user}/{bname}.txt","r")
                        content=fh.read()
                        fh.close()
                        Button(blog_read,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=2,column=0,padx=5,pady=5)
                        Button(blog_read,text="Update",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=2,column=1,padx=5,pady=5)
                        blog_read.resizable(0,0)
                        blog_read.mainloop()
                    Label(rewrite_menu,text="Re-write Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                    Label(rewrite_menu,text=f"Select blog which you want to re-write:-----",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                    cb=ttk.Combobox(rewrite_menu,textvariable=StringVar(),width=30)
                    try:
                        blogs=os.listdir(f"USERS/{user}")
                        t=[]
                        try:
                            for i in blogs:
                                t.append(i.split(".")[0])
                            cb['values']=[x for x in t]
                            cb.current(0)            
                            cb.grid(row=1,column=1,columnspan=2)
                            Button(rewrite_menu,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                            Button(rewrite_menu,text="Re-Write",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                        except:
                            rewrite_menu.withdraw()
                            messagebox.showwarning("Oops","You've never created a blog")
                            rewrite_menu.deiconify()
                            rewrite_menu.destroy()
                            proceed()
                    except:
                        rewrite_menu.withdraw()
                        messagebox.showerror("Oops","Something's Wrong")
                        rewrite_menu.deiconify()
                        rewrite_menu.destroy()
                        proceed()
                    rewrite_menu.mainloop()
                def delete():
                    user_menu.destroy()
                    delete_menu=Tk()
                    def back():
                        delete_menu.destroy()
                        proceed()
                    delete_menu.title("View Blogs")
                    delete_menu.resizable(width=1,height=1)
                    delete_menu.config(background="Yellow")
                    delete_menu.resizable(0,0)
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',12,'italic bold')
                    def submit():
                        bname=cb.get()
                        os.remove(f"USERS/{user}/{bname}.txt")
                        messagebox.showinfo("Done","Blog Deleted !!!")
                    Label(delete_menu,text="Delete Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                    Label(delete_menu,text=f"Select blog which you want to delete:-----",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                    cb=ttk.Combobox(delete_menu,textvariable=StringVar(),width=30)
                    try:
                        blogs=os.listdir(f"USERS/{user}")
                        t=[]
                        try:
                            for i in blogs:
                                t.append(i.split(".")[0])
                            cb['values']=[x for x in t]
                            cb.current(0)            
                            cb.grid(row=1,column=1,columnspan=2)
                            Button(delete_menu,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                            Button(delete_menu,text="Delete",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                        except:
                            delete_menu.withdraw()
                            messagebox.showwarning("Oops","You've never created a blog")
                            delete_menu.deiconify()
                            delete_menu.destroy()
                            proceed()
                    except:
                        delete_menu.withdraw()
                        messagebox.showerror("Oops","Something's Wrong")
                        delete_menu.deiconify()
                        delete_menu.destroy()
                        proceed()
                    delete_menu.mainloop()
                def change_pwd():
                    user_menu.destroy()
                    changepwd=Tk()
                    def back():
                        changepwd.destroy()
                        proceed()
                    changepwd.title("Password Change")
                    changepwd.resizable(width=1,height=1)
                    changepwd.config(background="Yellow")
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',10,'italic bold')
                    def submit():
                        user_dict={}
                        current=e1.get()
                        new=e2.get()
                        new_confirm=e3.get()
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        c.execute("select username,password from records;")
                        for i in c:
                            user_dict[i[0]]=i[1]
                        if (len(current)<1 or len(new)<1 or len(new_confirm)<1):
                            messagebox.showerror("Error","All fields are required !!!!")
                        else:
                            if current!=user_dict[user]:
                                messagebox.showerror("Error","Current password is wrong !!!!")
                            else:
                                if new!=new_confirm:
                                    messagebox.showerror("Error"," Please check and confirm password correctly !!!!")
                                else:
                                    q="update records set password=%s where username=%s;"
                                    v=(new,user)
                                    c.execute(q,v)
                                    conn.commit()
                                    messagebox.showinfo("Done","Password Changed !!!")
                    Label(changepwd,text="Change Password\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5,columnspan=4,sticky=N)
                    Label(changepwd,text="Enter your current password:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,column=0,padx=5,pady=5,sticky=W)
                    e1=Entry(changepwd,width=30)
                    e1.grid(row=1,column=3,padx=5,pady=5,sticky=E)
                    Label(changepwd,text="Enter your new password:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,column=0,padx=5,pady=5,sticky=W)
                    e2=Entry(changepwd,width=30)
                    e2.grid(row=2,column=3,padx=5,pady=5,sticky=E)
                    Label(changepwd,text="Confirm new password:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=3,column=0,padx=5,pady=5,sticky=W)
                    e3=Entry(changepwd,width=30)
                    e3.grid(row=3,column=3,padx=5,pady=5,sticky=E)
                    Button(changepwd,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=4,column=0,padx=5,pady=5,sticky=W)
                    Button(changepwd,text="Change Password",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=4,column=3,padx=5,pady=5,sticky=E)
                    changepwd.resizable(0,0)
                    changepwd.mainloop()
                def logout():
                    user_menu.destroy()
                    main()
                Button(user_menu,text="Read my blogs",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=userread).grid(row=3,sticky=W,padx=5,pady=5)                
                Button(user_menu,text="Create a new blog",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=create).grid(row=4,sticky=W,padx=5,pady=5)
                Button(user_menu,text="Edit my blog",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=edit).grid(row=5,padx=5,pady=5,sticky=W)
                Button(user_menu,text="Re-write my blog",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=rewrite).grid(row=6,sticky=W,padx=5,pady=5)
                Button(user_menu,text="Delete My Blog",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=delete).grid(row=7,sticky=W,padx=5,pady=5)
                Button(user_menu,text="Change Password",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=change_pwd).grid(row=8,sticky=W,padx=5,pady=5)
                Button(user_menu,text="Logout",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=logout).grid(row=9,padx=5,pady=5,sticky=W)
                user_menu.resizable(0,0)
                user_menu.mainloop()
            user_dict={}
            user=e1.get()
            pass1=e2.get()
            c.execute("select username,password from records;")
            for i in c:
                user_dict[i[0]]=i[1]
            try:
                if (len(user)<1 or len(pass1)<1):
                    messagebox.showerror("Error","All fields are required !!!!")
                else:
                    if user not in user_dict:
                        messagebox.showerror("Error",f"User '{user}' does not exist !!!")
                        e1.delete(0,END)             
                        e2.delete(0,END)             
                    else:
                        if user_dict[user]==pass1:
                            messagebox.showinfo("Congratulations","Login Successfull")
                            proceed()
                        else:
                            messagebox.showerror("Invalid","Wrong Password !!!\nTry Again !!!")
                            e2.delete(0,END)
            except:
                messagebox.showerror("Sorry","Unknown error occured")
        signin_menu.title("Sign In")
        signin_menu.resizable(width=1,height=1)
        signin_menu.config(background="Yellow")
        f1=('Cobrel',40,'bold')
        f2=('Cobrel',15,'italic bold')
        f3=('Cobrel',12,'italic bold')
        Label(signin_menu,text="Sign In\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,columnspan=2,padx=5,pady=5)
        Label(signin_menu,text="Username",font=f3,bg="Yellow",fg="Black",padx=5,pady=5,).grid(row=1,column=0,padx=5,pady=5,sticky=W)
        e1=Entry(signin_menu,width=30,borderwidth=2)
        e1.grid(row=1,column=1,padx=5,pady=5)
        Label(signin_menu,text="Password",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,column=0,padx=5,pady=5,sticky=W)
        e2=Entry(signin_menu,width=30,borderwidth=2)
        e2.grid(row=2,column=1,padx=5,pady=5)
        Button(signin_menu,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=3,column=0,padx=5,pady=5)
        Button(signin_menu,text="Log In",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=3,column=1,padx=5,pady=5)
        signin_menu.resizable(0,0)
        signin_menu.mainloop()
    def admin():
        def back_to_main_menu():
            adminlogin_menu.destroy()       
            main()
        main_menu.destroy()
        adminlogin_menu=Tk()
        def submit():
            def proceed():
                try:
                    adminlogin_menu.destroy()
                except:
                    pass
                admin_panel=Tk()
                admin_panel.title("Admin Panel")
                admin_panel.resizable(width=1,height=1)
                admin_panel.config(background="Yellow")
                f1=('Cobrel',40,'bold')
                f2=('Cobrel',15,'italic bold')
                f3=('Cobrel',12,'italic bold')
                Label(admin_panel,text="Admin Panel\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                Label(admin_panel,text=f"Welcome, {adminid}",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5,sticky=W)
                Label(admin_panel,text=f"What do you want to do ?\n",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,padx=5,pady=5,sticky=W)
                def view_user_content():
                    admin_panel.destroy()
                    def back():
                        view_content.destroy()
                        proceed()
                    def submit():
                        uname=cb.get()
                        view_content.destroy()
                        view_blog=Tk()
                        view_blog.title("View Blogs")
                        view_blog.resizable(width=1,height=1)
                        view_blog.config(background="Yellow")
                        view_blog.resizable(0,0)
                        f1=('Cobrel',40,'bold')
                        f2=('Cobrel',20,'italic bold')
                        f3=('Cobrel',12,'italic bold')
                        def back():
                            view_blog.destroy()
                            proceed()
                        def submit():
                            blogname=ub.get()
                            view_blog.destroy()
                            blog_read=Tk()
                            print(blogname)
                            def back():
                                blog_read.destroy()
                                proceed()
                            blog_read.title("View Blogs")
                            blog_read.resizable(width=1,height=1)
                            blog_read.config(background="Yellow")
                            f1=('Cobrel',40,'bold')
                            f2=('Cobrel',20,'italic bold')
                            f3=('Cobrel',12,'italic bold')
                            q="select name from records where username=%s;"
                            v=(uname,)
                            c.execute(q,v)
                            Label(blog_read,text=f"Blog Name: {blogname}",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5,sticky=W)    
                            Label(blog_read,text=f"Written By: {c.fetchall()[0][0]}\n",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5,sticky=W)    
                            text_box=Text(blog_read,width=56,height=28)
                            text_box.grid(row=2,padx=5,pady=5)
                            print("BLOG:",blogname)
                            print("USER:",uname)
                            fh=open(f"USERS/{uname}/{blogname}.txt","r")
                            content=fh.read()
                            fh.close()
                            text_box.insert(END,content)
                            Button(blog_read,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=3,padx=5,pady=5)
                            blog_read.resizable(0,0)
                            blog_read.mainloop()
                        Label(view_blog,text="View Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5,sticky=W)
                        Label(view_blog,text="Select user whose you want to read:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                        ub=ttk.Combobox(view_blog,textvariable=StringVar(),width=30)
                        ub.grid(row=2)
                        try:
                            users=os.listdir(f"USERS/{uname}")
                            t=[]
                            try:
                                for i in users:
                                    t.append(i.split(".")[0])
                                ub["values"]=[x for x in t]
                                ub.current(0)
                                ub.grid(row=1,column=1,columnspan=2)
                                Button(view_blog,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                                Button(view_blog,text="Next",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                            except:
                                view_blog.withdraw()
                                messagebox.showwarning("Oops","User never created a blog !!!")
                                view_blog.deiconify()
                                view_blog.destroy()
                                proceed()                        
                        except:
                            view_blog.withdraw()
                            messagebox.showerror("Oops","Something's Wrong")
                            view_blog.deiconify()
                            view_blog.destroy()
                            proceed()                        
                        view_blog.mainloop()
                    view_content=Tk()
                    view_content.title("View Blogs")
                    view_content.resizable(width=1,height=1)
                    view_content.config(background="Yellow")
                    view_content.resizable(0,0)
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',20,'italic bold')
                    f3=('Cobrel',12,'italic bold')
                    Label(view_content,text="View Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                    Label(view_content,text="Select user whose blog you want to read:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                    cb=ttk.Combobox(view_content,textvariable=StringVar(),width=30)
                    cb.grid(row=2)
                    try:
                        users=os.listdir(f"USERS")
                        t=[]
                        try:
                            for i in users:
                                t.append(i)
                            cb["values"]=[x for x in t]
                            cb.current(0)
                            cb.grid(row=1,column=1,columnspan=2)
                            Button(view_content,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                            Button(view_content,text="Next",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                        except:
                            view_content.withdraw()
                            messagebox.showwarning("Oops","No users available !!!")
                            view_content.deiconify()
                            view_content.destroy()
                            proceed()
                    except:
                        view_content.withdraw()
                        messagebox.showerror("Oops","Something's Wrong")
                        view_content.deiconify()
                        view_content.destroy()
                        proceed()
                    view_content.mainloop()
                def delete_user_content():
                    admin_panel.destroy()
                    def back():
                        delete_content.destroy()
                        proceed()
                    def submit():
                        uname=cb.get()
                        delete_content.destroy()
                        delete_blog=Tk()
                        delete_blog.title("Delete Blogs")
                        delete_blog.resizable(width=1,height=1)
                        delete_blog.config(background="Yellow")
                        delete_blog.resizable(0,0)
                        f1=('Cobrel',40,'bold')
                        f2=('Cobrel',20,'italic bold')
                        f3=('Cobrel',12,'italic bold')
                        def back():
                            delete_blog.destroy()
                            proceed()
                        def submit():
                            bname=ub.get()
                            os.remove(f"USERS/{uname}/{bname}.txt")
                            messagebox.showinfo("Removed","Blog Deleted !!!")
                        Label(delete_blog,text="Delete Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5,sticky=W)
                        Label(delete_blog,text="Select blog you want to delete:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                        ub=ttk.Combobox(delete_blog,textvariable=StringVar(),width=30)
                        ub.grid(row=2)
                        try:
                            users=os.listdir(f"USERS/{uname}")
                            t=[]
                            try:
                                for i in users:
                                    t.append(i.split(".")[0])
                                ub["values"]=[x for x in t]
                                ub.current(0)
                                ub.grid(row=1,column=1,columnspan=2)
                                Button(delete_blog,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                                Button(delete_blog,text="Delete",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                            except:
                                delete_blog.withdraw()
                                messagebox.showwarning("Oops","No blogs available !!!")
                                delete_blog.deiconify()
                                delete_blog.destroy()
                                proceed()                        
                        except:
                            delete_blog.withdraw()
                            messagebox.showerror("Oops","Something's Wrong")
                            delete_blog.deiconify()
                            delete_blog.destroy()
                            proceed()
                        delete_blog.mainloop()
                    delete_content=Tk()
                    delete_content.title("Delete Blogs")
                    delete_content.resizable(width=1,height=1)
                    delete_content.config(background="Yellow")
                    delete_content.resizable(0,0)
                    Label(delete_content,text="Delete Blogs\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                    Label(delete_content,text="Select user whose blog you want to delete:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                    cb=ttk.Combobox(delete_content,textvariable=StringVar(),width=30)
                    cb.grid(row=2)
                    try:
                        users=os.listdir(f"USERS")
                        t=[]
                        try:
                            for i in users:
                                t.append(i)
                            cb["values"]=[x for x in t]
                            cb.current(0)
                            cb.grid(row=1,column=1,columnspan=2)
                            Button(delete_content,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                            Button(delete_content,text="Next",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                        except:
                            delete_content.withdraw()
                            messagebox.showwarning("Oops","No users available !!!")
                            delete_content.deiconify()
                            delete_content.destroy()
                            proceed()
                    except:
                        delete_content.withdraw()
                        messagebox.showerror("Oops","Something's Wrong")
                        delete_content.deiconify()
                        delete_content.destroy()
                        proceed()
                    delete_content.mainloop()
                def delete_user():
                    admin_panel.destroy()
                    def back():
                        delete_user_window.destroy()
                        proceed()
                    delete_user_window=Tk()
                    delete_user_window.title("Remove User")
                    delete_user_window.resizable(width=1,height=1)
                    delete_user_window.config(background="Yellow")
                    delete_user_window.resizable(0,0)
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',12,'italic bold')

                    def submit():
                        uname=cb.get()
                        shutil.rmtree(f"USERS/{uname}")
                        q='delete from records where username=%s'
                        v=(uname,)
                        c.execute(q,v)
                        conn.commit()
                        messagebox.showinfo("Done","User Removed !!!")    
                    Label(delete_user_window,text="Remove User\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5)
                    Label(delete_user_window,text="Select user which you want to remove:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,padx=5,pady=5)
                    cb=ttk.Combobox(delete_user_window,textvariable=StringVar(),width=30)
                    try:
                        blogs=os.listdir(f"USERS")
                        t=[]
                        try:
                            for i in blogs:
                                t.append(i)
                            cb['values']=[x for x in t]
                            cb.current(0)       
                            cb.grid(row=1,column=1,columnspan=2)
                            Button(delete_user_window,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=5,column=0,padx=5,pady=5)
                            Button(delete_user_window,text="Delete",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=5,column=1,padx=5,pady=5)
                        except:
                            delete_user_window.withdraw()
                            messagebox.showwarning("Oops","No Users Available !!!")
                            delete_user_window.deiconify()
                            delete_user_window.destroy()
                            proceed()
                    except:
                        delete_user_window.withdraw()
                        messagebox.showerror("Oops","Something's Wrong")
                        delete_user_window.deiconify()
                        delete_user_window.destroy()
                        proceed()
                    delete_user_window.mainloop()
                def admin_reset_pass():
                    admin_panel.destroy()
                    changepwd=Tk()
                    def back():
                        changepwd.destroy()
                        proceed()
                    changepwd.title("Password Change")
                    changepwd.resizable(width=1,height=1)
                    changepwd.config(background="Yellow")
                    f1=('Cobrel',40,'bold')
                    f2=('Cobrel',15,'italic bold')
                    f3=('Cobrel',10,'italic bold')
                    def submit():
                        admin_dict={}
                        current=e1.get()
                        new=e2.get()
                        new_confirm=e3.get()
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        c.execute("select adminid,password from adminrecords;")
                        for i in c:
                            admin_dict[i[0]]=i[1]
                        if (len(current)<1 or len(new)<1 or len(new_confirm)<1):
                            messagebox.showerror("Error","All fields are required !!!!")
                        else:
                            if current!=admin_dict[adminid]:
                                messagebox.showerror("Error","Current password is wrong !!!!")
                            else:
                                if new!=new_confirm:
                                    messagebox.showerror("Error"," Please check and confirm password correctly !!!!")
                                else:
                                    q="update adminrecords set password=%s where adminid=%s;"
                                    v=(new,adminid)
                                    c.execute(q,v)
                                    conn.commit()
                                    messagebox.showinfo("Done","Password Changed !!!")
                    Label(changepwd,text="Change Password\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,padx=5,pady=5,columnspan=4,sticky=N)
                    Label(changepwd,text="Enter your current password:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=1,column=0,padx=5,pady=5,sticky=W)
                    e1=Entry(changepwd,width=30)
                    e1.grid(row=1,column=3,padx=5,pady=5,sticky=E)
                    Label(changepwd,text="Enter your new password:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,column=0,padx=5,pady=5,sticky=W)
                    e2=Entry(changepwd,width=30)
                    e2.grid(row=2,column=3,padx=5,pady=5,sticky=E)
                    Label(changepwd,text="Confirm new password:",font=f2,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=3,column=0,padx=5,pady=5,sticky=W)
                    e3=Entry(changepwd,width=30)
                    e3.grid(row=3,column=3,padx=5,pady=5,sticky=E)
                    Button(changepwd,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=4,column=0,padx=5,pady=5,sticky=W)
                    Button(changepwd,text="Change Password",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=4,column=3,padx=5,pady=5,sticky=E)
                    changepwd.resizable(0,0)    
                    changepwd.mainloop()
                def admin_logout():
                    admin_panel.destroy()
                    main()
                Button(admin_panel,text=" View User Contents ",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=view_user_content).grid(row=3,padx=5,pady=5,sticky=W)
                Button(admin_panel,text="Delete User Content",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=delete_user_content).grid(row=4,padx=5,pady=5,sticky=W)
                Button(admin_panel,text="Delete User",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=delete_user).grid(row=5,padx=5,pady=5,sticky=W)
                Button(admin_panel,text="Reset Password",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=admin_reset_pass).grid(row=6,padx=5,pady=5,sticky=W)
                Button(admin_panel,text="Log Out",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=admin_logout).grid(row=7,padx=5,pady=5,sticky=W)
                admin_panel.resizable(0,0)
                admin_panel.mainloop()
            admin_dict={}
            adminid=e1.get()
            adminpassword=e2.get()
            e1.delete(0,END)
            e2.delete(0,END)
            c.execute("select adminid,password from adminrecords;")
            for i in c:
                admin_dict[i[0]]=i[1]
            try:
                if len(adminid)<1 or len(adminpassword)<1:
                    messagebox.showerror("Error","All fields are required")
                else:
                    if adminid not in admin_dict:
                        messagebox.showerror("Error",f"Admin '{adminid}' does not exists")
                    else:
                        if admin_dict[adminid]==adminpassword:
                            messagebox.showinfo("Congrats","Login Successful")
                            adminlogin_menu.destroy()
                            proceed()
                        else:
                            messagebox.showerror("Oops","Invalid Password\nTry Again")
            except:
                messagebox.showerror("Sorry","Unknown error occured")
        adminlogin_menu.title("Admin Login")
        adminlogin_menu.resizable(width=1,height=1)
        adminlogin_menu.config(background="Yellow")
        f1=('Cobrel',40,'bold')
        f2=('Cobrel',15,'italic bold')
        f3=('Cobrel',12,'italic bold')
        Label(adminlogin_menu,text="Admin Login\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,columnspan=2,padx=5,pady=5)
        Label(adminlogin_menu,text="Admin ID",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,column=0,padx=5,pady=5,sticky=W)
        e1=Entry(adminlogin_menu,width=30,borderwidth=2)
        e1.grid(row=2,column=1,padx=5,pady=5)
        Label(adminlogin_menu,text="Password",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=3,column=0,padx=5,pady=5,sticky=W)
        e2=Entry(adminlogin_menu,width=30,borderwidth=2)
        e2.grid(row=3,column=1,padx=5,pady=5)
        Label(adminlogin_menu,text="",bg="Yellow").grid(row=5)
        Button(adminlogin_menu,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back_to_main_menu).grid(row=6,column=0,padx=5,pady=5)
        Button(adminlogin_menu,text="Submit",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=6,column=1,padx=5,pady=5)
        adminlogin_menu.resizable(0,0)
        adminlogin_menu.mainloop()
    def signup():
        main_menu.destroy()
        signup_menu=Tk()
        def back():
            signup_menu.destroy()
            main()
        def submit():
            name=e1.get()
            user=e2.get()
            pass1=e3.get()
            pass2=e4.get()
            if (len(name)<1 or len(user)<1 or len(pass1)<1 or len(pass2)<1):
                messagebox.showerror("Error","All fields are required !!!!")
            else:
                user_list=[]
                c.execute("select username from records;")
                for i in c:
                    user_list.append(i[0])
                if user in user_list:
                    messagebox.showerror("Error","Username taken !!!\nTry another username !!!")
                    e2.delete(0,END)        
                else:
                    if (pass1!=pass2):
                        messagebox.showerror("Error","Both password does not match")
                        e3.delete(0,END)
                        e4.delete(0,END)
                    else:        
                        q="insert into records (name,username,password) values (%s,%s,%s);"
                        v=(name,user,pass1)
                        c.execute(q,v)
                        conn.commit()
                        os.mkdir(f"USERS/{user}")
                        messagebox.showinfo("Congratulations","User Created !!!\nGo Sign In !!!")
                        time.sleep(1)
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        signup_menu.destroy()
                        main()
        signup_menu.title("Sign Up")
        signup_menu.resizable(width=1,height=1)
        signup_menu.config(background="Yellow")
        f1=('Cobrel',40,'bold')
        f2=('Cobrel',15,'italic bold')
        f3=('Cobrel',12,'italic bold')
        Label(signup_menu,text="Sign Up\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,columnspan=2,padx=5,pady=5)
        Label(signup_menu,text="Full Name",font=f3,bg="Yellow",fg="Black",padx=5,pady=5,).grid(row=1,column=0,padx=5,pady=5,sticky='w')
        e1=Entry(signup_menu,width=30,borderwidth=2)
        e1.grid(row=1,column=1,padx=5,pady=5)
        Label(signup_menu,text="Username",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=2,column=0,padx=5,pady=5,sticky=W)
        e2=Entry(signup_menu,width=30,borderwidth=2)
        e2.grid(row=2,column=1,padx=5,pady=5)
        Label(signup_menu,text="Password",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=3,column=0,padx=5,pady=5,sticky=W)
        e3=Entry(signup_menu,width=30,borderwidth=2)
        e3.grid(row=3,column=1,padx=5,pady=5)
        Label(signup_menu,text="Confirm Password",font=f3,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=4,column=0,padx=5,pady=5,sticky=W)
        e4=Entry(signup_menu,width=30,borderwidth=2)
        e4.grid(row=4,column=1,padx=5,pady=5)
        Label(signup_menu,text="",bg="Yellow").grid(row=5)
        Button(signup_menu,text="Main Menu",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=back).grid(row=6,column=0,padx=5,pady=5)
        Button(signup_menu,text="Sign Up",font=f3,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=submit).grid(row=6,column=1,padx=5,pady=5)
        signup_menu.resizable(0,0)
        signup_menu.mainloop()
    main_menu=Tk()
    main_menu.title("Blog System")
    main_menu.resizable(width=1,height=1)
    main_menu.config(background="Yellow")
    f1=('Cobrel',40,'bold')
    f2=('Cobrel',15,'italic bold')
    Label(main_menu,text="Blog System\n",font=f1,bg="Yellow",fg="Black",padx=5,pady=5).grid(row=0,columnspan=3,padx=5,pady=5)
    Button(main_menu,text="Sign Up",font=f2,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=signup).grid(row=1,column=0,padx=5,pady=5)
    Button(main_menu,text="Admin Login",font=f2,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=admin).grid(row=1,column=1,padx=5,pady=5)
    Button(main_menu,text="Sign In",font=f2,bg="Black",fg="Yellow",padx=5,pady=5,borderwidth=5,command=signin).grid(row=1,column=2,padx=5,pady=5)
    main_menu.resizable(0,0)
    main_menu.mainloop()
main()