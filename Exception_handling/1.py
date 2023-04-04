import sys
try:
    f = open("food")
except FileNotFoundError as e:
    print("couldn't open", e.filename, e.args[1], file=sys.stderr)
    print("Exception arguments", e.args, file=sys.stderr)
