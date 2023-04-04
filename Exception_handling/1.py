import sys
try:
    f = open("foo")
except FileNotFoundError as e:
    print("could mnot open", e.filename, e.args[0], file=sys.stderr)
    print("Exception arguments", e.args, file=sys.stderr)
