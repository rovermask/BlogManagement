"""Menu Driven Program for blog system"""
import pickle
import time
import os

try:
    users=pickle.load(open("Records.pkl","rb"))
except:
    users={}

adm={"admin":"pass"}

while True:
    print("Press:-\n\
        1. User Signin\n\
        2. User Signup\n\
        3. Admin Login\n\
        4. Exit\n")
    main_ch=input("-> ")
    if main_ch=="1":
        uname=input("Enter username : ")
        if uname in users:
            pas=input("Enter password : ")
            if pas==users[uname]:
                print("Login Successfull")
                while True:
                    print("Press:-\n\
                        1. Create a new blog\n\
                        2. Read the blog\n\
                        3. Delete a blog\n\
                        4. Logout\n")
                    user_ch=input("-> ")
                    if user_ch=="1":
                        blog_name=input("Enter your blog's name : ")+".txt"
                        if blog_name in os.listdir(uname):
                            print("Blog already exist, change name")
                        else:
                            f=open(f"{uname}/{blog_name}","w")
                            print("Stat writing your content from next line....\n")
                            while True:
                                content=input()
                                if content=="END":
                                    break
                                content+="\n"
                                f.write(content)
                            f.close()
                            print("Blog Created..!!!")
                    elif user_ch=="2":
                        if len(os.listdir(uname))==0:
                            print("No blogs Available")
                        else:
                            count=1
                            l=os.listdir(uname)
                            for i in l:
                                print(f"{count}. {i.split('.')[0]}")
                                count+=1
                            b_name=input("Enter name of the blog you want to read : ")+".txt"
                            f=open(f"{uname}/{b_name}")
                            content=f.read()
                            print(f"Blog Name : {b_name}")
                            print("+++++++++++++++++++++")
                            print(f"{content}")
                            print("+++++++++++++++++++++")
                    elif user_ch=="3":
                        if len(os.listdir(uname))==0:
                            print("No blogs Available")
                        else:
                            count=1
                            l=os.listdir(uname)
                            for i in l:
                                print(f"{count}. {i.split('.')[0]}")
                                count+=1
                            b_name=input("Enter name of the blog you want to delete : ")+".txt"
                            os.remove(f"{uname}/{b_name}")
                            print("Blog Deleted...!!!")
                    elif user_ch=="4":
                        break
                    else:
                        print("Wrong Choice")
            else:
                print("Wrong Password")
        else:
            print("User not found")
    elif main_ch=="2":
        uname=input("Create a username : ")
        if uname not in users:
            pas=input("Create a password : ")
            users[uname]=pas
            pickle.dump(users,open("Records.pkl","wb"))
            os.mkdir(uname)
            print("Signup Successful, Go to signin section")
            time.sleep(2)
        else:
            print("Username exist")
    elif main_ch=="3":
        uname=input("Enter username : ")
        if uname in adm:
            pas=input("Enter password : ")
            if pas==adm[uname]:
                print("Login Successful")
                while True:
                    print("Press:-\n\
                        1. Read user's blogs\n\
                        2. Delete Blog\n\
                        3. Delete User\n\
                        4. Logout\n")
                    adm_ch=input("-> ")
                    if adm_ch=="1":
                        if len(os.listdir())==0 or len(os.listdir())==2:
                            print("No Users Available")
                        else:
                            user_list=os.listdir()
                            u=[i for i in user_list if "." not in i]
                            count=1
                            for i in u:
                                print(f"{count}. {i.split('.')[0]}")
                                count+=1
                            u_name=input("Enter name of the user whose blog you want to read : ")
                            c=1
                            for i in os.listdir(f"{u_name}"):
                                print(f"{c}. {i.split('.')[0]}")
                                c+=1
                            b_name=input("Enter name of the blog you want to read : ")+".txt"
                            f=open(f"{u_name}/{b_name}")
                            print(f"Blog Name : {b_name}")
                            print("+++++++++++++++++++++")
                            print(f"{f.read}")
                            print("+++++++++s++++++++++++")
                    elif adm_ch=="2":
                        pass
                    elif adm_ch=="3":
                        pass
                    elif adm_ch=="4":
                        break
                    else:
                        print("Wrong Choice")
            else:
                print("Wrong password")
        else:
            print("Username not found")
    elif main_ch=="4":
        exit()
    else:
        print("Wrong Choice")
