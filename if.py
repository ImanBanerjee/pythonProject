answer = input("Are you indian?\n")

affirmative_list = ["yes", "y"]
negative_list = ["no", "n"]

# another way but no best every time is
# if "yes" in answer.lower(): # .lower() is used to convert the input to lower case
if answer.lower() in affirmative_list:
    print("Okay!")

# if answer in affirmative_list: (this is also good but not the best way)
   #  print("Okay!")
# if answer == "yes" or answer == "Yes" or answer == "YES": (one way to dao it)
    # print("Okay!")
elif answer.lower() in negative_list:
    print("Ohh thats sad but okay!")
#  answer == "no":
    # print("Ohh thats sad but okay!")
elif answer == "maybe":
    print("being sus huh?")
elif answer == "i dont know":
    print("you are not sure?")
elif answer == "who are you":
    print("I am a bot")
else:
    print("I dont understand answer - Yes/No/Maybe ")

# If - elif - else works like this and or can be used like above example but not directly or a bug will occur

