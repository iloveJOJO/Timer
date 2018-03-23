# p4_5.py
for i in range(10):
    if i%2 !=0:
        print (i)
        continue
    i +=2
    print(i)
input("for 语句结束")
#for，range和continue的搭配，进行两个循环体的交配作用。
#...


#...
name=["孙海霞","蔡文敬","陆兰兰","宋金金","吴丽梅"]
name[0],name[1]=name[1],name[0]
print (name)
input ("列表对换元素")
#对列表本身进行操作，列表本身已经进行了数据置换。
#...

#...
name.pop(0)
name.pop(3)
print (name)
input("POP弹出的语句结束")
#对列表本身进行数据的弹出，列表数据本身已经被改变了，直接输出处理后的列表数据。
#...



#...
print (name[0:2])
print(name[::-1])
print(name)
#列表分片操作，对列表的copy进行取值，列表本身没有任何的改变，可以继续输出name的值。
#...


#...
list1=['dcba']
list2=['artyu']
print(list1>list2)
input("List字符串String大小比较结束")
#普通的列表进行比较时，只进行首字符（对应的ASCII码）或者首数字的大小比较。
#...

#...
print(name)
name.reverse()
print(name)
input("对真值进行反转操作，完成")
#真值反转，reverse
#...

#...
help(dir)
#.........

#define a tuple!!
tuple1=(1,2,3,4,5,6,7,8,9)
print (tuple1)
tuple2=(1,)
tuple3=()
type(tuple2)
isinstance (tuple2,tuple)
isinstance (tuple3,tuple)

#Generally common copy的操作 分片 slice！！！
tuple4=tuple1[::-1]
print(tuple4)
#通过分片进行copy，步长默认为1，设置步长可以选取需要的执行性copy。

#string作为最常见的数据类型，其可以进行的内置函数）方法）是超级多的
string1=("hello,我要学好Python")
string2=string1.capitalize()
print(string2)
capitalize=("nimenhaoa ")

print(capitalize.capitalize())
#深刻理解了什么是“方法”，内置函数的使用形式！

print(string1.count("我"))
#常用的方法还有split，join，replace，find... ...

#format格式化{}表示replacement,提供数据暂存处.
print("{0},你好吗？{1}".format("Python","我很好"))
print("你们好，{0},请将这个数字保留三位小数四舍五入！答案：{1:.3f}".format(3.88888,
3.88888))
#format的用法能进行替换和对替换的内容格式化，通过“：”来进行格式化得定义.

#string专用的格式化符号：%
symbol=("%d,这是一个整数，%f这是一个浮点数，%c这是对应的ASCII码" % (399,399,399))
print(symbol)
#%还有能够进行辅助的指令：m.n,-,+,0... ...

#列表，元祖，字符串统称为序列，处理方式大抵一致。
a=str()
b=str("我爱Python")
print(b)
c=list()
d=list("我爱Python")
print(d)
e=tuple()
f=tuple(["我爱Python"])
print(f)
#序列()的使用迭代每个()中的元素，格式化为相应的序列形式。

string0="我爱Python！"
list0=[]
for each in string0:
    list0.append(each)

print(list0)
#哇塞，我的第一个小程序，提取string的每一个元素增加到列表中去,完成了！




#序列中常见的一些BIF还有(max,min,sum,len),sorted,(reversed,enumerate,zip)。
enumerate(string0)
for each in enumerate(string0):
    print (each)
#其中reverse,enumerate和zip都是返回的迭代器对象！




#第六章，函数章节，Function。
def myfirstfunction(num1,num2):
    print(num1+num2)
print(myfirstfunction(1,2))
input("执行完毕函数调用参数，继续请按enter")
#返回值
def reback():
    return 2,2.5,'我爱Python',
#利用元组或者列表形式打包不同的文本类型，返回值。


#作用域,局部变量（Local variable),全局变量(Global variable),shadowing.
def fun1(num1=0,num2=0):
    print(int(num1+num2))
    def fun2():
        print("我爱Python")
    fun2()

fun1()
#fun2是fun1的内置函数，内置函数所有的作用域都在上层函数内部。

#闭包closure，内置函数对上层函数的变量引用。
def test0():
    step= input("请输入你的性别：")
    name= input("请输入你的年纪：")
    age= int(name)
    def test1():
        if step != '男':
            if age < int(24):
                print("你真是个漂亮的女生")
            else:
                    print("你是成熟的女士呢")
        else:
                if age > int(40):
                    print("你是个成功的男士")
                else:
                       print("你充满活力")
                       
                    
    test1()
test0()
#定义了test0的函数，方便之后调动功能。

