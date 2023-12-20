numbers = range(1, 101)

for number in numbers:
    if number % 2 == 0:
        print(number,"is even")
    elif number % 2 != 0:
        print(number,"is odd")
    else:
        print(number,"is neither even nor odd")



names = ["Iman","Arnab","Raj","Rahul","Rohan","Rajesh"]

for name in names:
    print(name)
    for i in name:
        print(i)