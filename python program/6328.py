#为了提取70600开头的测试行的数据。


i_vbat=[]
f=open(r"C:\Users\Administrator\Desktop\FT1D_R0_All_10110191539401A_02202018_072309.txt")
for each_line in f:
    if each_line[:6]==" 70601":
        i_vbat.append(each_line)

            
file_name_testname='AVDD_DVDD18_CUR'+'.txt'
a=open(file_name_testname,'w')
a.writelines(i_vbat)
a.close()
f.close()
















