import sys

#def my_func(*arguments):
   # if not all(arguments):
      #  raise ValueError('False argument in my_func')
#try:
   # my_func('Tom', '', 42)
#except ValueError as err:
   # print('Oops:', err, file=sys.stderr)



try:
    f = open("foo")
except FileNotFoundError as e:
    print("Could not open", e.filename, e.args[1], file=sys.stderr)
    print("Exception arguments:", e.args, file=sys.stderr)