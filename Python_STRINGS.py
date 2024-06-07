#Example:
print("Hello")
print('Hello')
#Example:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#Example:
a = "Hello"
print(a)
#Example:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Example:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#Example:
a = "Hello, World!"
print(a[1])
#Example:
for x in "banana":
  print(x)
#Example:
a = "Hello, World!"
print(len(a))
#Example:
txt = "The best things in life are free!"
print("free" in txt)
#Example:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#Example:
txt = "The best things in life are free!"
print("expensive" not in txt)
#Example:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#Example:
b = "Hello, World!"
print(b[2:5])
#Example:
b = "Hello, World!"
print(b[:5])
#Example:
b = "Hello, World!"
print(b[2:])
#Example:
b = "Hello, World!"
print(b[-5:-2])
#Example:
a = "Hello, World!"
print(a.upper())
#Example:
a = "Hello, World!"
print(a.lower())
#Example:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#Example:
a = "Hello, World!"
print(a.replace("H", "J"))
#Example:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#Example:
a = "Hello"
b = "World"
c = a + b
print(c)
#Example:
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Example:
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#Example:
price = 59
txt = f"The price is {price} dollars"
print(txt)
#Example:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Example:
txt = f"The price is {20 * 59} dollars"
print(txt)
#Example:
txt = "We are the so-called \"Vikings\" from the north."
#Exercise 1:
x = "Hello World"
print(len(x))
#Exercise 2:
txt = "Hello World"
x = txt[0]
#Exercise 3:
txt = "Hello World"
x = txt[2:5]
#Exercise 4:
txt = " Hello World "
x = txt.strip()
#Exercise 5:
txt = "Hello World"
txt = txt.upper()
#Exercise 6:
txt = "Hello World"
txt = txt.lower()
#Exercise 7:
txt = "Hello World"
txt = txt.replace('H', 'J')
#Exercise 8:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

