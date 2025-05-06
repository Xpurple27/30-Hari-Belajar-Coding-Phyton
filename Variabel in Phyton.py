#First day learn about coding

#Variabel = A variable is a value that can change within a range ( string, integer, float, boolean)
#String = character
#Integer = number
#Float = number with decimal
#Boolean = True or False (using If)
#If = conditional clause

#String (the value will be count as a char)
name = input(f"Hi ! What is your name ? : ")
print(f"Hi {name}")
food = input(f"Whats your Favorit Food ? : ")
print(f"yes {food} looks delicius ")

#Integer (u can use operation to ur integer value)
age = int(input(f"how old are you ? : "))
print(f"ohh, you {age} years old")
print(f"your age next years is {age + 1}")
sibling = int(input(f"how many ours siblings ? "))
print(f"woww you have {sibling} siblings")

#Float (u just can use decimal when use float)
tall = float(input("how tall are you ? :"))
print(f"nice, your tall is {tall} feet")
gpa = float(input("what about your gpa ? : "))
print(f"your gpa is {gpa}")

#Boolean and If (conditional clause)

gender = input(f"whats your gender male / female ? : ")

if gender == "male" :
    print(f"Nice too meet you Mr {name}")
elif gender == "female":
    print(f"Nice too meet you Mrs {name}")
else :
    print(f"Nice too meet you Mr/Mrs {name}")
