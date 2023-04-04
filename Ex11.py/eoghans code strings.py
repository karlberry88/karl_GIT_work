# Module 11 Strings Demo
# Bytes

euro = "\u20ac"
print(euro)

euro = "\N{euro sign}"
print(euro)

chars_as_bytes = b"single-byte string"
print(chars_as_bytes)
print(type(chars_as_bytes))

print("The answer is", 42, "always", sep=': ', end='\n')
print("The answer is", 42, "always")
print("(I think)")

print("The * will appear on a new line: \n *\n\n")
print("The ** will have a <tab> inbetween: *\t*")
# https://unicode.org/charts/charindex.html#S
print("\N{sailboat}")
print("\N{scorpion}")

print("The * will appear on THE SAME line: \\n *")
print("The * will appear on \"THE SAME\" line: \\n *")


# Concatenation
name = 'fred' 'bloggs'
print(name)
name = 'fred' \
 'bloggs'
print(name)

first = 'fred'
name = first + 'bloggs'
print(name)

fruit = ['apple', 'orange', 'banana']
s = ""
for item in fruit:
    s = s + item + "s "
print(s)
s = ""
print("s ".join(fruit))

# Quote'

# Quotes
print('hello\nworld')
print("hello\nworld")
html = """
    <tr>
        <td></td>
    </tr>
"""
print(html)
html2 = '\n\t<tr>\n\t\t<td></td>\n\t</tr>'
print(html2)

#String Methods
fname = "FRED"
print(fname)
print(fname.lower())
print(fname.swapcase())
print(fname.title())
print(fname.replace('ED','£$'))
surname = " Bloggs   "
print(fname, surname, "<--", sep='')
print(fname, surname.lstrip(),"<--", sep='')
print(fname, surname.rstrip(),"<--", sep='')
# FREDBloggs
print(fname, surname.lstrip().rstrip(),"<--", sep='')
print(fname, surname.strip(),"<--", sep='')

print(fname * 3)