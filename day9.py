'''
break---> this is used to exit from the loop, when we found the required value...
eg:
for j in range(1,10):
    print(j)
    if j == 5:
        break

lis_ = [8,11,19,26,]
for n in lis_:
    print(n)
    if n == 1:
        break

continue--->        

for j in range(1,10):
    if j == 5:
        continue
    print(j)

lis_ = [8,11,19,26,]
for n in lis_:
    if n == 11:
        continue
    print(n)
pass---> this is called as space holder , incase any statement like (if, for, else, elif...)this should be
         complete, if not we will get indentation error to avoid this we are using pass

for j in range(1,100):
    pass

else -- for:-
-----------
it will fall back to else block, when all loops are completed

for m in range(1,11):
    print(m)
else:
    print("else block")
    
while---> this is a combination of for and if statements , if we didn't end the loop in proper way it will
          run upto the memory space in the system become empty

num = 1
while num<11:
    print(num)
    num += 1

user_in = int(input("Enter the limit: "))
num_1 = 0
num_2 = 1
print(num_1, num_2, end=" ")
for v in range (user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end =" ")







