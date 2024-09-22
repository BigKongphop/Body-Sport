import datetime
from tkinter import*
from tkinter import messagebox
import sqlite3

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    return(conn,cursor)

def time():
    global data1
    data1 = datetime.datetime.now()
    data1.strftime("%X")

def mainwindow():
    root = Tk()
    root.geometry("1000x600")
    root.configure(bg = "#FFFFFF")
    root.config(bg='#28527a')
    root.title("Body & Sport")
    root.option_add('*font',"Calibri 16 bold")
    return root

def show_pass():
    if pwd_s.get() == 1 :
        pwdentry.config(show="")
    else :
        pwdentry.config(show="●")

def login():
    global userentry,pwdentry,button_1,loginframe,pwd_s
    loginframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    loginframe.place(x = 0, y = 0)

    loginframe.create_image(747,93,image=lst_img_login[0])
    loginframe.create_image(743,173,image=lst_img_login[1])
    loginframe.create_image(243,300,image=lst_img_login[2])
    loginframe.create_image(599,327,image=lst_img_login[3])
    loginframe.create_image(599,227,image=lst_img_login[4])
    loginframe.create_image(744,300,image=lst_img_login[5])
    loginframe.create_image(241,213,image=lst_img_login[6])

    userentry = Entry(loginframe,bd=0,bg="#E4E4E4")
    userentry.place(x=555,y=243,width=388,height=38)

    pwdentry = Entry(loginframe,show="●",bd=0,bg="#E4E4E4")
    pwdentry.place(x=555,y=343,width=388,height=38)

    pwd_s = IntVar(value=0)
    button_1 = Checkbutton(loginframe,text="Show password",variable=pwd_s,onvalue=1,offvalue=0,font="Calibri 16 bold",bg="white",fg="#787878",borderwidth=0,highlightthickness=0,command=lambda: show_pass(),activebackground="#FFFFFF")
    button_1.place(x=603,y=401,width=274,height=55)

    button_2 = Button(image=lst_img_login[8],borderwidth=0,highlightthickness=0,command=lambda: registration(),relief="flat",activebackground="#FFFFFF")
    button_2.place(x=134,y=436,width=220,height=70)

    button_3 = Button(image=lst_img_login[9],borderwidth=0,highlightthickness=0,command=lambda: loginclick(userentry.get(),pwdentry.get()),relief="flat",activebackground="#FFFFFF")
    button_3.place(x=629,y=461,width=235,height=74)

def loginclick(user,pwd) :
    global result
    if user == "" :
        messagebox.showwarning("B&S:","Pleas enter username.")
        userentry.focus_force()
    else :
        sql = "select * from login where username=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("B&S:","Please enter password.")
                pwdentry.focus_force()
            else :
                sql = "select * from login where username=? and pwd=? "
                cursor.execute(sql,[user,pwd])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("B&S:","Login Successfully.")
                    home()
                else :
                    messagebox.showwarning("B&S:","Incorrect Password.")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("B&S:","Username not found\n Please register before Login.")
            userentry.focus_force()

def registration():
    global newuser,newpwd,cfpwd,Email
    registerframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    registerframe.place(x = 0, y = 0)

    registerframe.create_image(101,165,image=lst_img_regis[0])
    registerframe.create_image(733,300,image=lst_img_regis[1])
    registerframe.create_image(231,100,image=lst_img_regis[2])
    registerframe.create_image(740,263,image=lst_img_regis[3])
    registerframe.create_image(80,245,image=lst_img_regis[4])
    registerframe.create_image(99,323,image=lst_img_regis[5])
    registerframe.create_image(136,406,image=lst_img_regis[6])
    registerframe.create_image(233,300,image=lst_img_regis[7])

    button_1 = Button(image=lst_img_regis[8],borderwidth=0,highlightthickness=0,command=lambda: login(),relief="flat")
    button_1.place(x=624,y=453,width=220,height=70)

    button_2 = Button(image=lst_img_regis[9],borderwidth=0,highlightthickness=0,command=lambda: registration_click(),relief="flat")
    button_2.place(x=130,y=480,width=196,height=74)

    newuser = Entry(bd=0,bg="#E4E4E4")
    newuser.place(x=52,y=179,width=362,height=39)

    Email = Entry(bd=0,bg="#E4E4E4")
    Email.place(x=52,y=262,width=362,height=39)

    newpwd = Entry(bd=0,bg="#E4E4E4")
    newpwd.place(x=52,y=338,width=362,height=39)

    cfpwd = Entry(bd=0,show="●",bg="#E4E4E4")
    cfpwd.place(x=52,y=420,width=362,height=39)

    newuser.focus_force()

def registration_click() :
    if newuser.get() == "" :
        messagebox.showwarning("B&S: ","Please enter a new username.")
        newuser.focus_force()
    elif Email.get() == "" :
        messagebox.showwarning("B&S: ","Please enter a Email.")
        Email.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("B&S: ","Please enter a password.")
        newpwd.focus_force()
    elif cfpwd.get() == "" :
        messagebox.showwarning("B&S: ","Please enter a confirm password.")
        cfpwd.focus_force()
    elif newpwd.get() != cfpwd.get() :
        messagebox.showwarning("B&S: ","Incorrect a confirm password\nTry again.")
        cfpwd.selection_range(0,END)
        cfpwd.focus_force()
    else :
        sql = "select * from login where username=?"
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("B&S:","The username is already exists.")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
            bmi()

def bmi():
    global w,h,bmiframe
    bmiframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    bmiframe.place(x = 0, y = 0)

    bmiframe.create_image(108,300,image=lst_img_bmi[0])
    bmiframe.create_image(887,300,image=lst_img_bmi[1])
    bmiframe.create_image(496,300,image=lst_img_bmi[2])

    w = Entry(bd=0,bg="#E4E4E4")
    w.place(x=329,y=172,width=330,height=48)

    h = Entry(bd=0,bg="#E4E4E4")
    h.place(x=329,y=270,width=330,height=48)

    button_1 = Button(image=lst_img_bmi[4],borderwidth=0,highlightthickness=5,highlightcolor="#000000",command=lambda: registration(),relief="flat")
    button_1.place(x=23,y=16,width=127,height=42)

    button_2 = Button(image=lst_img_bmi[5],borderwidth=0,highlightthickness=0,command=lambda: sum_bmi(),relief="flat")
    button_2.place(x=379,y=354,width=233,height=68)
    
    button_3 = Button(image=lst_img_bmi[6],borderwidth=0,highlightthickness=0,command=lambda: regis(),relief="flat")
    button_3.place(x=842,y=16,width=127,height=42)

def regis():
    try:
        sql = "select * from login where username=?"
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("B&S:","The username is already exists.")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
                sql = "insert into login values (?,?,?,?)"
                cursor.execute(sql,[newuser.get(),newpwd.get(),"%0.2f"%cal_bmi,Email.get()])
                conn.commit()
                messagebox.showinfo("B&S:","Registration Successfully.")
                newuser.delete(0,END)
                Email.delete(0,END)
                newpwd.delete(0,END)
                cfpwd.delete(0,END)
                login()
    except:
        messagebox.showerror("B&S","Please calculate BMI first.")
       
def sum_bmi():
    global status,cal_bmi
    if w.get() == "" :
        messagebox.showwarning("B&S: ","Please enter Weight.")
        w.focus_force()
    elif h.get() == "" :
        messagebox.showwarning("B&S: ","Please enter Height.")
        h.focus_force()
    elif h.get() != "" and w.get() != "":
        try:
            cal_bmi = int(w.get())/ (int(h.get())/100)**2
            if cal_bmi < 18.5 : 
                status = 'underweight.'
                status_bg = "#93B4D7"
            elif cal_bmi < 25 :
                status = "normal weight."
                status_bg = "#8FC69F"
            elif cal_bmi < 30 :
                status = "overweight."
                status_bg = "#F9D648"
            elif cal_bmi < 35:
                status = "obesity."
                status_bg = "#E4985E"
            else :
                status = "Extremly obese."
                status_bg = "#D55C5B"
            Label(bmiframe,text="BMI = %0.2f"%cal_bmi,bg=status_bg,fg="white",font='Calibri 30 bold').place(x=258,y=489,width=477,height=60)
        except:
            messagebox.showerror("B&S","Enter only numbers.")
        
