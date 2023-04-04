filename = "foo"
try:
    f = open(filename)
except FileNotFoundError as e:
   errmsg = filename + " not found"
   print(e)
except

print("Prog OK")
if errmsg !="":
    exit(errmsg)