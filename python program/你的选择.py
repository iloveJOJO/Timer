from tkinter import *
# 导入tkinter模块的所有内容

def callback():         # 定义一个 改变文本的函数 . 
    var.set("吹吧你小屁孩，我才不信呢~\n请右上角关闭此页面！！！")

root = Tk()     # 初始旷的声明 . 

frame1 = Frame(root)   # 在初始旷里面 声明两个模块 . 
frame2 = Frame(root)

# 创建一个文本Label对象
var = StringVar()           #声明可变 变量  . 
var.set("您即将参与的票选含有未成年人限制内容，\n请满18岁后再点击参与！") # 设置变量 . 
textLabel = Label(frame1,           # 绑定到模块1
                  textvariable=var,  # textvariable 是文本变量的意思 .  
                  justify=LEFT)    # 字体 位置 
textLabel.pack(side=LEFT)   #  整体位置 

# 创建一个图像Label对象
# 用PhotoImage实例化一个图片对象（支持gif格式的图片）
photo = PhotoImage(file="18.jpg")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

# 加一个按钮
theButton = Button(frame2, text="已满18周岁", command=callback)  # 按下按钮 执行 callback函数
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()



from tkinter import *
import easygui

root = Tk()
root.title('年会质量部美女投票 !')
v = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
photo = PhotoImage(file="18.jpg")    # 声明一下图片 .
def callback1():
    easygui.msgbox('摸着你的良心请重新选择',title='你真虚伪')
def callback2():
    easygui.msgbox('建议你选择...',  title='你说呢?')
def callback3():
    easygui.msgbox('建议你去医院挂五官科专家会诊',  title='你瞎了眼?')
def callback4():
    easygui.msgbox('他是男的吧',  title='或许?')

    
group=LabelFrame(root,text='质量部美女中最美得是 ?')   # 基于root 制定一个框架 .
group.pack(padx=50)



v1.set(1)
Language = [('孙海霞',1),
            
            
            
        ]
for lang,num in Language:
    b = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=True,padx=30,pady=3,command=callback1)
    l = Label(group,textvariable=v1)  # 将内容添加到框架当中
    l.pack()
    b.pack(anchor=W,fill=X)





v2.set(2)
Language = [('陆兰兰',2),
            
            
            
        ]
for lang,num in Language:
    b1 = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=True,padx=30,pady=3,command=callback2)
    l = Label(group,textvariable=v2)  # 将内容添加到框架当中
    l.pack()
    b1.pack(anchor=W,fill=X)




v3.set(3)
Language = [('许小敏',3),
            
            
            
        ]
for lang,num in Language:
    b2 = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=True,padx=30,pady=3,command=callback3)
    l = Label(group,textvariable=v3)  # 将内容添加到框架当中
    l.pack()
    b2.pack(anchor=W,fill=X)




v4.set(4)
Language = [('蔡文敬',4),
            
            
            
        ]
for lang,num in Language:
    b3 = Radiobutton(group,text=lang,variable=v,value=num,indicatoron=True,padx=30,pady=3,command=callback4)
    l = Label(group,textvariable=v4)  # 将内容添加到框架当中
    l.pack()
    b3.pack(anchor=W,fill=X)
    
c=Button(root,text='返回上一层',command=callback)
c.pack(pady=20)













mainloop()
