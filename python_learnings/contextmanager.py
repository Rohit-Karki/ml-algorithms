# Writing context manager using objects
# Similar to the open() function we will write the FileWriter() class
class FileWriter:
    def __init__(self, fileName):
        self.fileName = fileName

    def __enter__(self):
        self.file = open(self.fileName, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, trace):
        self.file.close()

# with FileWriter("example.txt") creates a new FileWriter object and calls __enter__().
# The __enter__() method initializes the resource you want to use.
# In this case, it opens a text file. It also has to return the descriptor of the resource, so it returns the opened file.
# The as file assigns the file to a variable file.
# Finally, the code you want to run with the acquired resource is placed in the with block after the colon.
# As soon as this code finishes execution, the __exit__() method is automatically called. In this case, it closes the file.


with FileWriter("stopwords.txt") as f:
    print(f.read().replace('\n', ' ').split())


class BulletedList:
    def __init__(self):
        self.indent_level = 0

    def __enter__(self):
        self.indent_level += 1
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.indent_level -= 1

    def bullet_type(self):
        bullet_types = ["o ", "- ", "* "]
        return bullet_types[self.indent_level % 3]

    def item(self, text):
        print("  " * self.indent_level + self.bullet_type() + text)


with BulletedList() as bp:
    bp.item("Dessert")
    with bp:
        bp.item("Apple Pie")
        with bp:
            bp.item("Apples")
            bp.item("Cinamon")
            bp.item("Sugar")
            bp.item("Flour")
            bp.item("Eggs")
    with bp:
        bp.item("Hot Chocolate")
        with bp:
            bp.item("Milk")
            bp.item("Chocolate powder")
            bp.item("Cream")
