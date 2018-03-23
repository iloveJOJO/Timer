#new 12th character
#magical way
'''
__new__()
__init__()
__del__()
'''
#Mass 算数运算符 and correspond anti-运算符：
'''
__add__
__sub__
__mul__
__truediv__()
__floordiv__()
__mod__()
__divmod__()
__pow__()
__lshift__()
__rshift__()
__and__()
__xor__()
__or__()
'''
#实验12.1 主要验证了__new__()需要在进行类的继承时候，重写调用的方便。
class Capstr(str):
    def __new__(cls,string):
        string=string.upper()
        return str.__new__(cls,string)
a=Capstr("i love python")
print(a)
print(Capstr)#The script invoked directly is considered the __main__ module. It can be imported and accessed the same way as other module.
print(a.__new__(Capstr,a))


b="i love python"
b=str.upper(b)
print(b)

class BBBB:
    def vd(self):
        print("I love python ")
n=BBBB()
n.vd()

t=id(BBBB.__new__(BBBB))

print(t)


#__del__()实验12.2
class De():
    def __init__(self):
        print ("调用了这个方法了")
    def __del__(self):
        print ("调用了delete的方法")
y=De()
y1=y
y2=y1
del y
del y1
del y2#作为Python的垃圾收回机制，del会在删除所有引用项的时候回收该赋值项。
'''
工厂函数和内置函数(BIF)类型不一样;
工厂函数：int(),float(),list(),str()等等都是<class 'type'>,是类对象;
#Pyrhon 无处不对象，加减乘除都是实例对象的操作。

'''
#在进行__运算符__的时候呢，先来回顾和补充一下运算的知识以及format的格式化。
#  /：真正的除法;  //:地板除法;  %：求余除法.

print(5%3)

#例子12.2关于运算符；
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)#重新定义了加法"+"为减法"-"!
    def __sub__(self,other):
        return int.__add__(self,other)#重新定义了减法"-"为加法"+"!
a=New_int(3)
b=New_int(5)
print(a+b)#调用了加法符号"+"但是Python已经改变了运算机制；
print(a-b)



#上面的程序扩展，不调用__sub__等等魔法方法；
class My_int(int):
    def __add__(self,other):
        return int(self)-int(other)
    def __sub__(self,other):
        return int(self)+int(other)
c=My_int(3)
d=My_int(5)
print(c+d)

class int(int):
    def __add__(self,other):
        return int.__sub__(self,other)







#关于反运算的理解，可以说是副运算，主运算不能实行的后备方法；
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self,other)
a=Nint(5)
b=Nint(4)
c=int(3)
d=int(2)
e=New_int(3)
print(c+d)
print(c+b)#这里是个问题啊，难道单层的int，没有双层的优先级高？
print(e+b)
print(a+b)
print(3+5)


#浮点数的精度控制（python默认提供最多17位有效数字,numpy数据库可扩展）
#格式化处理方法：
m="%.30f" % float(1/3)
print(m)
import decimal#导入高精度模块；

l=decimal.Decimal("%.30f" % float(1/3))#配合字符的格式化；
print(l)

#内置函数round函数处理方法：
print(round(1/3,2))

#高精度模块下面使用getcontext内置方法,可以自定义设置浮点精度！

from decimal import Decimal
print(decimal.getcontext())
decimal.getcontext().prec=2

b=Decimal(1)/Decimal(3)
print(b)

#增量赋值语句 a-=1,a-=b
#一元操作符（python中定义一元操作符的魔法方法有__neg__,__pos__, __abs__[绝对值],__invert__(按位取反)）
#简单定制













    
















































































