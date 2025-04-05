print("Hello, World!") #printing a string
s = "hello"
print(s[::-1]) #reversing a string
print(s[2:4]) #slicing a string
print(s[0:5:2]) #slicing a string with step
print(s[1]) #printing the character of a string
print(s[1:]) #slicing a string from index 1 to end
# Changing case
p = "Hello World"
print(p.upper())       # HELLO WORLD
print(p.lower())       # hello world
print(p.title())       # Hello World
print(p.capitalize())  # Hello world
print(p.swapcase())    # hELLO wORLD
print(p.replace("Hello", "Hi")) # replacing a string
print(p.count("o"))   # 2 (count of 'o')
print(p.find("o"))    # 4 (index of first 'o')
print(p.index("o"))   # 4 (index of first 'o')
print(p.rfind("o"))   # 7 (index of last 'o')
print(p.rindex("o"))  # 7 (index of last 'o')
print(p.startswith("Hello")) # True
print(p.endswith("World"))   # True
print(p.startswith("World")) # False
print(p.endswith("hello"))   # False
print(p.startswith("Hello", 0, 5)) # True (within range)
print(p.endswith("World", 6, 11)) # True (within range)
print(p.startswith("Hello", 0, 4)) # False (within range)   
print(p.endswith("World", 0, 5)) # False (within range)
print(p.split())      # ['Hello', 'World']
print(p.split("o"))   # ['Hell', ' W', 'rld']
print(p.split("o", 1)) # ['Hell', ' World'] (split at first 'o')
print(p.split("o", 2)) # ['Hell', ' W', 'rld'] (split at first two 'o')
print(p.split("o", 0)) # ['Hello World'] (no split)
print(p.split("o", -1)) # ['Hell', ' W', 'rld'] (split at all 'o')
print(p.split("o", -2)) # ['Hell', ' W', 'rld'] (split at all 'o')  


# Checking string properties
p = "Hello World"
print(p.isalpha())     # False (because of space)
print("Hello".isalpha())  # True
print("123".isdigit())    # True
print("hello123".isalnum()) # True
print("   ".isspace())     # True
print("Hello".isupper())   # True
print("hello".islower())   # True
print("Hello".istitle())  # True
print("hello".istitle())  # False
print("HELLO".isupper()) # True
print("hello".islower()) # True


# String concatenation
a = "Hello"
b = "Mizu"
print(a + " " + b)   # Hello Mizu
print(a + b)         # HelloMizu
print(a + " " + b + "!") # Hello Mizu!


# String repetition
print(a * 3)   # HelloHelloHello
print(b * 2)   # MizuMizu
print(a * 0)   # (empty string) 
print(b * -1)  # (empty string)
print(a * -1) # (empty string)


# Membership testing
print("H" in a)      # True
print("z" in b)      # True
print("Z" in b)      # False
print("Hello" in a)  # True
print("Mizu" in b)   # True
print("Mizu" in a)   # False
print("Mizu" not in a) # True
print("Hello" not in b) # True
print("H" not in a)  # False
print("z" not in b)  # False

# Stripping whitespaces
s = "   Mizu   "
print(s.strip())     # Mizu
print(s.lstrip())    # Mizu___
print(s.rstrip())    # ___Mizu
print(s.strip(" Mizu")) # (empty string) (removes all characters in " Mizu")
print(s.strip(" M")) # ___Mizu (removes all characters in " M")
print(s.strip("M")) # ___Mizu (removes all characters in "M")


# Splitting and joining
msg = "Python is fun"
words = msg.split()   # ['Python', 'is', 'fun']
print(words)
print("-".join(words)) # Python-is-fun
print(" ".join(words)) # Python is fun
print("".join(words)) # Pythonisfun
print(" ".join(["Hello", "World"])) # Hello World
print(" ".join(["Hello", "World", "Python"])) # Hello World Python
print(" ".join(["Hello", "World", "Python", "is", "awesome"])) # Hello World Python is awesome
print(" ".join(["Hello", "World", "Python", "is", "awesome", "and", "fun"])) # Hello World Python is awesome and fun


# Replace and find
text = "I love Python"
print(text.replace("Python", "coding"))  # I love coding
print(text.find("love"))  # 2 (index)
print(text.find("Java"))  # -1 (not found)
print(text.index("love")) # 2 (index)
print(text.index("Java")) # ValueError (not found)


# String formatting (f-string)
name = "Mizu"
age = 21
print(f"My name is {name} and I am {age} years old.")
print(f"{name} is {age} years old.")
print(f"Hello, {name}! You are {age} years old.")
print(f"{name} is a student.")

# String formatting (format method)
name = "Mizu"
age = 21
print("My name is {} and I am {} years old.".format(name, age))
print("{} is {} years old.".format(name, age))

vowels = "aeiou"
count = sum(1 for c in s.lower() if c in vowels)
print(f"Number of vowels in '{s}': {count}")
# Counting vowels in a string
s = "hello world"


n = 123
total = sum(int(d) for d in str(n))
print(f"Sum of digits in {n}: {total}")
n = 123                # A number
# Step 1: Convert to string
n_str = str(n)         # '123'
# Step 2: Loop through each character in the string
total = 0
for d in n_str:        # d will be '1', then '2', then '3'
    digit = int(d)     # Convert '1' -> 1, '2' -> 2, etc.
    total += digit     # Add it to the running total
print(total)           # Output: 6













vowels = "aeiou"
count = sum(1 for c in s.lower() if c in vowels)
