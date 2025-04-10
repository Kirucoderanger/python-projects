"""The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
Add an item to the end of the list. Similar to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, 
so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, 
a.pop() removes and returns the last item in the list. 
It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Similar to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Similar to a[:]."""

#An example that uses most of the list methods:
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting at position 4
6
fruits.reverse()
fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting at position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()
#Using Lists as Stacks¶
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack
#Using Lists as Queues¶
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival
#List Comprehensions¶
squares = []
for x in range(10):
    squares.append(x**2)

squares

squares = list(map(lambda x: x**2, range(10)))
#or, equivalently:

squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

#and it’s equivalent to:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
#File "<stdin>", line 1
[x, x**2 for x in range(6)]
     
#SyntaxError: did you forget parentheses around the comprehension target?
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

#List comprehensions can contain complex expressions and nested functions:


from math import pi
[str(round(pi, i)) for i in range(1, 6)]
#. Nested List Comprehensions¶
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
"""The following list comprehension will transpose rows and columns:

>>>
[[row[i] for row in matrix] for i in range(4)]

As we saw in the previous section, the inner list comprehension is evaluated in the context of the for that follows it, so this example is equivalent to:

>>>
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

which, in turn, is the same as:

>>>
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed

In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:

>>>
list(zip(*matrix))


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

>>>
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

>>>
{x: x**2 for x in (2, 4, 6)}

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

>>>
dict(sape=4139, guido=4127, jack=4098)


5.6. Looping Techniques
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

>>>
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)



When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

>>>
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)




To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

>>>
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))




To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

>>>
for i in reversed(range(1, 10, 2)):
    print(i)






To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

>>>
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)







Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

>>>
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)





It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

>>>
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data"""