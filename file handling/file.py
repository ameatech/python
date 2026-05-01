#f=open("a.txt", "x")
#creates file
#if you run again you will get file exist error
# r=open("a.txt","r")# default is r
# file=r.read()
# print(file)

# r mode can't create a file
# r=open("a.txt","w")
# file=r.write("now i am teaching isr")
# print(file)
#read then write in r+ mode
# r=open("a.txt","r+")
# print(r.read())
# print(r.tell())
# file=r.write("\nplease give me your attention")
# print(r.tell())
# f=open("a.txt", "w+")
# f.write("hi student")
# f.seek(0)
# print(f.read())
# f.close()
f=open("file.txt", "a")
x=f.write("hi there")

f.seek(0)#geting file handler at the beginning
print(x)
#print(f.read())
f.close()
