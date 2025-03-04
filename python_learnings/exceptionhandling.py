# try:
#     value = [1, 2, 3, 4]
#     reference = value[3]
#     print(reference)
# except IndexError:
#     print("Index out of bound")
# except ZeroDivisionError:
#     print("Zero division error")

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
finally: 
