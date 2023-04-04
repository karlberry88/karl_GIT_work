def demo_no_params():
    print("*"*25)

def make_list(val, times):
    demo_no_params()
    res = str(val) * times
    return res

my_function_value = make_list("Test", 5)
print(make_list("blah",3 ))
demo_no_params()
print(my_function_value)
demo_no_params()

def change_list(inlist,val,times):
    inlist += str(val) * times
mylist=[]
change_list(mylist, 'h',8)
print(mylist)

