from tkinter import *
from ctypes import *
import gmpy2
import libnum

'''
导论第一次作业
项目解决方案名称：凯撒/RSA/xor加密工具
version: 1.2
版本：debug版

python使用外部库：无
程序解密算法链接库：CpytoDll.dll（使用c语言编写）
链接库代码地址（/rsa/data/CpytoDll/pch.cpp)\(/rsa/data/CpytoDll/pch.h)
链接库编译环境：cl、msvc 正常生成

ps：项目将放到组长的github上，关注组长的github
Name：dDostalker
项目地址：
'''



def main():
    #引用
    import os
    import tkinter.messagebox
    from tkinter import ttk



    # 程序参数
    MainWindows = tkinter.Tk()  # 主窗口名称
    Screenwidth = MainWindows.winfo_screenwidth()
    Screenheight = MainWindows.winfo_screenheight()
    ProAddr = os.getcwd()  # 读取当前程序路径
    ProAddr = ProAddr[:-3]
    IcoAddr = ProAddr + "data/ICO.ico"  # 图标位置
    WinScreenMod = '600x400+%d+%d' % ((Screenwidth - 600)/2,(Screenheight - 400)/2)
    MainWindows.geometry(WinScreenMod)
    libc = cdll.LoadLibrary('./CpytoDll.dll')

    #主界面设置
    MainWindows.title("凯撒/RSA/xor加密工具")
    MainWindows.iconbitmap(IcoAddr)
    MainWindows.geometry(WinScreenMod)
    MainWindows.minsize(600, 400)  # 使界面固定
    MainWindows.maxsize(600, 400)
    MainWindows['background'] = "DarkSlateBlue"


    # 设置参数
    #凯撒圈数
    Rog=[]
    for i in range(0,25):
        Rog.append(i+1)

    def rsa(p, q, e, c):
        n = p * q
        phi = (p - 1) * (q - 1)
        d = gmpy2.invert(e, phi)
        m = pow(c, d, n)
        return libnum.n2s(int(m))

    def rsa2(m, p, q,e):
        n = p * q
        phi = (p - 1) * (q - 1)
        c = pow(m, e, n)
        return c

    #程序菜单
    def FMenu1():
        Entry1.place_forget()
        MKS.place_forget()
        Entry2.place_forget()
        Entry3.place_forget()
        Entry4.place_forget()
        KSkey.config(text=' ')
        Mmode.current(0)
        Mkey.current(0)
        MKS.current(0)
        return

        return
    def FMenu3():
        text = '''
        （以下排名不分先后）\n
        项目组长、链接库制作、算法优化、GUI设计制作：    ***
        RSA加密算法设计、GUI审美建议指导:                         ***
        RSA解密算法设计、相关加密资料收集:                           ***
        凯撒加解密设计、团队指导规划:                                  ***
        异或加密设计、测试案例设计:                                      ***
        测试案例设计、信息搜集:                                              ***
        '''
        tkinter.messagebox.showinfo(title='关于', message=text)
        return


    #程序设置flag
    def FLabel(event):
        words.place(x=15, y=110)
        Bnext.config(text='执行'+Mmode.get()+Mkey.get())
        if (Mmode.get() == '凯撒'):
            Entry1.place_forget()
            MKS.place_forget()
            Entry2.place_forget()
            Entry3.place_forget()
            Entry4.place_forget()
            KSkey.config(text='轮数')
            Entry1.place(x=15, y=130)
            MKS.place(x=15,y=300)

            return
        elif (Mmode.get() == 'RSA'):
            Entry1.place_forget()
            MKS.place_forget()
            Entry2.place_forget()
            Entry3.place_forget()
            Entry4.place_forget()
            KSkey.config(text='输入p                                              输入q                                                 输入e')
            Entry1.place(x=15, y=130)
            Entry2.place(x=15,y=300)
            Entry4.place(x=185,y=300)
            Entry5.place(x=350,y=300)
            return
        else:

            MKS.place_forget()
            Entry1.place_forget()
            Entry2.place_forget()
            Entry3.place_forget()
            Entry4.place_forget()
            KSkey.config(text='key')
            Entry1.place(x=15, y=130)
            Entry3.place(x=15,y=300)
            return


    def FNull(event):

        return

