import sys
# # Iterators
# An object that enables a programmer to traverse a container, 
# particularly lists, without having to store all of the 
# different items in that container in memory.

# # Generator
# A routine that can be used to control the iteration behavior 
# of a loop. A generator is very similar to a function that 
# returns an array.

def how_iterator_works():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    y  = map(lambda i: i**2, x)
    
    for i in y:
        print(i)
    
    print("Using while implement for loop.")
    
    while True:
        try:
            value = next(y)
            print(y)
        except StopIteration:
            print('Done')
            break
    
def dive_into_range():
    # # range()
    x = range(1, 11)
    
    print(x)
    print(next(x))  # 'range' object is not an iterator
    print(next(iter(x)))

def iterator_Class():
    class Iter:
        def __init__(self, n):
            self.n = n
    
        def __iter__(self):
            self.current = -1
            return self
    
        def __next__(self):
            self.current +=1
            if self.current >= self.n:
                raise StopIteration
    
            return self.current
    
    x = Iter(5)
    for i in x:
        print(i)
    
    itr = iter(x)
    print(next(itr))

# def gen(n):
#     for i in range(n):
#         yield i

# def gen():
#     yield 0
#     print('Pause 0')
#     yield 1
#     print('Pause 1')
#     yield 2
#     print('Pause 2')
#     yield 3
#     print('Pause 3')
#     yield 4
#     print('Pause 4')

# x = gen()
# print(next(x))
# print('-' * 10)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# Read large file with small memory
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

# Generator comprehension
x = (i for i in range(10))
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))