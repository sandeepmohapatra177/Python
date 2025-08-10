#Basic:
#list=data structure which can hold multiple values of multiple type
#array= multiple values with same type3

list_of_friends =["mitra","bal","mota","pamba","basa"]

list_of_friends.append("tutu") #append: add to the end
list_of_friends.insert(3,"bapu")
print(len(list_of_friends))
print(list_of_friends)

#list starts with 0,1,2.....
#insert gugu at 0 index
list_of_friends.insert(0,"gugu")
print(list_of_friends)

#iteration of a list
for friends in list_of_friends:
    print(friends)
    
#range
for i in range(1,5):
    print(i)



