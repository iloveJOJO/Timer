import pickle
a=open(r"C:\Users\Administrator\Desktop\record.txt","r")
c=list(a)


x=open(r"C:\Users\Administrator\Desktop\record.pkl","wb")
pickle.dump(c,x)
x.close()
a.close()

#对生成的record.pkl文件进行compile。
t=open("C:\\Users\\Administrator\\Desktop\\record.pkl","rb")
s=print(pickle.load(t))
