print("\n------------task 1-------------\n")

def swap(lst,i,j):
    if i > len(lst)-1 or i > len(lst)-1:
        raise IndexError
    
    lst[i], lst[j] = lst[j], lst[i]


    return lst

my_list = [1,2,3,4,5,6]
print(swap(my_list, 5,2))


print("\n------------task 2-------------\n")

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

def digit_filter(lst):
    result = [item for item in lst if item.isalpha()]
    return result


print(digit_filter(l33t))

print("\n------------task 4 -------------\n")

# Write a program that takes a list of numbers and returns a 
# new list containing only the even numbers.
# use list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_num = [num for num in numbers if num% 2 == 0]

print(even_num)


print("\n------------task 5 -------------\n")

# Write a program that takes a list of numbers and
#  returns a new list containing the squares of each number.
# use list comprehension
numbers = [1, 2, 3, 4, 5]
sqr_numbers = [num**2 for num in numbers]
print(sqr_numbers)

print("\n------------task Bonus -------------\n")
# Create a list of tuples where each tuple contains a
#  number and its factors using list comprehension.
numbers = [1, 2, 3, 4, 5] #----> [(1, [1]), (2, [1, 2]), (3, [1, 3]), (4, [1, 2, 4]), (5, [1, 5])]


factor_lst2 = [(j,[i for i in numbers if j % i == 0]) for j in numbers]

print(factor_lst2)

print("\n------------cartesian product -------------\n")

# Write a Python program that takes two lists and returns a list of tuples, 
# where each tuple is a pair of elements, one from each input list, representing the cartesian product of the two input lists.
# For example, if the input lists are [1, 2, 3] and ['a', 'b'], 
# the output should be [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')].

lst_1 =[1, 2, 3]  
lst_2 = ['a', 'b']

# cartesian = [[i for i in lst_1] , j for j in lst_2]
cartesian = []
tup = ()
for i in lst_1:
    for j in lst_2:
        element = [i,j]
        tup = tuple(element)
        cartesian.append(tup)
    

cartesian_comp = [(j,i) for j in lst_1 for i in lst_2]
print(cartesian)
print(cartesian_comp)