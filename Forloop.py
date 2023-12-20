name = ["Iman","Arnab","Raj","Rahul","Rohan","Rajesh"]

for names in name:
    print("My name is ",names)

# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

numbers = [1,2,3,4,5,6,7,8,9,10]



for number in numbers:
    print("Square of ",number,"is",number**2)                   # ** is used for exponentiation


num = list(range(1,10))

for nums in num:  # range is used to create a list of numbers
    print("square of ",nums,"is",nums**2)

# range(start,stop,step) is used to create a list of numbers

#it can be directly used inside for term in range(100,100)

# here's how you access elements of a list
animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

# You can also find the length of a list with len()

print("They're are this many things:", len(num))
print(type(num))