#匿名函数：lambda函数，简单的冒号:两边的赋值语句。
Y=lambda x,y:x*y
print(Y(1,2))
#两个十分重要的内置函数:(filter：筛选，map：映射批量处理)
a=list(filter(lambda x:x%2 , range(1000)))
print(a)

b = list(map(lambda x:2*x, range(10)))
print(b)

#Hanoi Tower---typical recursion:函数反复调用本身，可设置调用次数。       
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        hanoi(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
#定义完逻辑函数，递归函数。

n=int(input('请输入汉诺塔的层数：'))#确认输入值。
hanoi(n,'x','y','z')#具体调用函数。


#another example: use recursion to relize the factorial function.
def factorial(n):
    
    if n==1:
        
        return 1
    else:
        return n*factorial(n-1)

number=int(input("请输入一个整数:"))        
result=factorial(number)    
print(result)  
#第六章“递归”收尾结束。

#第七章，字典dictionaryand集合
#Python中唯一的映射类型的数据存储，5种创建方法。
print(dict(a="lhkl",b="shahka",d="djiahka"))

"""
字典的内置方法，主要以下几种：
1,fromkeys():在原有的字典基础上创建一个新的字典，并且返回字典；
2,keys(),values() and items()：分别是提取键，提取值，提取键和值；
3,get()：更宽容的访问，无论需要访问的键Key在不在字典里，都会返回值(None)，set搜不到直接添加；
4,copy()：对字典整个进行复制；
5,pop()popitem()：分别给键弹出值，弹出第一项；
6,update()：更新字典的元素；（感觉没什么用）
7,clear():清空字典。

"""

x=dict(a="lhkl",b="shahka",d="djiahka")
c=x["b"]#表明创建字典有返回值，能够直接访问并且能调用
print(c)
print (x["a"])

#打包解包，有两种方式*-元组的打包；**-字典的打包。
def fight(*python):
    print("总共有这么几种: %d " % len(python))
    print("他们是：%s%s%s" % python)
fight("string","list","tuple")

a={"dafaf":1,"fafa":2,"fasdfafafa":3}
b=a.popitem()#arbitrary 弹出一个值，一般最末尾或者最开始的键值对；
print(type(b))#return的是一个元组。
print(a,b)

def dictionary(**knight):
    print("有多少个组合:%d" % len(knight))
    c="解码器解码出密码：%s" % knight
    """
    非常需要注意的是：元组和字典的不同：
    在利用字符串的格式化时候，元组需要执行到具体的元素，多个值；
    而字典直接把整体视作一个字符串。
    """
    print(c)
    print(type(c))
night={"我":1,"爱":2,"P":3,"y":4,"t":5,"o":6,"n":7}
dictionary (**night)

#集合，没有映射关系的{}即可以视作是集合，和字典是表亲。
#集合的最大特点是：唯一，删除重复元素。
a=set("ninfniof")
print(a)
"""
在集合中进行格式化输出，对象只能是一个，可以是列表，字符串或者字典；
在集合中增加或者删除元素，利用add和remove访问元素值；
利用frozenset fix集合。
"""

#第八章，读取访问外部文件，处理文件并保存在新文件中。
#主要用到的函数"open".
f=open (r"C:\Users\Administrator\Desktop\T\18.1.23\5401S-GU3EA\5401S-GU3EA\_NZ5401S_TS41C_AX_V2.0__5401S-GU3EA___01-22-2018_162043.txt","r")
#非常重要！！"r"用来消除斜杠的转义字符，防止在输出时候的“判定Unicode编码错误！”



#文件的读取，写入利用“对象函数”，和编辑（一个任务）；
#Caution:每一个操作都需要现在Open里设置好相应的模式！否则会报错的。
a=f.read(2)
print(a)
f=open (r"C:\Users\Administrator\Desktop\T\18.1.23\5401S-GU3EA\5401S-GU3EA\_NZ5401S_TS41C_AX_V2.0__5401S-GU3EA___01-22-2018_162043.txt","a")
b=f.write("我爱Python")
print (b)

count=1
boy=[]
girl =[]
f=open(r"C:\Users\Administrator\Desktop\record.txt")
for each_line in f:
    if each_line[:6]!= "== == ==":
        (role,line_spoken)=each_line.split('：',1)
        if role=='小甲鱼':
            boy.append(line_spoken)
        ifrole == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy ='boy_'+str(count)+'.txt'
        file_name_girl='girl_'+str(count)+'.txt'
        boy_file=open(file_name_boy, "w")
        girl_file=open(file_name_girl, "w")
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy=[]
        girl=[]
        count+=1
file_name_boy='boy_'+str(count)+'.txt'
file_name_girl='girl_'+str(count)+'.txt'
boy_file=open(file_name_boy,'w')
girl_file=open(file_name_girl, "w")
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
f.close()
    
dir(os)


















































