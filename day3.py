'''vowel_con = input("Enter a letter:")
if vowel_con in "AEILOaeiou":
    print("vow")
else:
    print("COn")
Time_aday = input("Enter 24 hours time: ")
Parts_ = Time_aday.split(":")
hours_ = int(Parts[0])
Min_ = int(Parts_[1])
if hours_ >=13 and Min_ < 60:
    print(f"{Time_aday} convert into {hours_ - 12}:{Min_}pm")
else:
    print(f"you have entered normal or min are incorrect")

list---> Different datatype inside the[] , which are separated by ,
eg---> [1,"Name,",[1,2,"Janu"]]

List_1 = [1,2,3,"python",[1,2,["python","java"],"Language"]]
print(List_1[4][2][0][3])

methods of list
---------------
append()--- This method is used to add new items into list,it will only go for the last index of the list
syntax:- variable_name.append(iteam)

extend():- this method is used to add items to list in the last index, where each iteam or substring is
each index in the list
syntax:- variable_name.extend(iteam)

remove():- this method will delete the iteam or a value directly
syntax:-variable_name.remove(iteam)

pop():- this method will delete the item or value based on index position
syntax:-variable_name

mutable:-                                             immutable:-
i can directly modify on that particular variable     i cann't modify directly
                                                      on the variable

List_2 = [1,2,3,4]
print(List_2)
List_2.append([11,24,23])
print(List_2)

List_3 = [11,8,3]
print(List_3)
List_3.append(23)
List_3.extend("janu")
print(List_3)

List_4 = [23,45,23,"janu"]
List_4.remove("janu")
print(List_4)

List_3 = [11,8,3]
print(List_3)
List_3.append(23)
List_3.extend("janu")
print(List_3)
List_3.remove(23)
print(List_3)

List_3 = [11,8,3]
List_3.pop(0)
print(List_3)
'''
List_1 = [11,23,34,"jhanavi",[13,24,["ammu","codegnan"],"apple"]]
print(List_1[4][2][0])




