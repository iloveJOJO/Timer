#第九章，异常的处理。
#9-1.py
"""
在完整的程序执行过程中会出现许多的错误，常见的9种：
AssertionError:断句判断，在程序中经常有插入进行判定asser后方的真假；
AttributionError:访问对象出错；
IndexError:索引超出范围；
KeyError：字典访问关键字出错；
NameError:输入和引用未定义的变量报错；
OSError:系统应用报错，例如程序进行交互的时候。读取文件；
SyntaxError:语法报错！需要检查程序；
TypeError:在进行不同的数据类型运算的时候会进行报错；
ZeroDivisionError:除数不能为0！
"""
#Try-except, Try-finally语句;识别try下面的程序语句错误并进行编辑反馈；

"""
try:
    检测范围
except  Exception[as reason]:
    出现异常(Exception)后的处理代码
finally:
    在Except之后还是需要执行完毕的动作。
"""

#raise 语句主动出击，抛出自己想要的任何异常。
a=OSError
raise a("不要紧张，这只是个尝试")
#丰富的else语句：
'''
if:
    如果怎么样，就怎么样；
else:
    除了这些，之后怎么样；



while(for):
    循环体，当怎么样的时候，开始怎么样；
else:
    循环之后，不满足条件的怎么样。


#先检测，没有问题，就可以接下来继续干
try:
    fadfa
except:
    fdas
else:
    fadf
'''

#间接地with语句
"""
with open(r"moyigewenjian")as f:
    a=f.readlines()

好处就是代码简洁，不需要关闭文件的代码操作，方便迭代；
"""






















    

    



                              
