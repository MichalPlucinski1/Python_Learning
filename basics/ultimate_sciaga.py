




Tuple = ('bob', 123, 'Lisa', ('another list')) # immutable and no append

List = ['bob', 123, 'Lisa', ['another list']] # well... list

Set = {1,2,3,'test'}  # no duplicates

Dictionary = {'name':'Bob',123:'test'} # key, value

Dictionary['new key'] = 1.5


print(Dictionary['name'])

user_name = 'srname'

user_information = f'{user_name} is {10 + 20} years old'

# we can make set of a list, this will delete duplicates
l2 = []
size = 10
for i in range(size):
    l2.append(i)


simple_list = [i for i in range(0,11) for j in ('a','b','c')]

complex_list = [f'{j}{i}' for i in range(0,11,1) for j in ('a','b','c') if i == 1]

print('simple list:')
print(simple_list)

print('complex list:')
print(complex_list)

my_it = iter(simple_list)
print(next(my_it))

#lambda

double_value = lambda num: num*2


#fast sorting

random_list = [('Anna', 25), ('Paul', 40), ('Lisa', 40)]
sorted_list = sorted(random_list, key = lambda user_tuple: user_tuple[1])

print(sorted_list)




board = [ f'{j}{i}' for i in range(1,6) for j in {'A', 'B', 'C', 'D', 'E'} if f'{j}{i}'!= 'C3']

board = sorted(board, key = lambda s: s[0])

print(board)




spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'





spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
spam.setdefault('color', 'white')


"""
isalpha() Returns True if the string consists only of letters and isn’t blank

isalnum() Returns True if the string consists only of letters and numbers and is not blank

isdecimal() Returns True if the string consists only of numeric characters and is not blank

isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank

istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters


join and split
str.split(' ')
"""



# map - changes values with a function inside of a iterable

my_list = [1,2,3,4,5]

def power_function(num):
    return num**2

m = map(power_function, my_list)

print("list(m)", list(m))

#print(list(map(lambda num: num ** 2, my_list)))

l3 = list(m)

def get_below_4(num):
    if num < 4:
        return True
    return False

print(list(filter(get_below_4, my_list))) # also can be lambda
#print(list(filter(lambda num: num < 4, my_list))) # also can be lambda





import random

fnum =  5 # random.randint(10,100) #maszyny
snum =  15 #random.randint(20,50) #ile zadań

with open("./data.txt","w") as file: # can be a, for append
    file.write(str(fnum)+"\n"+str(snum))
    for i in range(snum):
        file.write("\n"+str(random.randint(1,10))) #czasy wykonań zadań

with open("../dane/m10n200.txt","r") as file:
        M = int(file.readline().strip())                    #liczba procesorów/maszyn
        file.readline()
        Proceses = [int(line.strip()) for line in file]  


with open('test.txt') as file:
     for line in list(file):
          print(line)