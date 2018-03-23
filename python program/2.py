import pickle
a=open(r"C:\Users\Administrator\Desktop\record.txt","r")
c=list(a)


x=open(r"C:\Users\Administrator\Desktop\record.pkl","wb")
pickle.dump(c,x)
x.close()

t=open("C:\\Users\\Administrator\\Desktop\\record.pkl","rb")
s=print(pickle.load(t))
