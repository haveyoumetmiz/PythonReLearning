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


"hello world".capitalize()
# Output: 'Hello world'
"HeLLo".casefold()
# Output: 'hello'
"hi".center(10, "*")
# Output: '****hi****'
"hello".encode()
# Output: b'hello'
"hello.py".endswith(".py")
# Output: True
"hello\tworld".expandtabs(4)
# Output: 'hello   world'
"pineapple".find("apple")
# Output: 4
"Hello {}, your score is {}".format("Mizu", 99)
# Output: 'Hello Mizu, your score is 99'
data = {"name": "Zu", "age": 22}
"Name: {name}, Age: {age}".format_map(data)
# Output: 'Name: Zu, Age: 22'
"hello".index("e")
# Output: 1
"Python3".isalnum()
# Output: True
"Python".isalpha()
# Output: True
"Hi123".isascii()
# Output: True
"123".isdecimal()
# Output: True
"123".isdigit()
# Output: True
"my_var1".isidentifier()
# Output: True
"hello".islower()
# Output: True
"²34".isnumeric()
# Output: True
"Hello!\n".isprintable()
# Output: False
"   ".isspace()
# Output: True
"Hello World".istitle()
# Output: True
"HELLO".isupper()
# Output: True
"-".join(["a", "b", "c"])
# Output: 'a-b-c'
"Hi".ljust(5, ".")
# Output: 'Hi...'
"HELLO".lower()
# Output: 'hello'
"   Hello".lstrip()
# Output: 'Hello'
trans = str.maketrans("ae", "12")
"apple".translate(trans)
# Output: '1ppl2'
"email@example.com".partition("@")
# Output: ('email', '@', 'example.com')
"hello world".replace("world", "Zu")
# Output: 'hello Zu'
"hello hello".rfind("lo")
# Output: 9
"banana".rindex("a")
# Output: 5
"Hi".rjust(5, "*")
# Output: '***Hi'
"hello@world@com".rpartition("@")
# Output: ('hello@world', '@', 'com')
"apple,banana,grape".rsplit(",", 1)
# Output: ['apple,banana', 'grape']
"hello   ".rstrip()
# Output: 'hello'
"one,two,three".split(",")
# Output: ['one', 'two', 'three']
"line1\nline2".splitlines()
# Output: ['line1', 'line2']
"sunshine".startswith("sun")
# Output: True
"  hey  ".strip()
# Output: 'hey'
"HeLLo".swapcase()
# Output: 'hEllO'
"hello world".title()
# Output: 'Hello World'
"hello".upper()
# Output: 'HELLO'
"42".zfill(5)
# Output: '00042'


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

#Lists
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
# Output: ['apple', 'banana', 'cherry']

fruits = ["apple", "banana"]
fruits.clear()
print(fruits)
# Output: []

fruits = ["apple", "banana"]
new_fruits = fruits.copy()
print(new_fruits)
# Output: ['apple', 'banana']

nums = [1, 2, 2, 3, 2]
print(nums.count(2))
# Output: 3

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)
# Output: [1, 2, 3, 4]

colors = ["red", "blue", "green"]
print(colors.index("blue"))
# Output: 1

numbers = [1, 3, 4]
numbers.insert(1, 2)
print(numbers)
# Output: [1, 2, 3, 4]

items = [10, 20, 30]
items.pop()
# Output: 30
print(items)
# Output: [10, 20]

nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)
# Output: [1, 3, 2]

letters = ['a', 'b', 'c']
letters.reverse()
print(letters)
# Output: ['c', 'b', 'a']

scores = [5, 2, 9, 1]
scores.sort()
print(scores)
# Output: [1, 2, 5, 9]

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)
# Output: ['apple', 'banana', 'cherry']

words = ["banana", "kiwi", "apple", "cherry"]
words.sort(key=lambda word: word[-1])
print(words)
# Output: ['banana', 'apple', 'kiwi', 'cherry']

words = ["banana", "Apple", "cherry", "apple"]
words.sort(key=str.lower)
print(words)
# Output: ['Apple', 'apple', 'banana', 'cherry']

words = ["banana", "kiwi", "apple", "cherry", "ananas", "mango", "lemon", "orange", "lime", 
         "grapefruit", "grape", "blueberry", "melon", "strawberry", "raspberry", "blackberry", "pear"]

# Separate the berry gang and non-berry gang
berry_words = []
non_berry_words = []

for word in words:
    if "berry" in word:
        berry_words.append(word)
    else:
        non_berry_words.append(word)

# Sort 'em both like a good playlist
berry_words.sort()
non_berry_words.sort()

# Merge into the ultimate fruit list
final_list = berry_words + non_berry_words

print(final_list)




#tuple
t = (1, 2, 3, 2, 4, 2)

print(t.count(2))   # Output: 3
print(t.index(3))   # Output: 2


#set
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))                # {1, 2, 3, 4, 5}
print(a | b)                     # same as union

print(a.intersection(b))         # {3}
print(a & b)                     # same

print(a.difference(b))           # {1, 2}
print(a - b)                     # same

print(a.symmetric_difference(b)) # {1, 2, 4, 5}
print(a ^ b)                     # same

print(a.issubset(b))             # False
print(a.issuperset(b))           # False
print(a.isdisjoint(b))           # False



nums = [3, 1, 4]
new_nums = sorted(nums)
print(new_nums)
# Output: [1, 3, 4]
print(nums)
# Output: [3, 1, 4]

len([1, 2, 3])
# Output: 3

"apple" in ["apple", "banana"]
# Output: True

items = [1, 2, 3]
del items[1]
print(items)
# Output: [1, 3]



#find the Largest Number in a List

numbers = [12, 56, 34, 78, 89, 23, 45]
largest_number = max(numbers)
print("The largest number is:", largest_number) # The largest number is: 89

#Check if a String is a Palindrome
word = "madame"
if word == word[::-1]:
    print("palindrome")
else:
    print("Not") # Not a palindrome

#Find the Common Elements in Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print("Common elements:", common_elements) # Common elements: {4, 5}

#Reverse a String Without Using Reverse Method

s = "Hello, World!"
reversed_s = ''.join(reversed(s))
print("Reversed string:", reversed_s) # Reversed string: !dlroW ,olleH


#Count Occurrences of Each Character in a String

text = "hello there, how are you?"
char_count = {}

for char in text: 
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character counts:", char_count) # Character counts: {'h': 2, 'e': 3, 'l': 2, 'o': 3, ' ': 6, 't': 1, 'r': 1, ',': 1, 'w': 1, 'a': 1, 'y': 1, '?': 1}


sentence = input("Enter a sentence: ")
words = sentence.split()
visited = []

for i in range(len(words)):
    if words[i] not in visited:
        count = 0
        for j in range(len(words)):
            if words[i] == words[j]:
                count += 1
        visited.append(words[i])
        print(words[i], ":", count)
             
#Remove Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("List without duplicates:", unique_numbers)
