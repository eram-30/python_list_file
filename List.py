#List in python
# list ios atype of variable in python
name="Johan"
age=20
percent=82.90

student=["Johan",20,8.5]
print(student)
print(type(student))
student1=["sam",[10,20,[2,3],30]]
print(student1)
print("\n")
days_of_week=["Mon","Tues","Wed","Thurs","Fri","Sat","Sunday"]
#Index value=   0     1      2      3       4     5     6
# printing value using index value
print(days_of_week[6])
print(days_of_week)
print("Last Day of week is",days_of_week[5])
#using f-string we print value of sunday
print(f"Tommorow is Holiday because of {days_of_week[6]}")

#Length of List  string check
print("Length of List:" ,len(days_of_week))
#check List value via Negative(-) index number
print(f"The Days of week is{days_of_week[-2]}")
print("\n")
#List Operations:- Slicing,concatination/concat,repeat,append,insert
#list operation:- Slicing(start value,End value,jump value)
list1=[3,8,1,0,4,9,7,3,6]   #counting via Index number
print(list1[1:6:1])
print(list1[2:8:2])
print(list1[2:7:2])
print(list1[1:5:1])
#list operation:- Concatination/concat(joining of string)
list1=[1,7,2]
list2=[0,5]
print(list1+list2)
#list operation:- Repetition of list(* using multiplication symbol repeatv multiple times)
print(list1*5)
print(list2*3)
#list operation:-Append in list using variabal Name.append(){means to add item in the end of list}
fruits=["Mango","Banana","Apple"]
#print(append("strawberry"))
fruits.append("strawberry")
#now add new variable
update_list1=fruits
#Now print old list of fruit
print(fruits)
# another example of append list
fruits.append("Blueberry")
update_list1=fruits
print(fruits)
print("\n")
#list operation :- insert() Add an element before the specified index
boys_name=["Huzaif","Ali","Saad"]
print("Boyes names are:", boys_name)
#insert a item in list in last:-
#listname.insert(index,item)
boys_name.insert(3,"Osama")
print(boys_name)
#insert a item in list in first position
boys_name.insert(0,"Kalim")
print(boys_name)
print("\n")
#List Operations:-For Removing items
# Extends #Remove #Pop

