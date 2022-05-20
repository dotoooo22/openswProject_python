from tkinter import *
from tkinter import messagebox
import sqlite3
import calendar
import os

def myFunc() :
    ##다음페이지뜨기
    name = str(name_input.get())
    phone = str(phone_input.get())
    ##address = address_input.get()
    if(name=="" or phone=="") :
        messagebox.showwarning("경고", "정보를 다 입력하지 않았습니다.")
        return
    else:
        conn = sqlite3.connect(path + "/cakeDB.db", isolation_level=None)
        c = conn.cursor()
        c.execute("INSERT INTO userTable(name, phone) \
            VALUES(?,?)", \
            (name, phone))
        ##c.execute("CREATE TABLE IF NOT EXISTS userTable \
            ##(name text, phone text)")
        ##c.execute("INSERT INTO userTable VALUES('바보', '1234')")
        print(c.fetchall())
        conn.close()


name = ""
phone = ""
address = ""
path = os.path.dirname(os.path.realpath(__file__))  ##현재디렉토리경로

def showCal() :
 
    # Create a window window
    new_window = Tk()
     
    # Set the background colour of window window
    new_window.config(background = "white")
 
    # set the name of tkinter window window
    new_window.title("CALENDAR")
 
    # Set the configuration of window window
    new_window.geometry("550x600")
 
    # get method returns current text as string
    fetch_year = int(year_field.get())
 
    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)
 
    # Create a label for showing the content of the calendar
    cal_year = Label(new_window, text = cal_content, font = "Consolas 10 bold")
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row = 5, column = 1, padx = 20)
     
    # start the window
    new_window.mainloop()


if __name__=="__main__":
    window=Tk()
    window.geometry("400x400")
    window.title("정보입력")

    window.config(background="Black")
    
    nameText=Label(window,text="이름 ",fg="black",font=("굴림체",10))
    name_input = Entry(window, width=10)
    
    phoneText=Label(window,text="연락처 ",fg="black",font=("굴림체",10))
    phone_input = Entry(window, width=10)
    ##addressText=Label(window,text="주소 ",fg="black",font=("굴림체",10))
    ##address_input = Entry(window, width=10)
    
    hosuText=Label(window,text="케이크 호수 선택 ",fg="black",font=("굴림체",10))
    
    askText=Label(window,text="남기실말 ",fg="black",font=("굴림체",10))
    ask_input = Entry(window, width=10)
    
    var=IntVar()
    rb1=Radiobutton(window,text="1호",variable=var,value=1)
    rb2=Radiobutton(window,text="2호",variable=var,value=2)
    rb3=Radiobutton(window,text="3호",variable=var,value=3)
    buttonOk=Button(window,text="다음",command=myFunc)
    
    cal = Label(window, text = "CALENDAR", bg = "dark gray", font = ("times", 28, 'bold'))
 
    # Create a Enter Year : label
    year = Label(window, text = "Enter Year", bg = "light green")
     
    # Create a text entry box for filling or typing the information. 
    year_field = Entry(window)
 
    # Create a Show Calendar Button and attached to showCal function
    Show = Button(window, text = "Show Calendar", fg = "Black", bg = "Red", command = showCal)
 
    # Create a Exit Button and attached to exit function
    Exit = Button(window, text = "Exit", fg = "Black", bg = "Red", command = exit)
     
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row = 7, column = 1)
 
    year.grid(row = 8, column = 1)
 
    year_field.grid(row = 9, column = 1)
 
    Show.grid(row = 10, column = 1)
 
    Exit.grid(row = 11, column = 1)
    
    nameText.grid(row=1, column=1)
    name_input.grid(row=1, column=2)
    phoneText.grid(row=2, column=1)
    phone_input.grid(row=2, column=2)
    ##addressText.grid(row=3, column=1)
    ##address_input.grid(row=3, column=2)
    askText.grid(row=4, column=1)
    ask_input.grid(row=4, column=2)
    
    hosuText.grid(row=5, column=1)
    rb1.grid(row=6, column=1)
    rb2.grid(row=6, column=2)
    rb3.grid(row=6, column=3)
    buttonOk.grid(row=6, column=4)
    
    

    window.mainloop()