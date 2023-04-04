
with open('pelican.txt') as f:
    pel = f.read().splitlines()

print(type(pel))
print(len(pel))
print(pel)


print('--'*100)
print('\n')

with open('pelican.txt') as g:
   for peli in g.read().splitlines():
    print(peli)

print(type(peli))
print(len(peli))
