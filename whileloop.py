# i = 1
#
# while(i <= 50):
#     print("Noob")
#     i = i / 1

# i = int(input("Enter a number: "))
#
# while(i <= 50):
#     i = int(input("Enter a number: "))
#     print("Noob")
#
# print("You are not a noob anymore!")
#
# i = 50
# while(i > 0):
#     print(i)
#     i = i - 1
# else:
#     print("Done with all the work")
# else inside while

i = int(input("Enter a number: "))

match i:

    case 0 if i == 0:
        print("Zero")
    case 1 if i == 1:
        print("One")
    case _ if i != 0:
        while (i <= 50):
            i = int(input("Enter a number: "))
            if i <= 50:
                print("Noob")


    case _:
        print("You are not a noob anymore!")