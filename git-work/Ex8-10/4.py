import getopt
import sys

first = "karl"
last = "berry"
argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "f:l:",
                                  ["first =",
                                   "last ="])
except:
    print("Error Message ")

for name, value in options:
    if name in ['-f', '--first']:
        first = value
    elif name in ['-l', '--last']:
        last = value

print(first + " " + last)