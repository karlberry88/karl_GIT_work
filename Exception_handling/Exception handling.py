#filename = "foo"
#try:
   # f = open(filename)
#except FileNotFoundError as e:
  # errmsg = filename + " not found"
   #print(e)
#except

#print("Prog OK")
#if errmsg !="":
   # exit(errmsg)

filename = "foo"
# filename = 3

try:
    f = open(filename)
except FileNotFoundError as e:
    errmsg = filename + " not found"
    print(e)
    print(type(e))
except (OSError) as e:
    errmsg = "Invalid filename"
    print(e)
    print(type(e))

print("Prog OK")
if errmsg != "":
    print(f"Our error message we have handled is {errmsg}")
    exit(errmsg)