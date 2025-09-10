len("Alpha")
# checking the type of a data using "type" function
print(type("Alpha"))
print(type(23.04))
print(type(False))
print(type(3456))

# Type Conversion
print(int("123")+int("235"))
# str()
# float()
# int()
# bool()
print(type("abc")) #will give you <class 'str'>

# PAUSE 3

print("Number of letters in your name: " + str(len(input("Enter your name"))))
# # print(len(input("Enter Your Name")))
numbers_in_name=len(input("Enter your name"))
print(type(str(numbers_in_name)))