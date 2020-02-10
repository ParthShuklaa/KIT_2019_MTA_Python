#Step1: Create a file object
#Step2: Read/Write operation
#Step3: Close file object

MyFile = open("MyData",'w')
MyFile.write("I m feeling Lucky")
MyFile.close()

myfile = open("MyData",'r')
Content = myfile.readline()
print(Content)
MyFile.close()