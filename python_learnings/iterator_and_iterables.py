my_list = [1, 2, 3]
my_string = "Hello"

# Checking if it's iterable
print(hasattr(my_list, '__iter__'))   # True
print(hasattr(my_string, '__iter__'))  # True


# An iterable is any Python object that can return an iterator.
# It has a special method called __iter__(), which returns an iterator.


# An iterator is an object that produces the next value in a sequence when next() is called. It must implement:

# __iter__() → returns the iterator itself.

# __next__() → returns the next value in the sequence.

my_iter = iter(my_list)  # Converting list to iterator

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # Raises StopIteration


# Custom iterator
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


counter = Counter(1, 5)
for num in counter:
    print(num)  # 1 2 3 4

# Custom Iterable: It needs to implement just __iter__ and
# return a iterator which has __iter__ and __next__ or just implement itself __iter__ and __next__


class CounterIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return CounterIterator(self.start, self.end)  # Returns a new iterator


class CounterIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Iterator should return itself

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Stop when end is reached
        value = self.current
        self.current += 1
        return value


# Using the custom iterable
counter = CounterIterable(1, 5)

for num in counter:
    print(num)  # Output: 1 2 3 4


# Another approach is to make the iterable class also serve as its own iterator by implementing
# both __iter__() and __next__()

class Counter:
    def __init__(self, start, end):
        self.start = start
        self.current = start
        self.end = end

    def __iter__(self):
        self.current = self.start  # Reset iterator each time
        return self  # The class itself acts as an iterator

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# Using the custom iterable
counter = Counter(1, 5)

for num in counter:
    print(num)  # Output: 1 2 3 4

# Reusing the iterable in another loop
for num in counter:
    print(num)  # Output: 1 2 3 4 (it resets)

# Custom Iterable Using Generators


class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for num in range(self.start, self.end):
            yield num  # Yield acts like __next__()


# Using the custom iterable
counter = Counter(1, 5)

for num in counter:
    print(num)  # Output: 1 2 3 4
