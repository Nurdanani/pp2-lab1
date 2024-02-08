def newlist(mylist):
    uniquelist = []
    for i in range(len(mylist)):
        if mylist[i] not in uniquelist:
            uniquelist.append(mylist[i])
    print(uniquelist)

mylist = [1,1,12,2]
newlist(mylist)