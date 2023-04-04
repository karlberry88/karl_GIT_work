list=["He can take his beak,\n", "Enough food for a week,\n", "But im damned if i see how the helican.\n"]

with open('pelican.txt', "w") as myF:
    myF.write("A wonderfull bird is the pelican,\nHis bill holds more than his belican,\n")
    myF.writelines(list)