def home():
    global homeframe
    homeframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    homeframe.place(x = 0, y = 0)

    homeframe.create_image(500,73,image=lst_img_home[0])
    homeframe.create_image(495,368,image=lst_img_home[1])

    button_1 = Button(image=lst_img_home[2],borderwidth=0,highlightthickness=0,command=lambda: profile(),relief="flat")
    button_1.place(x=920,y=-1,width=80,height=80)

    button_2 = Button(image=lst_img_home[3],borderwidth=0,highlightthickness=0,command=lambda: news(),relief="flat")
    button_2.place(x=245,y=96,width=291,height=48)

    button_3 = Button(image=lst_img_home[4],borderwidth=0,highlightthickness=0,command=lambda: train(),relief="flat")
    button_3.place(x=538,y=96,width=244,height=48)

    button_4 = Button(image=lst_img_home[5],borderwidth=0,highlightthickness=0,command=lambda: shop(),relief="flat")
    button_4.place(x=784,y=96,width=169,height=48)

    button_5 = Button(image=lst_img_home[6],borderwidth=0,highlightthickness=0,command=lambda: home(),relief="flat")
    button_5.place(x=12,y=6,width=210,height=130)
    
def news():
    global newsframe
    newsframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    newsframe.place(x = 0, y = 0)

    newsframe.create_image(500,54,image=lst_img_news[0])
    newsframe.create_image(521,299,image=lst_img_news[1])

    button_1 = Button(image=lst_img_news[2],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#0077D1",relief="flat")
    button_1.place(x=247,y=55,width=135,height=54)

    button_2 = Button(image=lst_img_news[3],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#005493",relief="flat")
    button_2.place(x=0,y=0,width=203,height=108)
    
    button_3 = Button(image=lst_img_news[4],borderwidth=0,highlightthickness=0,command=lambda: news_exe(),relief="flat")
    button_3.place(x=709,y=62,width=171,height=45)

    button_4 = Button(image=lst_img_news[5],borderwidth=0,highlightthickness=0,command=lambda: news_body(),relief="flat")
    button_4.place(x=548,y=62,width=157,height=45)
    
    button_5 = Button(image=lst_img_news[6],borderwidth=0,highlightthickness=0,command=lambda: news_sport(),relief="flat")
    button_5.place(x=383,y=62,width=163,height=46)
    
    button_6 = Button(image=lst_img_news[7],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#0077D1",relief="flat")
    button_6.place(x=912,y=55,width=63,height=54)

def news_body():
    global bodyframe
    bodyframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    bodyframe.place(x = 0, y = 0)

    bodyframe.create_image(500,54,image=lst_img_news[0])
    bodyframe.create_image(500,297,image=lst_img_news[9])

    button_1 = Button(image=lst_img_news[2],borderwidth=0,highlightthickness=0,command=lambda: news(),activebackground="#0077D1",relief="flat")
    button_1.place(x=247,y=55,width=135,height=54)

    button_2 = Button(image=lst_img_news[3],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#005493",relief="flat")
    button_2.place(x=0,y=0,width=203,height=108)
    
    button_3 = Button(image=lst_img_news[4],borderwidth=0,highlightthickness=0,command=lambda: news_exe(),relief="flat")
    button_3.place(x=709,y=62,width=171,height=45)

    button_4 = Button(image=lst_img_news[5],borderwidth=0,highlightthickness=0,command=lambda: news_body(),relief="flat")
    button_4.place(x=548,y=62,width=157,height=45)
    
    button_5 = Button(image=lst_img_news[6],borderwidth=0,highlightthickness=0,command=lambda: news_sport(),relief="flat")
    button_5.place(x=383,y=62,width=163,height=46)
    
    button_6 = Button(image=lst_img_news[7],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#0077D1",relief="flat")
    button_6.place(x=912,y=55,width=63,height=54)

def news_sport():
    global sportframe
    newsframe.destroy()
    sportframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    sportframe.place(x = 0, y = 0)

    sportframe.create_image(500,54,image=lst_img_news[0])
    sportframe.create_image(500,301,image=lst_img_news[8])

    button_1 = Button(image=lst_img_news[2],borderwidth=0,highlightthickness=0,command=lambda: news(),activebackground="#0077D1",relief="flat")
    button_1.place(x=247,y=55,width=135,height=54)

    button_2 = Button(image=lst_img_news[3],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#005493",relief="flat")
    button_2.place(x=0,y=0,width=203,height=108)
    
    button_3 = Button(image=lst_img_news[4],borderwidth=0,highlightthickness=0,command=lambda: news_exe(),relief="flat")
    button_3.place(x=709,y=62,width=171,height=45)

    button_4 = Button(image=lst_img_news[5],borderwidth=0,highlightthickness=0,command=lambda: news_body(),relief="flat")
    button_4.place(x=548,y=62,width=157,height=45)
    
    button_5 = Button(image=lst_img_news[6],borderwidth=0,highlightthickness=0,command=lambda: news_sport(),relief="flat")
    button_5.place(x=383,y=62,width=163,height=46)
    
    button_6 = Button(image=lst_img_news[7],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#0077D1",relief="flat")
    button_6.place(x=912,y=55,width=63,height=54)

def news_exe():
    global exeframe
    exeframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    exeframe.place(x = 0, y = 0)

    exeframe.create_image(500,54,image=lst_img_news[0])
    exeframe.create_image(500,300,image=lst_img_news[10])

    button_1 = Button(image=lst_img_news[2],borderwidth=0,highlightthickness=0,command=lambda: news(),activebackground="#0077D1",relief="flat")
    button_1.place(x=247,y=55,width=135,height=54)

    button_2 = Button(image=lst_img_news[3],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#005493",relief="flat")
    button_2.place(x=0,y=0,width=203,height=108)
    
    button_3 = Button(image=lst_img_news[4],borderwidth=0,highlightthickness=0,command=lambda: news_exe(),relief="flat")
    button_3.place(x=709,y=62,width=171,height=45)

    button_4 = Button(image=lst_img_news[5],borderwidth=0,highlightthickness=0,command=lambda: news_body(),relief="flat")
    button_4.place(x=548,y=62,width=157,height=45)
    
    button_5 = Button(image=lst_img_news[6],borderwidth=0,highlightthickness=0,command=lambda: news_sport(),relief="flat")
    button_5.place(x=383,y=62,width=163,height=46)
    
    button_6 = Button(image=lst_img_news[7],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#0077D1",relief="flat")
    button_6.place(x=912,y=55,width=63,height=54)

def train():
    homeframe.destroy()
    trainframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    trainframe.place(x = 0, y = 0)

    trainframe.create_image(500,292,image=lst_img_train[0])
    trainframe.create_image(262,351,image=lst_img_train[1])

    button_1 = Button(image=lst_img_train[2],borderwidth=0,highlightthickness=0,command=lambda: train_ez())
    button_1.place(x=384,y=62,width=162,height=46)

    button_2 = Button(image=lst_img_train[3],borderwidth=0,highlightthickness=0,command=lambda: train_hard())
    button_2.place(x=744,y=62,width=136,height=46)
    
    button_3 = Button(image=lst_img_train[4],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#FF484F")
    button_3.place(x=243,y=55,width=135,height=54)

    button_4 = Button(image=lst_img_train[5],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#ED1C24")
    button_4.place(x=0,y=1,width=203,height=108)
    
    button_5 = Button(image=lst_img_train[6],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#FF484F")
    button_5.place(x=910,y=55,width=63,height=54)
    
    button_6 = Button(image=lst_img_train[7],borderwidth=0,highlightthickness=0,command=lambda: train_normal())
    button_6.place(x=548,y=62,width=194,height=46)

def train_ez():
    homeframe.destroy()
    train_ez_frame = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    train_ez_frame.place(x = 0, y = 0)

    train_ez_frame.create_image(500,294,image=lst_img_train[8])

    button_1 = Button(image=lst_img_train[2],borderwidth=0,highlightthickness=0,command=lambda: train_ez())
    button_1.place(x=384,y=62,width=162,height=46)

    button_2 = Button(image=lst_img_train[3],borderwidth=0,highlightthickness=0,command=lambda: train_hard())
    button_2.place(x=744,y=62,width=136,height=46)
    
    button_3 = Button(image=lst_img_train[4],borderwidth=0,highlightthickness=0,command=lambda: train(),activebackground="#FF484F")
    button_3.place(x=243,y=55,width=135,height=54)

    button_4 = Button(image=lst_img_train[5],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#ED1C24")
    button_4.place(x=0,y=1,width=203,height=108)
    
    button_5 = Button(image=lst_img_train[6],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#FF484F")
    button_5.place(x=910,y=55,width=63,height=54)
    
    button_6 = Button(image=lst_img_train[7],borderwidth=0,highlightthickness=0,command=lambda: train_normal())
    button_6.place(x=548,y=62,width=194,height=46)

def train_normal():
    homeframe.destroy()
    train_normal_frame = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    train_normal_frame.place(x = 0, y = 0)

    train_normal_frame.create_image(500,294,image=lst_img_train[9])

    button_1 = Button(image=lst_img_train[2],borderwidth=0,highlightthickness=0,command=lambda: train_ez())
    button_1.place(x=384,y=62,width=162,height=46)

    button_2 = Button(image=lst_img_train[3],borderwidth=0,highlightthickness=0,command=lambda: train_hard())
    button_2.place(x=744,y=62,width=136,height=46)
    
    button_3 = Button(image=lst_img_train[4],borderwidth=0,highlightthickness=0,command=lambda: train(),activebackground="#FF484F")
    button_3.place(x=243,y=55,width=135,height=54)

    button_4 = Button(image=lst_img_train[5],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#ED1C24")
    button_4.place(x=0,y=1,width=203,height=108)
    
    button_5 = Button(image=lst_img_train[6],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#FF484F")
    button_5.place(x=910,y=55,width=63,height=54)
    
    button_6 = Button(image=lst_img_train[7],borderwidth=0,highlightthickness=0,command=lambda: train_normal())
    button_6.place(x=548,y=62,width=194,height=46)

def train_hard():
    homeframe.destroy()
    train_hard_frame = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    train_hard_frame.place(x = 0, y = 0)

    train_hard_frame.create_image(500,294,image=lst_img_train[10])

    button_1 = Button(image=lst_img_train[2],borderwidth=0,highlightthickness=0,command=lambda: train_ez())
    button_1.place(x=384,y=62,width=162,height=46)

    button_2 = Button(image=lst_img_train[3],borderwidth=0,highlightthickness=0,command=lambda: train_hard())
    button_2.place(x=744,y=62,width=136,height=46)
    
    button_3 = Button(image=lst_img_train[4],borderwidth=0,highlightthickness=0,command=lambda: train(),activebackground="#FF484F")
    button_3.place(x=243,y=55,width=135,height=54)

    button_4 = Button(image=lst_img_train[5],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#ED1C24")
    button_4.place(x=0,y=1,width=203,height=108)
    
    button_5 = Button(image=lst_img_train[6],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#FF484F")
    button_5.place(x=910,y=55,width=63,height=54)
    
    button_6 = Button(image=lst_img_train[7],borderwidth=0,highlightthickness=0,command=lambda: train_normal())
    button_6.place(x=548,y=62,width=194,height=46)

def shop():
    global shopframe,button_2
    shopframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    shopframe.place(x = 0, y = 0)

    shopframe.create_image(500,61,image=lst_img_shop[0])
    shopframe.create_image(107,385,image=lst_img_shop[1])

    button_1 = Button(image=lst_img_shop[3],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
    button_1.place(x=924,y=0,width=76,height=61)

    button_2 = Button(image=lst_img_shop[4],command=lambda: fnclick_ball(0),borderwidth=0,highlightthickness=0,activebackground="#FFFFFF")
    button_2.place(x=247,y=183,width=247,height=171)

    button_3 = Button(image=lst_img_shop[5],command=lambda: fnclick_ball(1),borderwidth=0,highlightthickness=0,activebackground="#FFFFFF")
    button_3.place(x=248,y=384,width=247,height=171)

    button_4 = Button(image=lst_img_shop[6],command=lambda: fnclick_bas(2),borderwidth=0,highlightthickness=0,activebackground="#FFFFFF")
    button_4.place(x=530,y=183,width=217,height=171)

    button_5 = Button(image=lst_img_shop[7],command=lambda: fnclick_bas(3),borderwidth=0,highlightthickness=0,activebackground="#FFFFFF")
    button_5.place(x=530,y=384,width=217,height=171)

    button_6 = Button(image=lst_img_shop[8],command=lambda: fnclick_dum(4),borderwidth=0,highlightthickness=0,activebackground="#FFFFFF")
    button_6.place(x=760,y=183,width=217,height=171)

    button_7 = Button(image=lst_img_shop[9],command=lambda: fnclick_dum(5),borderwidth=0,highlightthickness=0,activebackground="#FFFFFF")
    button_7.place(x=760,y=384,width=217,height=171)

    button_8 = Button(image=lst_img_shop[10],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
    button_8.place(x=0,y=7,width=203,height=108)

    button_9 = Button(image=lst_img_shop[11],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#7BC54B")
    button_9.place(x=421,y=65,width=135,height=54)

    button_10 = Button(image=lst_img_shop[12],borderwidth=0,highlightthickness=0,command=lambda: shop_II(),activebackground="#7BC54B")
    button_10.place(x=0,y=297,width=214,height=62)

    button_11 = Button(image=lst_img_shop[13],borderwidth=0,highlightthickness=0,command=lambda: shop_III(),activebackground="#7BC54B")
    button_11.place(x=0,y=359,width=214,height=62)

    button_12 = Button(image=lst_img_shop[14],borderwidth=0,highlightthickness=0,command=lambda: shop_I(),activebackground="#7BC54B")
    button_12.place(x=0,y=235,width=214,height=62)

    button_13 = Button(image=lst_img_shop[15],borderwidth=0,highlightthickness=0,command=lambda: credit(),activebackground="#FFFFFF")
    button_13.place(x=754,y=69,width=170,height=50)

    button_14 = Button(image=lst_img_shop[16],borderwidth=0,highlightthickness=0,command=lambda: shop_data_II(),activebackground="#FFFFFF")
    button_14.place(x=565,y=69,width=187,height=50)

    button_15 = Button(image=lst_img_Shop_1[10],bg="#7BC54B",borderwidth=0,highlightthickness=0,command=lambda: receipt(),activebackground="#7BC54B")
    button_15.place(x=925,y=61,width=76,height=61)

def receipt():
    global time_ball,sum_ball_lst,amount_ball,time_bas,sum_bas_lst,amount_bas,time_dum,sum_dum_lst,amount_dum
    charge = messagebox.askyesno("B&S","Confirm Order & Pay.")
    sql = "select * from credit where username=? "
    cursor.execute(sql,[userentry.get()])
    result = cursor.fetchone()    
    if charge :
        if result :
            messagebox.showinfo("B&S","Thank you for purchasing.")
            shopframe.destroy()

            time_ball = [0,0,0,0,0,0]
            sum_ball_lst = [0,0,0,0,0,0]
            amount_ball = [0,0,0,0,0,0]

            time_bas = [0,0,0,0,0,0]
            sum_bas_lst = [0,0,0,0,0,0]
            amount_bas = [0,0,0,0,0,0]

            time_dum = [0,0,0,0,0,0]
            sum_dum_lst = [0,0,0,0,0,0]
            amount_dum = [0,0,0,0,0,0]

            home()
        else:
            messagebox.showwarning("B&S:","Please register credit.")
            credit()
            card_id.focus_force()
    else:
        rtn = messagebox.askyesno("B&S","Reset Order?")
        if rtn:
            time_ball = [0,0,0,0,0,0]
            sum_ball_lst = [0,0,0,0,0,0]
            amount_ball = [0,0,0,0,0,0]

            time_bas = [0,0,0,0,0,0]
            sum_bas_lst = [0,0,0,0,0,0]
            amount_bas = [0,0,0,0,0,0]

            time_dum = [0,0,0,0,0,0]
            sum_dum_lst = [0,0,0,0,0,0]
            amount_dum = [0,0,0,0,0,0]

def fnclick_ball(counts) :
    global sum_ball,sum_ball_lst

    time()
    time_ball[counts] = data1
    amount_ball[counts] += 1
    sum_ball = sum_ball + ballprice[counts]
    sum_ball_lst[counts] = amount_ball[counts] * ballprice[counts]
    ball_spy.set(sum_ball)

    print(ball_spy.get())
    print(sum_ball_lst)
    print(amount_ball)
    
def fnclick_bas(counts) :
    global sum_bas

    time()
    time_bas[counts] = data1
    amount_bas[counts] += 1
    sum_bas = sum_bas + basprice[counts]
    sum_bas_lst[counts] = amount_bas[counts] * basprice[counts]
    bas_spy.set(sum_bas)
    print(bas_spy.get())
    print(sum_dum_lst)
    print(amount_bas)

def fnclick_dum(counts) :
    global sum_dum,dumprice

    time()
    time_dum[counts] = data1
    amount_dum[counts] += 1
    sum_dum = sum_dum + dumprice[counts]
    sum_dum_lst[counts] = amount_dum[counts] * dumprice[counts]
    dum_spy.set(sum_dum)

    print(dum_spy.get())
    print(sum_dum_lst)
    print(amount_dum)

def shop_data():
    global shopframe_data,time_dum
    shopframe_data = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    shopframe_data.place(x = 0, y = 0)

    dum_spy.get()+bas_spy.get()+ball_spy.get()

    shopframe_data.create_image(500,61,image=lst_img_Shop_1[0])
    Label(shopframe_data,image=lst_img_Shop_1[6]).place(x=11,y=133)

    Label(shopframe_data, text=dumprice[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=223,width=50,height=20)
    Label(shopframe_data, text=dumprice[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=285,width=50,height=20)
    Label(shopframe_data, text=dumprice[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=355,width=50,height=20)
    Label(shopframe_data, text=dumprice[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=420,width=50,height=20)
    Label(shopframe_data, text=dumprice[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=490,width=50,height=20)
    Label(shopframe_data, text=dumprice[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=550,width=50,height=20)

    Label(shopframe_data, text=amount_dum[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=223,width=50,height=20)
    Label(shopframe_data, text=amount_dum[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=285,width=50,height=20)
    Label(shopframe_data, text=amount_dum[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=355,width=50,height=20)
    Label(shopframe_data, text=amount_dum[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=420,width=50,height=20)
    Label(shopframe_data, text=amount_dum[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=490,width=50,height=20)
    Label(shopframe_data, text=amount_dum[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=550,width=50,height=20)

    Label(shopframe_data, text=time_dum[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=223,width=61,height=30)
    Label(shopframe_data, text=time_dum[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=285,width=61,height=30)
    Label(shopframe_data, text=time_dum[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=355,width=61,height=30)
    Label(shopframe_data, text=time_dum[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=420,width=61,height=30)
    Label(shopframe_data, text=time_dum[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=490,width=61,height=30)
    Label(shopframe_data, text=time_dum[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=550,width=61,height=30)

    Label(shopframe_data, text=sum_dum_lst[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=223,width=70,height=30)
    Label(shopframe_data, text=sum_dum_lst[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=285,width=70,height=30)
    Label(shopframe_data, text=sum_dum_lst[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=355,width=70,height=30)
    Label(shopframe_data, text=sum_dum_lst[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=420,width=70,height=30)
    Label(shopframe_data, text=sum_dum_lst[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=490,width=70,height=30)
    Label(shopframe_data, text=sum_dum_lst[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=550,width=70,height=30)

    button_1 = Button(image=lst_img_Shop_1[1],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
    button_1.place(x=924,y=0,width=76,height=61)
    button_2 = Button(image=lst_img_Shop_1[2],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
    button_2.place(x=0,y=7,width=203,height=108)
    button_3 = Button(image=lst_img_Shop_1[3],borderwidth=0,highlightthickness=0,command=lambda: shop_data_I(),activebackground="#7BC54B")
    button_3.place(x=421,y=65,width=135,height=54)
    button_4 = Button(image=lst_img_Shop_1[4],borderwidth=0,highlightthickness=0,command=lambda: credit(),activebackground="#FFFFFF")
    button_4.place(x=754,y=69,width=170,height=50)
    button_5 = Button(image=lst_img_Shop_1[5],borderwidth=0,highlightthickness=0,command=lambda: shop_data(),activebackground="#FFFFFF")
    button_5.place(x=565,y=69,width=187,height=50)

def shop_data_I():
    global shopframe_data_I,time_dum
    shopframe_data_I = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    shopframe_data_I.place(x = 0, y = 0)

    dum_spy.get()+bas_spy.get()+ball_spy.get()

    shopframe_data_I.create_image(500,61,image=lst_img_Shop_1[0])
    Label(shopframe_data_I,image=lst_img_Shop_1[8]).place(x=11,y=133)

    button_1 = Button(image=lst_img_Shop_1[7],bg="#7BC54B",borderwidth=0,highlightthickness=0,command=lambda: shop_data(),activebackground="#7BC54B")
    button_1.place(x=927,y=61,width=73,height=60)

    Label(shopframe_data_I, text=basprice[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=223,width=50,height=20)
    Label(shopframe_data_I, text=basprice[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=285,width=50,height=20)
    Label(shopframe_data_I, text=basprice[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=355,width=50,height=20)
    Label(shopframe_data_I, text=basprice[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=420,width=50,height=20)
    Label(shopframe_data_I, text=basprice[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=490,width=50,height=20)
    Label(shopframe_data_I, text=basprice[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=550,width=50,height=20)

    Label(shopframe_data_I, text=amount_bas[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=223,width=50,height=20)
    Label(shopframe_data_I, text=amount_bas[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=285,width=50,height=20)
    Label(shopframe_data_I, text=amount_bas[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=355,width=50,height=20)
    Label(shopframe_data_I, text=amount_bas[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=420,width=50,height=20)
    Label(shopframe_data_I, text=amount_bas[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=490,width=50,height=20)
    Label(shopframe_data_I, text=amount_bas[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=550,width=50,height=20)

    Label(shopframe_data_I, text=time_bas[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=223,width=61,height=30)
    Label(shopframe_data_I, text=time_bas[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=285,width=61,height=30)
    Label(shopframe_data_I, text=time_bas[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=355,width=61,height=30)
    Label(shopframe_data_I, text=time_bas[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=420,width=61,height=30)
    Label(shopframe_data_I, text=time_bas[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=490,width=61,height=30)
    Label(shopframe_data_I, text=time_bas[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=550,width=61,height=30)

    Label(shopframe_data_I, text=sum_bas_lst[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=223,width=70,height=30)
    Label(shopframe_data_I, text=sum_bas_lst[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=285,width=70,height=30)
    Label(shopframe_data_I, text=sum_bas_lst[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=355,width=70,height=30)
    Label(shopframe_data_I, text=sum_bas_lst[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=420,width=70,height=30)
    Label(shopframe_data_I, text=sum_bas_lst[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=490,width=70,height=30)
    Label(shopframe_data_I, text=sum_bas_lst[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=550,width=70,height=30)

    button_1 = Button(image=lst_img_Shop_1[1],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
    button_1.place(x=924,y=0,width=76,height=61)
    button_2 = Button(image=lst_img_Shop_1[2],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
    button_2.place(x=0,y=7,width=203,height=108)
    button_3 = Button(image=lst_img_Shop_1[3],borderwidth=0,highlightthickness=0,command=lambda: shop_data_II(),activebackground="#7BC54B")
    button_3.place(x=421,y=65,width=135,height=54)
    button_4 = Button(image=lst_img_Shop_1[4],borderwidth=0,highlightthickness=0,command=lambda: credit(),activebackground="#FFFFFF")
    button_4.place(x=754,y=69,width=170,height=50)
    button_5 = Button(image=lst_img_Shop_1[5],borderwidth=0,highlightthickness=0,command=lambda: shop_data_I(),activebackground="#FFFFFF")
    button_5.place(x=565,y=69,width=187,height=50)

def shop_data_II():
    global shopframe_data_II,time_dum
    shopframe_data_II = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    shopframe_data_II.place(x = 0, y = 0)

    dum_spy.get()+bas_spy.get()+ball_spy.get()

    shopframe_data_II.create_image(500,61,image=lst_img_Shop_1[0])
    Label(shopframe_data_II,image=lst_img_Shop_1[9]).place(x=11,y=133)

    button_1 = Button(image=lst_img_Shop_1[7],bg="#7BC54B",borderwidth=0,highlightthickness=0,command=lambda: shop_data_I(),activebackground="#7BC54B")
    button_1.place(x=927,y=61,width=73,height=60)

    Label(shopframe_data_II, text=ballprice[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=223,width=50,height=20)
    Label(shopframe_data_II, text=ballprice[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=285,width=50,height=20)
    Label(shopframe_data_II, text=ballprice[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=355,width=50,height=20)
    Label(shopframe_data_II, text=ballprice[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=420,width=50,height=20)
    Label(shopframe_data_II, text=ballprice[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=490,width=50,height=20)
    Label(shopframe_data_II, text=ballprice[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=255,y=550,width=50,height=20)

    Label(shopframe_data_II, text=amount_ball[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=223,width=50,height=20)
    Label(shopframe_data_II, text=amount_ball[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=285,width=50,height=20)
    Label(shopframe_data_II, text=amount_ball[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=355,width=50,height=20)
    Label(shopframe_data_II, text=amount_ball[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=420,width=50,height=20)
    Label(shopframe_data_II, text=amount_ball[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=490,width=50,height=20)
    Label(shopframe_data_II, text=amount_ball[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=425,y=550,width=50,height=20)

    Label(shopframe_data_II, text=time_ball[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=223,width=61,height=30)
    Label(shopframe_data_II, text=time_ball[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=285,width=61,height=30)
    Label(shopframe_data_II, text=time_ball[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=355,width=61,height=30)
    Label(shopframe_data_II, text=time_ball[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=420,width=61,height=30)
    Label(shopframe_data_II, text=time_ball[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=490,width=61,height=30)
    Label(shopframe_data_II, text=time_ball[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=602,y=550,width=61,height=30)

    Label(shopframe_data_II, text=sum_ball_lst[0],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=223,width=70,height=30)
    Label(shopframe_data_II, text=sum_ball_lst[1],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=285,width=70,height=30)
    Label(shopframe_data_II, text=sum_ball_lst[2],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=355,width=70,height=30)
    Label(shopframe_data_II, text=sum_ball_lst[3],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=420,width=70,height=30)
    Label(shopframe_data_II, text=sum_ball_lst[4],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=490,width=70,height=30)
    Label(shopframe_data_II, text=sum_ball_lst[5],font="Calibri 18 bold", bg="white",fg="#7BC54B").place(x=825,y=550,width=70,height=30)

    button_1 = Button(image=lst_img_Shop_1[1],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
    button_1.place(x=924,y=0,width=76,height=61)
    button_2 = Button(image=lst_img_Shop_1[2],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
    button_2.place(x=0,y=7,width=203,height=108)
    button_3 = Button(image=lst_img_Shop_1[3],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
    button_3.place(x=421,y=65,width=135,height=54)
    button_4 = Button(image=lst_img_Shop_1[4],borderwidth=0,highlightthickness=0,command=lambda: credit(),activebackground="#FFFFFF")
    button_4.place(x=754,y=69,width=170,height=50)
    button_5 = Button(image=lst_img_Shop_1[5],borderwidth=0,highlightthickness=0,command=lambda: shop_data_II(),activebackground="#FFFFFF")
    button_5.place(x=565,y=69,width=187,height=50)

def shop_I():
    global shopframe_I,ball_1
    shopframe_I = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    shopframe_I.place(x = 0, y = 0)

    shopframe_I.create_image(500,61,image=lst_img_shop[0])
    shopframe_I.create_image(107,385,image=lst_img_shop[1])

    button_1 = Button(image=lst_img_shop[3],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
    button_1.place(x=924,y=0,width=76,height=61)

    button_2 = Button(image=lst_img_shop[4],borderwidth=0,highlightthickness=0,command=lambda: fnclick_ball(0),activebackground="#FFFFFF")
    button_2.place(x=247,y=183,width=247,height=171)
    
    button_3 = Button(image=lst_img_shop[5],borderwidth=0,highlightthickness=0,command=lambda: fnclick_ball(1),activebackground="#FFFFFF")
    button_3.place(x=248,y=384,width=247,height=171)

    button_8 = Button(image=lst_img_shop[10],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
    button_8.place(x=0,y=7,width=203,height=108)

    button_9 = Button(image=lst_img_shop[11],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
    button_9.place(x=421,y=65,width=135,height=54)

    button_10 = Button(image=lst_img_shop[12],borderwidth=0,highlightthickness=0,command=lambda: shop_II(),activebackground="#7BC54B")
    button_10.place(x=0,y=297,width=214,height=62)

    button_11 = Button(image=lst_img_shop[13],borderwidth=0,highlightthickness=0,command=lambda: shop_III(),activebackground="#7BC54B")
    button_11.place(x=0,y=359,width=214,height=62)

    button_12 = Button(image=lst_img_shop[14],borderwidth=0,highlightthickness=0,command=lambda: shop_I(),activebackground="#7BC54B")
    button_12.place(x=0,y=235,width=214,height=62)

    button_13 = Button(image=lst_img_shop[15],borderwidth=0,highlightthickness=0,command=lambda: credit(),activebackground="#7BC54B")
    button_13.place(x=754,y=69,width=170,height=50)

    button_14 = Button(image=lst_img_shop[16],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
    button_14.place(x=565,y=69,width=187,height=50)
    
    button_15 = Button(image=lst_img_shop[17],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_ball(2),activebackground="#FFFFFF")
    button_15.place(x=530,y=150,width=217,height=204)

    button_16 = Button(image=lst_img_shop[18],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_ball(3),activebackground="#FFFFFF")
    button_16.place(x=530,y=384,width=217,height=171)

    button_17 = Button(image=lst_img_shop[19],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_ball(4),activebackground="#FFFFFF")
    button_17.place(x=767,y=165,width=217,height=189)

    button_18 = Button(image=lst_img_shop[20],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_ball(5),activebackground="#FFFFFF")
    button_18.place(x=770,y=384,width=217,height=171)

def shop_II():
    global shopframe_II
    shopframe_II = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    shopframe_II.place(x = 0, y = 0)

    shopframe_II.create_image(500,61,image=lst_img_shop[0])
    shopframe_II.create_image(107,385,image=lst_img_shop[1])

    button_1 = Button(image=lst_img_shop[3],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
    button_1.place(x=924,y=0,width=76,height=61)
    
    button_4 = Button(image=lst_img_shop[6],borderwidth=0,highlightthickness=0,command=lambda: fnclick_bas(1),activebackground="#FFFFFF")
    button_4.place(x=530,y=183,width=217,height=171)

    button_5 = Button(image=lst_img_shop[7],borderwidth=0,highlightthickness=0,command=lambda: fnclick_bas(2),activebackground="#FFFFFF")
    button_5.place(x=530,y=384,width=217,height=171)

    button_8 = Button(image=lst_img_shop[10],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
    button_8.place(x=0,y=7,width=203,height=108)

    button_9 = Button(image=lst_img_shop[11],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
    button_9.place(x=421,y=65,width=135,height=54)

    button_10 = Button(image=lst_img_shop[12],borderwidth=0,highlightthickness=0,command=lambda: shop_II(),activebackground="#7BC54B")
    button_10.place(x=0,y=297,width=214,height=62)

    button_11 = Button(image=lst_img_shop[13],borderwidth=0,highlightthickness=0,command=lambda: shop_III(),activebackground="#7BC54B")
    button_11.place(x=0,y=359,width=214,height=62)

    button_12 = Button(image=lst_img_shop[14],borderwidth=0,highlightthickness=0,command=lambda: shop_I(),activebackground="#7BC54B")
    button_12.place(x=0,y=235,width=214,height=62)

    button_13 = Button(image=lst_img_shop[15],borderwidth=0,highlightthickness=0,command=lambda: credit(),activebackground="#7BC54B")
    button_13.place(x=754,y=69,width=170,height=50)

    button_14 = Button(image=lst_img_shop[16],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
    button_14.place(x=565,y=69,width=187,height=50)

    button_15 = Button(image=lst_img_shop[21],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_bas(0),activebackground="#FFFFFF")
    button_15.place(x=247,y=153,width=247,height=200)

    button_16 = Button(image=lst_img_shop[22],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_bas(1),activebackground="#FFFFFF")
    button_16.place(x=248,y=371,width=247,height=183)

    button_17 = Button(image=lst_img_shop[23],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_bas(4),activebackground="#FFFFFF")
    button_17.place(x=767,y=183,width=217,height=171)

    button_18 = Button(image=lst_img_shop[24],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_bas(5),activebackground="#FFFFFF")
    button_18.place(x=770,y=384,width=217,height=171)

def shop_III():
    global shopframe_III
    shopframe_III = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    shopframe_III.place(x = 0, y = 0)

    shopframe_III.create_image(500,61,image=lst_img_shop[0])
    shopframe_III.create_image(107,385,image=lst_img_shop[1])

    button_1 = Button(image=lst_img_shop[3],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
    button_1.place(x=924,y=0,width=76,height=61)

    button_6 = Button(image=lst_img_shop[8],borderwidth=0,highlightthickness=0,command=lambda: fnclick_dum(4),activebackground="#FFFFFF")
    button_6.place(x=767,y=183,width=217,height=171)

    button_7 = Button(image=lst_img_shop[9],borderwidth=0,highlightthickness=0,command=lambda: fnclick_dum(5),activebackground="#FFFFFF")
    button_7.place(x=770,y=384,width=217,height=171)

    button_8 = Button(image=lst_img_shop[10],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
    button_8.place(x=0,y=7,width=203,height=108)

    button_9 = Button(image=lst_img_shop[11],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
    button_9.place(x=421,y=65,width=135,height=54)

    button_10 = Button(image=lst_img_shop[12],borderwidth=0,highlightthickness=0,command=lambda: shop_II(),activebackground="#7BC54B")
    button_10.place(x=0,y=297,width=214,height=62)

    button_11 = Button(image=lst_img_shop[13],borderwidth=0,highlightthickness=0,command=lambda: shop_III(),activebackground="#7BC54B")
    button_11.place(x=0,y=359,width=214,height=62)

    button_12 = Button(image=lst_img_shop[14],borderwidth=0,highlightthickness=0,command=lambda: shop_I(),activebackground="#7BC54B")
    button_12.place(x=0,y=235,width=214,height=62)

    button_13 = Button(image=lst_img_shop[15],borderwidth=0,highlightthickness=0,command=lambda: credit(),activebackground="#7BC54B")
    button_13.place(x=754,y=69,width=170,height=50)

    button_14 = Button(image=lst_img_shop[16],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
    button_14.place(x=565,y=69,width=187,height=50)

    button_15 = Button(image=lst_img_shop[25],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_dum(0),activebackground="#FFFFFF")
    button_15.place(x=247,y=161,width=247,height=193)

    button_16 = Button(image=lst_img_shop[26],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_dum(1),activebackground="#FFFFFF")
    button_16.place(x=248,y=383,width=247,height=171)

    button_17 = Button(image=lst_img_shop[27],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_dum(2),activebackground="#FFFFFF")
    button_17.place(x=530,y=138,width=217,height=217)

    button_18 = Button(image=lst_img_shop[28],bg="white",borderwidth=0,highlightthickness=0,command=lambda: fnclick_dum(3),activebackground="#FFFFFF")
    button_18.place(x=530,y=384,width=217,height=171)

def profile():
    global profileframe
    profileframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    profileframe.place(x = 0, y = 0)

    profileframe.create_image(500,300,image=lst_img_profile[0])

    sql_student = "SELECT * FROM login WHERE username=?" 
    cursor.execute(sql_student,[userentry.get()])
    result_stu = cursor.fetchone()

    Button(profileframe,text="Logout",bg="#C51E24",fg="white",font='Calibri 30 bold',borderwidth=2,highlightthickness=0,command=lambda: profile_login(),activebackground="#C51E24").place(x=830,y=11,width=140,height=50)

    Label(profileframe,text="BMI = %0.2f"%result_stu[2],bg="#ED1C24",fg="white",font='Calibri 20 bold').place(x=261,y=50,width=477,height=60)
    Label(profileframe,text="Username = "+result_stu[0],bg="#ED1C24",fg="white",font='Calibri 20 bold').place(x=261,y=200,width=477,height=60)
    Label(profileframe,text="Email = "+result_stu[3],bg="#ED1C24",fg="white",font='Calibri 20 bold').place(x=261,y=125,width=477,height=60)

    button_1 = Button(profileframe,image=lst_img_profile[4],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#C51E24")
    button_1.place(x=0,y=11,width=163,height=54)

    button_2 = Button(profileframe,image=lst_img_profile[5],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_I(),activebackground="#ED1C24")
    button_2.place(x=284,y=340,width=434,height=78)

    button_3 = Button(profileframe,image=lst_img_profile[6],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_II(),activebackground="#ED1C24")
    button_3.place(x=282,y=418,width=434,height=78)

    button_4 = Button(profileframe,image=lst_img_profile[7],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_III(),activebackground="#ED1C24")
    button_4.place(x=298,y=495,width=403,height=72)

def profile_login():
    global time_ball,sum_ball_lst,amount_ball,time_bas,sum_bas_lst,amount_bas,time_dum,sum_dum_lst,amount_dum
    time_ball = [0,0,0,0,0,0]
    sum_ball_lst = [0,0,0,0,0,0]
    amount_ball = [0,0,0,0,0,0]

    time_bas = [0,0,0,0,0,0]
    sum_bas_lst = [0,0,0,0,0,0]
    amount_bas = [0,0,0,0,0,0]

    time_dum = [0,0,0,0,0,0]
    sum_dum_lst = [0,0,0,0,0,0]
    amount_dum = [0,0,0,0,0,0]
    login()

def chat_bot_I():
    global chatframe_I
    chatframe_I = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    chatframe_I.place(x = 0, y = 0)

    chatframe_I.create_image(500,300,image=lst_img_profile[8])

    button_1 = Button(chatframe_I,image=lst_img_profile[4],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#C51E24")
    button_1.place(x=0,y=11,width=163,height=54)

    button_3 = Button(chatframe_I,image=lst_img_profile[6],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_II(),activebackground="#ED1C24")
    button_3.place(x=282,y=418,width=434,height=78)

    button_4 = Button(chatframe_I,image=lst_img_profile[7],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_III(),activebackground="#ED1C24")
    button_4.place(x=298,y=495,width=403,height=72)

def chat_bot_II():
    global chatframe_II
    chatframe_II = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    chatframe_II.place(x = 0, y = 0)

    chatframe_II.create_image(500,300,image=lst_img_profile[9])

    button_1 = Button(chatframe_II,image=lst_img_profile[4],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#C51E24")
    button_1.place(x=0,y=11,width=163,height=54)

    button_2 = Button(chatframe_II,image=lst_img_profile[5],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_I(),activebackground="#ED1C24")
    button_2.place(x=284,y=418,width=434,height=78)

    button_4 = Button(chatframe_II,image=lst_img_profile[7],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_III(),activebackground="#ED1C24")
    button_4.place(x=298,y=495,width=403,height=72)

def chat_bot_III():
    global chatframe_III
    chatframe_III = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    chatframe_III.place(x = 0, y = 0)

    chatframe_III.create_image(500,300,image=lst_img_profile[10])

    button_1 = Button(chatframe_III,image=lst_img_profile[4],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#C51E24")
    button_1.place(x=0,y=11,width=163,height=54)

    button_2 = Button(chatframe_III,image=lst_img_profile[5],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_I(),activebackground="#ED1C24")
    button_2.place(x=284,y=418,width=434,height=78)

    button_3 = Button(chatframe_III,image=lst_img_profile[6],borderwidth=0,highlightthickness=0,command=lambda: chat_bot_II(),activebackground="#ED1C24")
    button_3.place(x=282,y=495,width=434,height=78)

def credit():
    global creditframe,card_id,mm_yy,cvv
    sql = "select * from credit where username=?"
    cursor.execute(sql,[userentry.get()])
    result = cursor.fetchall()
    if result :
        messagebox.showinfo("B&S:","You already \nhave a credit card")
        shop()
    else:
        creditframe = Canvas(root,bg = "#FFFFFF",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
        creditframe.place(x = 0, y = 0)

        creditframe.create_image(500,294,image=lst_img_credit[0])

        Label(creditframe, text=("ID Card"),font=("Calibri 16 bold"),bg="white",fg="#A3A3A3").place(x=200,y=300,width=100,height=30)
        Label(creditframe, text=("MM / YY"),font=("Calibri 16 bold"),bg="white",fg="#A3A3A3").place(x=200,y=385,width=100,height=30)
        Label(creditframe, text=("CVV"),font=("Calibri 16 bold"),bg="white",fg="#A3A3A3").place(x=200,y=460,width=96,height=30)

        card_id = Entry(creditframe,bd=0,bg="#E4E4E4")
        card_id.place(x=310,y=288,width=410,height=59)
        mm_yy = Entry(creditframe,bd=0,bg="#E4E4E4")
        mm_yy.place(x=310,y=366,width=410,height=59)
        cvv = Entry(creditframe,bd=0,bg="#E4E4E4")
        cvv.place(x=310,y=441,width=410,height=59)

        button_1 = Button(creditframe,image=lst_img_credit[1],borderwidth=0,highlightthickness=0,command=lambda: profile(),activebackground="#5F9A38")
        button_1.place(x=924,y=0,width=76,height=61)

        button_2 = Button(creditframe,image=lst_img_credit[2],borderwidth=0,highlightthickness=0,command=lambda: home(),activebackground="#5F9A38")
        button_2.place(x=0,y=7,width=203,height=108)

        button_3 = Button(creditframe,image=lst_img_credit[3],borderwidth=0,highlightthickness=0,command=lambda: shop(),activebackground="#7BC54B")
        button_3.place(x=421,y=65,width=135,height=54)

        button_4 = Button(creditframe,image=lst_img_credit[4],borderwidth=0,highlightthickness=0,command=lambda: print("4"),activebackground="#ffffff")
        button_4.place(x=754,y=69,width=170,height=50)

        button_5 = Button(creditframe,image=lst_img_credit[5],borderwidth=0,highlightthickness=0,command=lambda: shop_data_II(),activebackground="#ffffff")
        button_5.place(x=565,y=69,width=187,height=50)

        button_6 = Button(creditframe,image=lst_img_credit[6],bg="white",borderwidth=0,highlightthickness=0,command=lambda: credit_click(),activebackground="#ffffff")
        button_6.place(x=282,y=495,width=434,height=78)

def credit_click():
    if card_id.get() == "" :
        messagebox.showwarning("B&S: ","Please enter ID Card ")
        card_id.focus_force()

        for x in range(len(card_id)):
            count = count + len(card_id[x])
        print('Characters in List = '+str(count))
            
    elif mm_yy.get() == "" :
        messagebox.showwarning("B&S: ","Please enter MM/YY ")
        mm_yy.focus_force()
    elif cvv.get() == "" :
        messagebox.showwarning("B&S: ","Please enter CVV ")
        cvv.focus_force()
    else:
        sql = "insert into credit values (?,?,?,?)"
        param = [userentry.get(),card_id.get(),mm_yy.get(),cvv.get()]
        cursor.execute(sql,param)
        conn.commit()
        messagebox.showinfo("B&S:","Credit card\nadded successfully.")
        card_id.delete(0,END)
        mm_yy.delete(0,END)
        cvv.delete(0,END)
        home()

conn,cursor = createconnection()
time()
root = mainwindow()

def img_login():
    global lst_img_login
    img_1 = PhotoImage(file=("img_login\image_1.png"))
    img_2 = PhotoImage(file=("img_login\image_2.png"))
    img_3 = PhotoImage(file=("img_login\image_3.png"))
    img_4 = PhotoImage(file=("img_login\image_4.png"))
    img_5 = PhotoImage(file=("img_login\image_5.png"))
    img_6 = PhotoImage(file=("img_login\image_6.png"))
    img_7 = PhotoImage(file=("img_login\image_7.png"))

    btn_1 = PhotoImage(file=("img_login\Button_1.png"))
    btn_2 = PhotoImage(file=("img_login\Button_2.png")).subsample(2,2)
    btn_3 = PhotoImage(file=("img_login\Button_3.png"))

    lst_img_login = [img_1,img_2,img_3,img_4,img_5,img_6,img_7,btn_1,btn_2,btn_3]

def img_resis():
    global lst_img_regis
    img_1 = PhotoImage(file=("image_acc\image_1.png"))
    img_2 = PhotoImage(file=("image_acc\image_2.png"))
    img_3 = PhotoImage(file=("image_acc\image_3.png"))
    img_4 = PhotoImage(file=("image_acc\image_4.png"))
    img_5 = PhotoImage(file=("image_acc\image_5.png"))
    img_6 = PhotoImage(file=("image_acc\image_6.png"))
    img_7 = PhotoImage(file=("image_acc\image_7.png"))
    img_8 = PhotoImage(file=("image_acc\image_8.png"))

    btn_1 = PhotoImage(file=("image_acc\Button_1.png"))
    btn_2 = PhotoImage(file=("image_acc\Button_2.png"))

    lst_img_regis = [img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,btn_1,btn_2]

def img_bmi():
    global lst_img_bmi
    img_1 = PhotoImage(file=("image_bmi\image_1.png"))
    img_2 = PhotoImage(file=("image_bmi\image_2.png"))
    img_3 = PhotoImage(file=("image_bmi\image_3.png"))
    img_4 = PhotoImage(file=("image_bmi\image_4.png"))

    btn_1 = PhotoImage(file=("image_bmi\Button_1.png"))
    btn_2 = PhotoImage(file=("image_bmi\Button_2.png"))
    btn_3 = PhotoImage(file=("image_bmi\Button_3.png"))

    lst_img_bmi = [img_1,img_2,img_3,img_4,btn_1,btn_2,btn_3]

def img_home():
    global lst_img_home
    img_1 = PhotoImage(file=("image_home\image_1.png"))
    img_2 = PhotoImage(file=("image_home\image_2.png"))

    btn_1 = PhotoImage(file=("image_home\Button_1.png"))
    btn_2 = PhotoImage(file=("image_home\Button_2.png"))
    btn_3 = PhotoImage(file=("image_home\Button_3.png"))
    btn_4 = PhotoImage(file=("image_home\Button_4.png"))
    btn_5 = PhotoImage(file=("image_home\Button_5.png"))

    lst_img_home = [img_1,img_2,btn_1,btn_2,btn_3,btn_4,btn_5]

def img_news():
    global lst_img_news
    img_1 = PhotoImage(file=("image_news\image_1.png"))

    img_2 = PhotoImage(file=("image_news\image_2.png"))

    btn_1 = PhotoImage(file=("image_news\Button_1.png"))
    btn_2 = PhotoImage(file=("image_news\Button_2.png"))
    btn_3 = PhotoImage(file=("image_news\Button_3.png"))
    btn_4 = PhotoImage(file=("image_news\Button_4.png"))
    btn_5 = PhotoImage(file=("image_news\Button_5.png"))
    btn_6 = PhotoImage(file=("image_news\Button_6.png"))

    img_sp_1 = PhotoImage(file=("image_news\image_3.png"))
    img_bd_1 = PhotoImage(file=("image_news\image_4.png"))
    img_ex_1 = PhotoImage(file=("image_news\image_5.png"))
    lst_img_news = [img_1,img_2,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,img_sp_1,img_bd_1,img_ex_1]

def img_train():
    global lst_img_train
    img_1 = PhotoImage(file=("image_Training\image_1.png")).subsample(2,2)
    img_2 = PhotoImage(file=("image_Training\image_2.png"))
    img_3 = PhotoImage(file=("image_Training\image_3.png"))
    img_4 = PhotoImage(file=("image_Training\image_4.png"))
    img_5 = PhotoImage(file=("image_Training\image_5.png"))

    btn_1 = PhotoImage(file=("image_Training\Button_1.png"))
    btn_2 = PhotoImage(file=("image_Training\Button_2.png"))
    btn_3 = PhotoImage(file=("image_Training\Button_3.png"))
    btn_4 = PhotoImage(file=("image_Training\Button_4.png"))
    btn_5 = PhotoImage(file=("image_Training\Button_5.png"))
    btn_6 = PhotoImage(file=("image_Training\Button_6.png"))

    lst_img_train = [img_1,img_2,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,img_3,img_4,img_5]

def img_shop():
    global lst_img_shop
    img_1 = PhotoImage(file=("image_shop\image_1.png"))
    img_2 = PhotoImage(file=("image_shop\image_2.png"))
    img_3 = PhotoImage(file=("image_shop\image_3.png"))

    btn_1 = PhotoImage(file=("image_shop\Button_1.png"))
    btn_2 = PhotoImage(file=("image_shop\Button_2.png"))
    btn_3 = PhotoImage(file=("image_shop\Button_3.png"))
    btn_4 = PhotoImage(file=("image_shop\Button_4.png"))
    btn_5 = PhotoImage(file=("image_shop\Button_5.png"))
    btn_6 = PhotoImage(file=("image_shop\Button_6.png"))
    btn_7 = PhotoImage(file=("image_shop\Button_7.png"))
    btn_8 = PhotoImage(file=("image_shop\Button_8.png"))
    btn_9 = PhotoImage(file=("image_shop\Button_9.png"))
    btn_10 = PhotoImage(file=("image_shop\Button_10.png"))
    btn_11 = PhotoImage(file=("image_shop\Button_11.png"))
    btn_12 = PhotoImage(file=("image_shop\Button_12.png"))
    btn_13 = PhotoImage(file=("image_shop\Button_13.png"))
    btn_14 = PhotoImage(file=("image_shop\Button_14.png"))

    btn_ball_1 = PhotoImage(file=("image_shop\image_ball\Button_4.png"))
    btn_ball_2 = PhotoImage(file=("image_shop\image_ball\Button_5.png"))
    btn_ball_3 = PhotoImage(file=("image_shop\image_ball\Button_6.png"))
    btn_ball_4 = PhotoImage(file=("image_shop\image_ball\Button_7.png"))

    btn_bas_1 = PhotoImage(file=("image_shop\image_bas\Button_1.png"))
    btn_bas_2 = PhotoImage(file=("image_shop\image_bas\Button_2.png"))
    btn_bas_3 = PhotoImage(file=("image_shop\image_bas\Button_3.png"))
    btn_bas_4 = PhotoImage(file=("image_shop\image_bas\Button_4.png"))
    
    btn_dum_1 = PhotoImage(file=("image_shop\image_dum\Button_2.png"))
    btn_dum_2 = PhotoImage(file=("image_shop\image_dum\Button_3.png"))
    btn_dum_3 = PhotoImage(file=("image_shop\image_dum\Button_4.png"))
    btn_dum_4 = PhotoImage(file=("image_shop\image_dum\Button_5.png"))

    lst_img_shop = [img_1,img_2,img_3,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,btn_11,btn_12,btn_13,btn_14,btn_ball_1,btn_ball_2,btn_ball_3,btn_ball_4
    ,btn_bas_1,btn_bas_2,btn_bas_3,btn_bas_4,btn_dum_1,btn_dum_2,btn_dum_3,btn_dum_4]

def img_profile():
    global lst_img_profile
    img_1 = PhotoImage(file=("image_profile\image_1.png"))
    img_2 = PhotoImage(file=("image_profile\image_2.png"))
    img_3 = PhotoImage(file=("image_profile\image_3.png"))
    img_4 = PhotoImage(file=("image_profile\image_4.png"))
    img_5 = PhotoImage(file=("image_profile\image_5.png"))
    img_6 = PhotoImage(file=("image_profile\image_6.png"))
    img_7 = PhotoImage(file=("image_profile\image_7.png"))

    btn_1 = PhotoImage(file=("image_profile\Button_1.png"))
    btn_2 = PhotoImage(file=("image_profile\Button_2.png"))
    btn_3 = PhotoImage(file=("image_profile\Button_3.png"))
    btn_4 = PhotoImage(file=("image_profile\Button_4.png"))

    lst_img_profile = [img_1,img_2,img_3,img_4,btn_1,btn_2,btn_3,btn_4,img_5,img_6,img_7]

def img_credit():
    global lst_img_credit
    img_1 = PhotoImage(file=("image_credit\image_1.png"))

    btn_1 = PhotoImage(file=("image_credit\Button_1.png"))
    btn_2 = PhotoImage(file=("image_credit\Button_2.png"))
    btn_3 = PhotoImage(file=("image_credit\Button_3.png"))
    btn_4 = PhotoImage(file=("image_credit\Button_4.png"))
    btn_5 = PhotoImage(file=("image_credit\Button_5.png"))
    btn_6 = PhotoImage(file=("image_credit\Button_6.png"))

    lst_img_credit = [img_1,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6]

def img_Shop():
    global lst_img_Shop_1
    img_1 = PhotoImage(file=("img_shop\image_1.png"))
    img_2 = PhotoImage(file=("img_shop\image_2.png")).subsample(2,2)
    img_3 = PhotoImage(file=("img_shop\image_3.png")).subsample(2,2)
    img_4 = PhotoImage(file=("img_shop\image_4.png")).subsample(2,2)

    btn_1 = PhotoImage(file=("img_shop\Button_1.png"))
    btn_2 = PhotoImage(file=("img_shop\Button_2.png"))
    btn_3 = PhotoImage(file=("img_shop\Button_3.png"))
    btn_4 = PhotoImage(file=("img_shop\Button_4.png"))
    btn_5 = PhotoImage(file=("img_shop\Button_5.png"))
    btn_6 = PhotoImage(file=("img_shop\Button_6.png")).subsample(2,2)
    btn_7 = PhotoImage(file=("img_shop\Button_7.png")).subsample(2,2)

    lst_img_Shop_1 = [img_1,btn_1,btn_2,btn_3,btn_4,btn_5,img_2,btn_6,img_3,img_4,btn_7]

img_login()
img_resis()
img_bmi()
img_home()
img_news()
img_train()
img_shop()
img_profile()
img_credit()
img_Shop()

ballprice = [4200,1100,299,499,2490,3100]
basprice = [1990,1590,1699,499,1150,950]
dumprice = [418,479,6375,1890,1350,750]

def amount_lst_ball():
    global amount_ball
    amount_1 = 0
    amount_2 = 0
    amount_3 = 0
    amount_4 = 0
    amount_5 = 0
    amount_6 = 0
    amount_ball = [amount_1,amount_2,amount_3,amount_4,amount_5,amount_6]

def amount_sum_ball():
    global sum_ball_lst
    sum_ball_1 = 0
    sum_ball_2 = 0
    sum_ball_3 = 0
    sum_ball_4 = 0
    sum_ball_5 = 0
    sum_ball_6 = 0
    sum_ball_lst = [sum_ball_1,sum_ball_2,sum_ball_3,sum_ball_4,sum_ball_5,sum_ball_6]

def amount_lst_bas():
    global amount_bas
    amount_1 = 0
    amount_2 = 0
    amount_3 = 0
    amount_4 = 0
    amount_5 = 0
    amount_6 = 0
    amount_bas = [amount_1,amount_2,amount_3,amount_4,amount_5,amount_6]

def amount_sum_bas():
    global sum_bas_lst
    sum_ball_1 = 0
    sum_ball_2 = 0
    sum_ball_3 = 0
    sum_ball_4 = 0
    sum_ball_5 = 0
    sum_ball_6 = 0
    sum_bas_lst = [sum_ball_1,sum_ball_2,sum_ball_3,sum_ball_4,sum_ball_5,sum_ball_6]

def amount_lst_dum():
    global amount_dum
    amount_1 = 0
    amount_2 = 0
    amount_3 = 0
    amount_4 = 0
    amount_5 = 0
    amount_6 = 0
    amount_dum = [amount_1,amount_2,amount_3,amount_4,amount_5,amount_6]

def amount_sum_dum():
    global sum_dum_lst
    sum_ball_1 = 0
    sum_ball_2 = 0
    sum_ball_3 = 0
    sum_ball_4 = 0
    sum_ball_5 = 0
    sum_ball_6 = 0
    sum_dum_lst = [sum_ball_1,sum_ball_2,sum_ball_3,sum_ball_4,sum_ball_5,sum_ball_6]

def data_time_dum():
    global time_dum
    time_dum_1 = 0
    time_dum_2 = 0
    time_dum_3 = 0
    time_dum_4 = 0
    time_dum_5 = 0
    time_dum_6 = 0
    time_dum = [time_dum_1,time_dum_2,time_dum_3,time_dum_4,time_dum_5,time_dum_6]

def data_time_ball():
    global time_ball
    time_ball_1 = 0
    time_ball_2 = 0
    time_ball_3 = 0
    time_ball_4 = 0
    time_ball_5 = 0
    time_ball_6 = 0
    time_ball = [time_ball_1,time_ball_2,time_ball_3,time_ball_4,time_ball_5,time_ball_6]

def data_time_bas():
    global time_bas
    time_bas_1 = 0
    time_bas_2 = 0
    time_bas_3 = 0
    time_bas_4 = 0
    time_bas_5 = 0
    time_bas_6 = 0
    time_bas = [time_bas_1,time_bas_2,time_bas_3,time_bas_4,time_bas_5,time_bas_6]

data_time_ball()
data_time_bas()
data_time_dum()

amount_lst_ball()
amount_lst_bas()
amount_lst_dum()
amount_sum_ball()
amount_sum_bas()
amount_sum_dum()

status = StringVar()
bmi_lst = DoubleVar()

sum_ball = 0
sum_bas = 0
sum_dum = 0

counter = 0
ball_spy = IntVar()
bas_spy = IntVar()
dum_spy = IntVar()
sum_all_spy = IntVar()

login()

c1 = PhotoImage(file="logo_image.png")
root.iconphoto(FALSE,c1)

root.resizable(False,False)
root.mainloop()