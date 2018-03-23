#魔法泡菜的意义在于能够保存任意的事物，并且可以转换回来。
import pickle
my_list=[123,3.14,'小甲鱼',['another list']]
pickle_file=open(r"C:\Users\Administrator\Desktop\kong.txt","ab")
pickle.dump(my_list,pickle_file)
pickle_file.close()

pickle_file=open(r"C:\Users\Administrator\Desktop\kong.txt","rb")
mylist=pickle.load(pickle_file)
print(mylist)
