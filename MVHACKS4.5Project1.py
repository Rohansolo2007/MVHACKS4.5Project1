import time as t
from plyer import notification
from tkinter import *

def enterInfo():
    global row1
    global ntd
    J = Label(tk,text=Input1.get()+" ")
    J.grid(column = 0,row = row1)
    F = Label(tk,text=Input2.get()+" ")
    F.grid(column = 1, row = row1)
    ntd.append([Input1.get(),Input2.get()])
    print(ntd)
    row1 += 1

def checkTasks():
    global ntd
    for i in range(len(ntd)):
        currentTime = t.strftime("%H:%M")
        if str(ntd[i][1]) == str(currentTime):
            #Sending the notification
            Header = "Get started on an assignment"
            Content = "New Task, you have to "+ntd[i][0]+" now!"
            notification.notify(title=Header,message=Content,
                                app_icon = None,
                                timeout = 10,
                                toast = False)
            print("Notification Sent")
    tk.after(30000,checkTasks)

row1 = 4
ntd = []
currentTime = ""

tk = Tk()
tk.geometry("700x700")
tk.title("School Reminders")

Task = Label(tk,text="Reminder")
Task.grid(column=0,row=1)

Input1 = Entry(tk,width=20)
Input1.grid(column=1,row=1)

Time = Label(tk,text="Start Time")
Time.grid(column=0,row=2)

Input2 = Entry(tk,width=20)
Input2.grid(column=1,row=2)


Enter = Button(tk,text="Enter",command=enterInfo)
Enter.grid(column = 1, row = 3)

for i in range(len(ntd)):
    print(i)
    currentTime = t.strftime("%H:%M")
    if str(ntd[i][1]) == str(currentTime):
        Heading = "New Assignment"
        Content = f"You have to finish"

tk.after(30000,checkTasks)
tk.mainloop()
