from collections import Counter
import copy

def getfirstmin(nestedlist):
    firstlist = []
    for i in range(len(nestedlist)):
        firstlist.append(nestedlist[i][0])
    count = Counter(firstlist)

    #Look at https://docs.python.org/3/library/collections.html#collections.Counter
    return count.most_common()[:-1-1:-1]

def remfromnlist(nestedlist, remove):
    #To prevent the destruction of the initial passed variable.
    #Because lists are mutable objects, we must use special ways to copy it.
    #Normally we use =old_list.copy() or =list(old_list), but these ways only make shallow copies.
    #Turn out complex objects need to use deepcopy. (In our case it's a list within a list)
    #Look at https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
    newnl = copy.deepcopy(nestedlist)
    for i in range(len(newnl)):
        newnl[i].remove(remove)
    return newnl
        

