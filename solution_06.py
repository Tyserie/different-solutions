'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]
'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

#Empty lists
list0 = []
list2 = []

#Lenght of unsorted_list == 5
lastlst = len(unsorted_list)

#Lenght of unsorted_list - 1 == 4
x = lastlst - 1

#Find last element in unsorted_list. Means 5 - 1 == 4 which lids to ('sixth_element', 3)
lastelemt = unsorted_list[x]

#Show what is inside ('sixth_element', 3) on index 1 == number 3
value = lastelemt[1]

#Loop through unsorted_list
for i in unsorted_list:
    value = lastelemt[1]                     #Store whats on index 1 in last element(Tuple)
    value2 = lastelemt[0]                    #Store whats on index 0 in last element(Tuple)
    list0.insert(0, value)                   #Insert Value into list0
    list2.insert(0, value2)                  #Insert Value2 into list2
    zipped = zip(list0, list2)               #Zip the list0 and list2 so the value on index 1 is now on index 0
    lst = list(zipped)                       #Result of zip
    lst.sort()                               #Sort the zipped list based on value on index 0 (number)
    x = x - 1                                #Lower lenght of unsorted list by 1
    lastelemt = unsorted_list[x]             #Last element lookup on new position (- 1)
#    print(value)

for x in range(0, len(lst) - 0):             #Go 0 to last tuple
    lst[x] = (lst[x][1], lst[x][0])          #Swap the possition of key and value in Tuple, but keeps the sorting based on number in Tuple
print(lst)
