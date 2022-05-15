from tkinter import *
from tkinter import messagebox

def myFunc() :
    ##다음페이지뜨기
    return



if __name__=="__main__":
    window=Tk()
    window.geometry("400x400")
    window.title("정보입력")

    
    
    nameText=Label(window,text="이름 ",fg="black",font=("굴림체",10))
    name_input = Entry(window, width=10)
    
    phoneText=Label(window,text="연락처 ",fg="black",font=("굴림체",10))
    phone_input = Entry(window, width=10)
    addressText=Label(window,text="주소 ",fg="black",font=("굴림체",10))
    address_input = Entry(window, width=10)
    
    hosuText=Label(window,text="케이크 호수 선택 ",fg="black",font=("굴림체",10))
    
    askText=Label(window,text="남기실말 ",fg="black",font=("굴림체",10))
    ask_input = Entry(window, width=10)
    
    var=IntVar()
    rb1=Radiobutton(window,text="1호",variable=var,value=1)
    rb2=Radiobutton(window,text="2호",variable=var,value=2)
    rb3=Radiobutton(window,text="3호",variable=var,value=3)
    buttonOk=Button(window,text="다음",command=myFunc)
    
    nameText.grid(row=1, column=1)
    name_input.grid(row=1, column=2)
    phoneText.grid(row=2, column=1)
    phone_input.grid(row=2, column=2)
    addressText.grid(row=3, column=1)
    address_input.grid(row=3, column=2)
    askText.grid(row=4, column=1)
    ask_input.grid(row=4, column=2)
    
    hosuText.grid(row=5, column=1)
    rb1.grid(row=6, column=1)
    rb2.grid(row=6, column=2)
    rb3.grid(row=6, column=3)
    buttonOk.grid(row=6, column=4)
    
    

    window.mainloop()