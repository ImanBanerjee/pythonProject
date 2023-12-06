def uppercase_and_reverse(text):
    uppercase_text = text.upper()
    return uppercase_text[::-1]
print(uppercase_and_reverse("hello"))

text = input("Enter a string: ")

text2 = uppercase_and_reverse(text)

print(f"Uppercase and reversed: {text2}")