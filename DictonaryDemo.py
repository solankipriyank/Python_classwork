d={909:"nandini",889:"shahnavaj",654:"moin",545:"gaurav",342:"priyank"}

print(d)
print(d[654])
print(d.get(545))
print(d.items())
print(d.keys())
print(d.values())
d1={123:"jigar",345:"ashish"}
d.update(d1)
print(d)
d.pop(123)
print(d)
d.popitem()
print(d)



for i in d:
    print(i,":",d[i])
    
for i in d:
    print(d.get)
