import sqlite3
from tkinter import *

#회원가입 함수
def signup():
    #회원가입 데이터베이스
    def signup_database():
        #DB 파일 생성과 연결
        conn = sqlite3.connect("oka.db") 
        #커서 연결
        cur = conn.cursor()
        #생성하려는 테이블이 없으면 생성 불가능하다
        cur.execute("CREATE TABLE IF NOT EXISTS OKAtable(Email text,ID text,Password text)")
        #생성하려는 테이블에 데이터 추가하기
        cur.execute("INSERT INTO OKAtable Values(?,?,?)",(signup_entry1.get(),signup_entry2.get(),signup_entry3.get()))
        #계정이 생성되었을때 뜨는 문구
        signup_label4 = Label(signup_window,text="계정이 생성되었습니다",font="맑은고딕 15")
        signup_label4.grid(row=6,column=2)
        
        conn.commit()  
        #접속 해체 
        conn.close() 

    #창 닫기
    window.destroy()  

    #회원가입 창 띄우기
    signup_window = Tk() 
    #회원가입 창 띄우기
    signup_window.geometry("500x200") 
    #회원가입 창 제목
    signup_window.title("회원가입") 
    #회원가입 창 크기 제한
    signup_window.resizable(False,False)

    #이메일 & 아이디 & 비밀번호 레이블 
    signup_label1 = Label(signup_window,text="이메일 ",font="맑은고딕 13")
    signup_label1.grid(row=1,column=1)

    signup_label2 = Label(signup_window,text="아이디: ",font="맑은고딕 13")
    signup_label2.grid(row=2,column=1)

    signup_label3 = Label(signup_window,text="비밀번호: ",font="맑은고딕 13")
    signup_label3.grid(row=3,column=1)

    #이메일 & 아이디 & 비밀번호 적는 칸
    Email_text = StringVar() 
    signup_entry1 = Entry(signup_window,textvariable=Email_text)
    signup_entry1.grid(row=1,column=2)

    ID_text = StringVar()
    signup_entry2 = Entry(signup_window,textvariable=ID_text)
    signup_entry2.grid(row=2,column=2)

    Password_text = StringVar()
    signup_entry3 = Entry(signup_window,textvariable=Password_text,show='*')
    signup_entry3.grid(row=3,column=2)

    #회원가입 버튼
    btn1 = Button(signup_window,text="회원가입", width=20, height=1, bg="black", fg="white",command=signup_database)
    btn1.grid(row=4,column=2)

    signup_window.mainloop()

#로그인 함수
def signin():
    def signin_data():
        #DB 파일 생성과 연결
        connect = sqlite3.connect("oka.db")
        #커서 연결
        cur = connect.cursor()
        #테이블 조회
        cur.execute("SELECT * FROM OKAtable WHERE ID=? AND Password=?",(signin_entry1.get(),signin_entry2.get()))
        rows=cur.fetchall()
        #연결 해체
        connect.close()

        #로그인 결과 해체
        print(rows)
        signin_label3 = Label(signin_window,font="맑은고딕 10")
        signin_label3.grid(row=6,column=1)

        if rows!=[]:
            IDname=rows[0][1]
            signin_label3.config(text=IDname + "님, 로그인되셨습니다. 좋은 하루되세요")
        else:
            signin_label3.config(text="이메일 또는 비밀번호가 틀리셨습니다. 회원가입 하셨습니까?")
    
    #창 닫기
    window.destroy()

    #로그인 창 띄우기
    signin_window = Tk() 
    #로그인 창 제목
    signin_window.title("로그인 화면")
    #로그인 창 크기
    signin_window.geometry("500x200") 
    #로그인 창 크기 변경 제한
    signin_window.resizable(False,False)

    #아이디 & 비밀번호 라벨 
    signin_label1 = Label(signin_window,text="아이디: ",font="맑은고딕 13")
    signin_label1.grid(row=1,column=0)

    signin_label2 = Label(signin_window,text="비밀번호: ",font="맑은고딕 13")
    signin_label2.grid(row=2,column=0)

    #아이디 & 비밀번호 쓰는 칸
    ID_text = StringVar() 
    signin_entry1 = Entry(signin_window,textvariable=ID_text)
    signin_entry1.grid(row=1,column=1)

    password_text = StringVar()
    signin_entry2 = Entry(signin_window,textvariable=password_text,show='*')
    signin_entry2.grid(row=2,column=1)

    
    btn2 = Button(signin_window,text="로그인",width=20, height=1, bg="black", fg="white",command=signin_data)
    btn2.grid(row=4,column=1)

    signin_window.mainloop()


#창 만들기
window = Tk()
#창 제목
window.title("로그인 & 회원가입 시스템")
#창 크기
window.geometry("300x200")
#창 크기 변경 제한
window.resizable(False,False)

#OKA 회사 로고
photo = PhotoImage(file = "C:\Program Files\Python Workspace\Sign-Up GUI Project\OKA LOGO.png")
label1 = Label(window, image = photo)
label1.grid(row=0,column=1,columnspan=2)
#로그인 또는 회원가입 레이블
label2 = Label(window, text="로그인 또는 회원가입 해주세요",font="맑은고딕 13")
label2.grid(row=1,column=1,columnspan=2)

#로그인 버튼
btn3 = Button(window, width=20,height = 2, bg = "black", fg = "white", text="로그인", command=signin)
btn3.grid(row=4,column=1)

#회원가입 버튼
btn4 = Button(window,width=20, height = 2, bg = "black", fg = "white", text="회원가입", command=signup)
btn4.grid(row=4,column=2)

window.mainloop()