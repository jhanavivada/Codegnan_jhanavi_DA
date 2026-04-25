'''

File Handling---> fille handler is an object of file to maintain several functions of file such as creating,   
reading, writing and update also deleting the file
How to open a file
1. open()--->This open ()function takes 2 parameters and in this we have to close the file by calling close() function after program..
1file name
2mode

2. with open()--->Modes ("r", "w", "a", "x", "t")
1. "r"(read)->To read the file we will use  this mode and if the file doesnt exist, it will give the error

any = open("dammi.txt","r")
print(any.read())

2. "w"(write mode)->to write the text into the file we will use this mode and it will create the file if it doesn't exists
file = open("dummy.txt","w")
file.write("this is hema")
file.close()


3."a"(append)->to add the text into the file this is used and it will create the file if it dosen't exists
               ->it will write text at the end
file = open("dummy.txt","a")
file.write("This is line 4")
file.close()

4. "x"(create)->this is used to create the file, but this is already in the system it raise an error

To read a file
------------
1.read()-->this method can read the entire file chunk by chunk
any = open("dammi.txt","r")
print(any.read(1000))
any.close()

2.readline()-->
any = open("dammi.txt","r")
print(any.readline(9))
any.close()

3.readlines()->this method can read the entire file and return into the list with each line into one index in the list

any = open("dammi.txt","r")
print(any.read())
print(any.readline())
print(any.readlines())
any.close()

