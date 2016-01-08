import random


def biggest(lst):
    c = 0
    champ = 0
    while c < len(lst):
        if champ > lst[c]:
            c += 1
        else:
            champ = lst[c]
            c += 1
    return champ
     
     
c = 0
ls = []
while c < 6:
    ls.append(random.randint(0, 20))
    c += 1
    
print("The old list " + str(ls))
c = 0
nls = []
k = len(ls)
while c < k:
    nls.append(biggest(ls))
    ls.remove(biggest(ls))
    c += 1
print("The new list " + str(nls))
print("The biggest number is " + str(nls[0]))
