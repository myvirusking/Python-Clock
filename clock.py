from tkinter import *
import time
import calendar
from tkinter import ttk
from tkinter import messagebox
import os

class Clock:
    def __init__(self):
        self.startup()

    def startup(self):
        self.root=Tk()
        screen_w=self.root.winfo_screenwidth()
        screen_h=self.root.winfo_screenheight()
        self.root.geometry("400x500+{0}+{1}".format(screen_w//3+50,screen_h//6))
        self.root.resizable(width=False,height=False)

        dc_name=Label(self.root,text="Digital Clock",font=('MS Sans Serif',40,'bold'))
        dc_name.pack(side=TOP,pady=20)

        sms="CLOCK APPLICATION IS FULLY CREATED IN\n\nPYTHON GUI MODULE i.e TKINTER\n\nWHICH IS CREATED BY,\n\n AMAR GUPTA AND ABHISHEK GUPTA\n\nFROM CS DEPT. BIRLA COLLEGE\n\nWITH THE HELP OR UNDER GUIDENCE OF,\n\nMRS.KAJAL JAISHINGHANI MAM"
        dc_name=Label(self.root,text=sms,font=('Helvetica',10,'italic'))
        dc_name.pack(pady=30)

        entry=Button(self.root,text='ENTER >>',font=('Helvetica',12),width=20,height=2,bg='light green',relief=RAISED,bd=5,command=self.main)
        entry.pack(side=BOTTOM)
    
    def main(self):
        self.root.destroy()
        self.root=Tk()
        screen_w=self.root.winfo_screenwidth()
        screen_h=self.root.winfo_screenheight()
        self.root.geometry("400x500+{0}+{1}".format(screen_w//3+50,screen_h//6))
        self.root.resizable(width=False,height=False)

        date=time.strftime("%d-%m-%Y")
        
        self.common_frame=Frame(self.root)
        self.common_frame.pack(side=TOP,pady=125)
        date_f=Frame(self.common_frame)
        date_f.pack()

        clock=Label(date_f,font=('MS Sans Serif',40,'bold'))
        clock.pack()
        
        date=Label(date_f,text=date,font=('Helvetica',15,'italic'))
        date.pack()
        
        def curr_time():
            mytime=time.strftime("%I:%M:%S:%p")
            clock.config(text=mytime)
            clock.after(200, curr_time)
            
        curr_time()

        def mycalendar():
            year=time.strftime("%Y")
            month=time.strftime("%m")
            cal=calendar.month(int(year),int(month))
            self.common_frame.destroy()

            self.common_frame=Frame(self.root)
            self.common_frame.pack(side=TOP)

            date1=time.strftime("%d-%m-%Y")
            date1=Label(self.common_frame,text=date1,font=('MS Sans Serif',20,'underline'))
            date1.pack(side=TOP)
        
            caltop_f=Frame(self.common_frame,bd=5,relief=GROOVE)
            caltop_f.pack(side=TOP,pady=20)

            week=('January','February','March','April','May','June','July','August','September','October','November','December')
            c=ttk.Combobox(caltop_f,values=week,justify=CENTER)
            c.pack(side=LEFT,padx=10,pady=5)
            
            e=Entry(caltop_f,justify=CENTER)
            e.pack(padx=10,pady=5,side=LEFT)

            def go():
                if e.get() and c.get():
                    week_l=['Month','January','February','March','April','May','June','July','August','September','October','November','December']
                    if str(c.get()) in week_l:
                        latest_m=week_l.index(c.get())
                        month=latest_m
                        year=e.get()
                        self.cal_f.destroy()
                        
                        self.cal_f=Frame(self.common_frame,bd=5,relief=GROOVE)
                        self.cal_f.pack(side=BOTTOM)
                        cal=calendar.month(int(year),int(month))
                        m1=Message(self.cal_f,text=cal,font=('courier',20,'bold'),bg='yellow')
                        m1.pack()
                else:
                    messagebox.showinfo("Value Error!","Please Enter Valid Month And Year...")
            
            b=Button(caltop_f,text="GO",bg="light green",command=go)
            b.pack(padx=10,pady=5)
            
            self.cal_f=Frame(self.common_frame,bd=5,relief=GROOVE)
            self.cal_f.pack(side=BOTTOM)
            
            m1=Message(self.cal_f,text=cal,font=('courier',20,'bold'),bg='yellow')
            m1.pack()


        def alarm():
            self.common_frame.destroy()
            self.common_frame=Frame(self.root)
            self.common_frame.pack(side=TOP)

            clock1=Label(self.common_frame,font=('MS Sans Serif',20,'underline'))
            clock1.pack(side=TOP)
        
            def curr_time():
                mytime=time.strftime("%H:%M:%S")
                clock1.config(text=mytime)
                clock1.after(200, curr_time)
            
            curr_time()
            
            
            alarm_f=Frame(self.common_frame)
            alarm_f.pack(pady=60)

            l1=Label(alarm_f,text="HOURS : ",font=('Helvetica',15,'italic'))
            l1.grid(row=0,pady=5)
            s1=Spinbox(alarm_f,from_=0,to=23,justify=CENTER,width=25)
            s1.grid(row=0,column=1,pady=5)
            
            l2=Label(alarm_f,text="MINUTE : ",font=('Helvetica',15,'italic'))
            l2.grid(row=1)
            s2=Spinbox(alarm_f,from_=0,to=59,justify=CENTER,width=25)
            s2.grid(row=1,column=1)

            l3=Label(alarm_f,text="Enter Your Mesaage : ",font=('Helvetica',15,'italic'))
            l3.grid(row=2,columnspan=2,pady=10)
            e1=Entry(alarm_f,justify=CENTER,width=35)
            e1.grid(row=3,columnspan=2)

            def set():
                if int(s1.get())>0 and int(s2.get())>0:
                    Message1()
                    curr_hr=int(time.strftime("%H"))
                    curr_min=int(time.strftime("%M"))
                    alarm_hr= int(s1.get())
                    alarm_min=int(s2.get())
                    print("the alarm time is: {0}:{1}".format(alarm_hr,alarm_min))
                    while True:
                        if alarm_hr == curr_hr and curr_min == alarm_min:
                            print("now Alarm Musing Playing")
                            os.system("start alarm-music.mp3")
                            l4.config(text = "Alarm music playing.....")
                            messagebox.showinfo(title= 'Alarm Message', message= "{}".format(e1.get()))
                            break
                        else: 
                            curr_hr=int(time.strftime("%H"))
                            curr_min=int(time.strftime("%M"))

                else:
                    messagebox.showinfo("Value Error!","Please Enter Valid Hours And Minute...")
                
            def Message1():
                alarm_hr= s1.get()
                alarm_min=s2.get()
                l4.config(text="The Alarm time is Counting...")
                #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
                messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {0}:{1}'.format(alarm_hr,alarm_min))     
                
            b1=Button(alarm_f,text='SET',bg='light green',font=('Helvetica',15,),width=20,height=1,command=set)
            b1.grid(row=4,columnspan=2,pady=15)

            l4=Label(alarm_f,font=('Helvetica',20,))
            l4.grid(row=5,columnspan=2,pady=20)
            
            

        def bottom_nav():
            f1=Frame(self.root)
            f1.pack(side=BOTTOM)
            
            b1=Button(f1,text='Time',width=10,height=2,bg='light green',relief=RAISED,bd=5,command=self.main)
            b1.pack(side=LEFT,padx=10)
            b2=Button(f1,text='Calender',width=10,height=2,bg='light green',relief=RAISED,bd=5,command=mycalendar)
            b2.pack(side=LEFT,padx=10)
            b3=Button(f1,text='Alarm',width=10,height=2,bg='light green',relief=RAISED,bd=5,command=alarm)
            b3.pack(side=LEFT,padx=10)
        bottom_nav()
        

c=Clock()
c.root.mainloop()

