nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

my_list2 = [n for n in nums]
# print(my_list2)

# for n in nums:
#     n = n*n
#     my_list.append(n)
# print(my_list)

my_list2 = [n*n for n in nums]
# print(my_list2)

"""map and lambda: map runs everything is the list through a certain function and lambda is an anonymous function"""

my_list3 = map(lambda n: n*n, nums)
print(list(my_list3))


# I want  'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)
my_list = [n for n in nums if n%2 == 0]
print(my_list)

my_list3 = filter(lambda n: n%2 == 0 , nums)
print(list(my_list3))

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((num,letter))
# print(my_list)
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# any data type can be zipped
# any data type can apply to comprehensions
names = ['bruce','clark','peter','logan','wade']
heros = ['batman','superman','spiderman','wolverine','deadpool']
print(dict(zip(names,heros)))

# I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'peter'}
print(my_dict)

# set() is just list with unique value
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = (n for n in nums)
print(set(my_set))


# generator expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_gen = (n*n for n in nums)  # use parenthesis
print(sorted(my_gen))
"""how to print out in vertical way"""



