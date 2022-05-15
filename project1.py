from tkinter import *
from tkinter import messagebox

def myFunc() :
    ##다음페이지뜨기
    return



if __name__=="__main__":
    window=Tk()
    window.geometry("400x400")
    window.title("정보입력")
    labelText=Label(window,text="케이크 호수 선택 ",fg="black",font=("굴림체",10))

    var=IntVar()
    rb1=Radiobutton(window,text="1호",variable=var,value=1)
    rb2=Radiobutton(window,text="2호",variable=var,value=2)
    rb3=Radiobutton(window,text="3호",variable=var,value=3)
    buttonOk=Button(window,text="다음",command=myFunc)
    
    
    rb1.pack(padx=10,pady=3, side=LEFT)
    rb2.pack(padx=10,pady=3, side=LEFT)
    rb3.pack(padx=10,pady=3, side=LEFT)
    buttonOk.pack(padx=3,pady=3, side=LEFT)

    window.mainloop()