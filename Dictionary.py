#Dictionary in python
#it is an unorderd collection of elements
#Mutable collection:-(update/chnage) elements
#store as key- value pair
#it is represented by{}
#each entry consist of key(unique identifire)- value(data associated with identifire)
# syntax: my_dictionary={"key":"Value"/value}
#value depends it will be integer, string, boolean,float  etc

#metals_Density={"Aluminium":2.7,"Copper":9.0,"Bronze":8.4-8.7,"sterling silver":10.2-10.3}
metals_Density={"Aluminium":2.7,"Copper":(9.0),"Bronze":(8.4),"sterling_silver":(10.2)}
print(metals_Density)

sensor_node= {"id":1001,"active":True,"last_reading":24.5}
print(sensor_node)
student1={"math":80.5 ,"English":78.9, "physics":67.5}
print(student1.get("math"))
#print(student1("chemistry"))
print(student1.get("chemistry"))
print(student1.get("chemistry",89))

#membership operator in dictionary :- in and not in operator applicable on key
emp1={"id":121 ,"name":"saahil" ,"salary":12000}
print("id" not in emp1)
print("salary" in emp1)
print('course' in  emp1)

# Operations on Disctionary
#Upadate operation :- updating dictionary with new key with new value
emp={"id":1001,"name":"sanorita","salary":1000000}
emp["phon_number"]=9876789802
print(emp)
#now update (change) salary amount 100000 to 150000
emp['salary']=150000
print(emp)
print("\n")
sub1={"english":89.4, "Hindi":67 ,"IT":98}
sub2={"chem":45,"bio":66}
sub1.update(sub2)
print(sub2)

print("\n")
#update one key - value and other value
stationary1={'pen':10,'pencil':10,'earaser':5}
stationary2={'sketchpen':100,'sketchpencil':150}
stationary1.update(stationary2)
print(stationary1)
stationary2.update(stationary1)
print(stationary2)
#del():- Delete Function in dictionary
groceries1={'milk':25,'biscuit':30,'rice':23}
del groceries1['biscuit']
print(groceries1)
#pop :- pop function is used to pop out(Remove) any specific element with key
groceries1.pop("milk")
print(groceries1)
#keys can not be duplicate in a dictionary , if done it will only print it once
groceries1={"milk":65,"kokam":34,"rice":77,"milk":34}
print(groceries1)
print('\n')
#More Operation on dictionary
# 1) keys can not be a list, sets or dictionary => Because these are Mutable data structure.
# 2) keys allowed are str,int,float,tuple => Because these are Im-Mutable data structure.
# Example only for assigning a key
    # Ex1 1) List as key
# l1={[1,2,3]:3,[7,8,9]:5}
# print(l1)
        #Error : TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# List as key
# d1 = {[1,3,5]: 9, [1,2,1]: 4}
# print(d1)
        #Error : TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
#Integer as key
val1={1:"chocholate",5:"milky bar"}
print(val1)

#float as a key
per={84.9:"Rama",67.4:"shama"}
print(per)

#Boolean as a key
Dubs_mash_game={True:1,False:0}
print(Dubs_mash_game)
 #Tuple as Key
tup={(0,2,4):3,(1,3,5):8}
print(tup)

#sets as a key
# d1={{1,2,3}:4,{2,4,5}:3}
# print(d1)
# values as tuples
tuple1={'name':("iram","khan")}