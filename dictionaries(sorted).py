thisdict = {
    "name" : "A",
    "course" : "2"
}

mykeys = list(thisdict.keys())
mykeys.sort()
sorteddict = {i:thisdict[i] for i in mykeys}
print(sorteddict)