# 程序跳转窗口
    def FKSWindowC():
        if(int(MKS.get())):
            KASAC = libc.KASAC
            KASAC.restype = c_char_p
            word = c_char_p(Entry1.get('0.0','end').encode("ascii"))
            key = c_int(int(MKS.get()))
            word2 = KASAC(word,key)
            Entry1.delete(1.0, tkinter.END)
            Entry1.insert("1.0", word2[:-1])
            print(word)
            print(MKS.get())
        return
    def FKSWindowU():
        KASAC = libc.KASAU
        KASAC.restype = c_char_p
        word = c_char_p(Entry1.get('0.0','end').encode("ascii"))
        key = c_int(int(MKS.get()))
        word2 = KASAC(word,key)
        Entry1.delete(1.0, tkinter.END)
        Entry1.insert("1.0", word2[:-1])
        print(word)
        print(MKS.get())
        print(2)
        return
    def FRSAWindowU():
        if(Entry1.get('0.0','end')):
            word = Entry1.get('0.0','end')
            p = int(Entry2.get())
            q = int(Entry4.get())
            e = int(Entry5)
            word2 = rsa(p,q,e,word)
            Entry1.delete(1.0, tkinter.END)
            Entry1.insert("1.0", word2)
            print(3)
            return
        else:
            print("bad input")
            return
    def FRSAWindowC():
        word = Entry1.get('0.0', 'end')
        p = int(Entry2.get())
        q = int(Entry4.get())
        e = int(Entry5)
        word2 = rsa(p, q, e, word)
        word2 = rsa2(p, q, e,word)
        Entry1.delete(1.0, tkinter.END)
        Entry1.insert("1.0", word2)
        print(3)
        return
    def FXorWindowC():
        Xor = libc.Xor
        Xor.restype = c_char_p
        word = c_char_p(Entry1.get('0.0','end').encode("ascii"))
        key = c_int(int(Entry3.get()))
        word2 = Xor(word,key)
        # get_value = ctypes.cast(word2, ctypes.py_object).value
        Entry1.delete(1.0, tkinter.END)
        Entry1.insert("1.0",word2[:-1])
        print(key)
        print(Entry1.get('0.0','end').encode("ascii"))

        return
    def FXorWindowU():
        print(6)
        return

    def Fchoose():
        if(Mmode.get() == '凯撒'):
            if(Mkey.get() == '解密'):
                FKSWindowU()
                return
            else:
                FKSWindowC()
                return
        elif(Mmode.get() == 'RSA'):
            if(Mkey.get()=='解密'):
                FRSAWindowU()
                return
            else:
                FRSAWindowC()
                return
        else:
                FXorWindowC()
                return


    #下拉菜单
    Mmode = ttk.Combobox(MainWindows)
    Mmode['value'] = ('凯撒', 'RSA', 'Xor')
    Mmode.current(0)
    Mmode.bind("<<ComboboxSelected>>", FLabel)

    Mkey = ttk.Combobox(MainWindows)
    Mkey['value'] = ('加密','解密')
    Mkey.current(0)
    Mkey.bind("<<ComboboxSelected>>", FLabel)
    #凯撒专属菜单
    MKS = ttk.Combobox(MainWindows)
    MKS['value'] = Rog
    MKS.current(0)
    MKS.bind("<<ComboboxSelected>>", FNull)

    Wi_menu = tkinter.Menu(MainWindows,bg='#1c1c1c',fg='white')
    Wi_menu.add_command(label="重置", command=FMenu1)
    Wi_menu.add_command(label='e生成',command= FMenu2)
    Wi_menu.add_command(label="关于", command=FMenu3)

    #信息设置
    CryptMod = tkinter.Label(MainWindows, text='选择加密算法', font=('微软雅黑', '25'), fg='white',bg='DarkSlateBlue')
    words = tkinter.Label(MainWindows, text='明文/密文', font=('微软雅黑', '8'), fg='white', bg='DarkSlateBlue')
    KSkey = tkinter.Label(MainWindows, text='   ', font=('微软雅黑', '8'), fg='white', bg='DarkSlateBlue')
    #操作设置
    Bnext = tkinter.Button(MainWindows,text='执行凯撒加密', command = Fchoose,bg='white', bd=0)
    #输入栏
    Entry1 = Text(MainWindows, width=81, height=10, undo=True, autoseparators=False, bg='#1C1C1C',fg='white',insertbackground='white')
    Entry2 = Entry(MainWindows,bg='#1C1C1C',fg='white',insertbackground='white') #RSA key
    Entry4 = Entry(MainWindows,bg='#1C1C1C',fg='white',insertbackground='white') #RSA mode
    Entry3 = Entry(MainWindows,bg='#1C1C1C',fg='white',insertbackground='white') #Xor
    Entry5 =Entry(MainWindows,bg='#1C1C1C',fg='white',insertbackground='white')
    #显示

    MainWindows.config(menu=Wi_menu)
    CryptMod.place(x=10,y=10)
    Mmode.place(x=15,y=80)
    KSkey.place(x=15,y=270)
    Mkey.place(x=200,y=80)
    Bnext.place(x=500,y=360)



    MainWindows.mainloop()

if __name__ == '__main__':
    main()