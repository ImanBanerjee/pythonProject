# explain what a function is: a function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function. A function can return data as a result.

def greet(names):  # names is a parameter
    # return "Hello, " + name + " how are you doing today?" (one way to do it)
    return f"Hello, {names} how are you doing today?"  # (another way to do it)


name = input("Enter your name: ")

print(greet(name))


def friends(word_1, word_2):  # word_1 and word_2 are parameters
    return f"{word_1} is friends with {word_2}"  # return is used to return the value


word_1 = input("Enter your name: ")  # word_1 and word_2 are arguments
word_2 = input("Enter your friends name: ")  # word_1 and word_2 are arguments

if word_1 == word_2:  # == is used to compare two values
    print("You are friends with yourself")  # if the condition is true then this will be printed
elif word_1 != word_2:  # != is used to compare two values
    print(friends(word_1, word_2))  # if the condition is true then this will be printed
else:
    print("Something went wrong")  # if the condition is false then this will be printed

    def age_calculator(year_of_birth):
        age = 2023 - year_of_birth
        return f"You are {age} years old"

    dob = int(input("Enter your year of birth: "))
    print(age_calculator(dob))

    def age_in_dog_years(age):
        dog_years = age * 7
        return f"You are {dog_years} years old in dog years"

    print(age_in_dog_years(2023 - dob))
