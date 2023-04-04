filename = "food"
try:
    f = open(filename)
except FileNotFoundError:
    errmsg = filename + " not found"
except (TypeError, ValueError):
    errmsg = "Invalid Filename"


if errmsg != "":
    exit(errmsg)