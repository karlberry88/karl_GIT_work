# String Tests
if 'log' in surname:
 print("Yes!")

print(surname.count('g'))

if fname.isupper():
    print("Uppercase:", fname)

if surname.startswith(" Bl"):
    print("Surname starts as expected!")

# String Formatting
print("Name is: {0} {1} {0}".format(fname, surname))
print("Name is: {1} {0}".format(fname, surname.strip()))
print("Name is: {1}, {0} {1}".format(fname, surname.strip()))
age = 43
cost = 10.5
print("Age: {0:5d} {1}".format(age, cost))
print("Age: {0:<5d} {1:.3f}".format(age, cost))
print("Age: {0:>5d} £{1:3.2f}".format(age, cost))

#String formatting planets
planets = {
    'Mercury': 57.91,
    'Venus': 108.2,
    'Earth': 149.597870,
    'Mars': 227.94
}
print(planets)
print(planets.keys())
print(planets.values())
for i, key in enumerate(planets.keys(), 1):
    print("{:2d} {:<10s} {:06.2f} Gm".format(i, key, planets[key]))
print("*"*10)
for i, key in enumerate(planets.keys(), 1):
    print("{:2d} {:>10s} {:6.1f} Gm".format(i, key, planets[key]))


# fstrings
names = ['Tom', 'Harry', 'Jane', 'Mary']
s = f"The third member is {names[2]}"
print(s)
for i, key in enumerate(planets.keys(), 1):
    print(f"{i:2d} {key:<10s} {planets[key]:06.2f} Gm")

drive = "C:"
dir = "Windows"
path = fr"{drive}\{dir}"
print(path)

#Slicing Strings
text = "Remarkable bird, the Norwegian Blue"
print(text[11:14])
print(text[-7:-1])
print(text[:14])
print(text[-7:])
print(fname[::-1].upper())

# Split and Join
words = "The quick brown fox"
print(words.split())
words = "The#quick#brown#fox"
print(words.split('#'))
print(words.split('#', maxsplit=1))
#join
print(",".join(fruit))