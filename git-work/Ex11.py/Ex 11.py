#excercise 11
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
w = len(Belgium)
x = int(Belgium[8:16])
y = int(Belgium[26:32])
z = (x + y)

# A)
print(w)
print("-" * w)
# B)
print(Belgium .replace(',', ':'))
# C)
print(x + y)
p = Belgium .split(",")
print(p)
q = int(p[1])
r = int(p[3])
print(q+r)
print(p)
print(len(p))
print(p[4])
population_of_belgium = int(p[1])
population_of_capital = int(p[3])
result = population_of_belgium + population_of_capital
print("the total is:",result)
print("the total is:" + str(result))
print("the total is: {}! which is cool" .format(result))
print(f"the total is: {result}! which is cool")