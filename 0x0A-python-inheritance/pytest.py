#!/usr/bin/python3

mylist = [1, 4, 3, 2]

k = 0
i = 1
j = 0
print(mylist)

while k <= len(mylist) - 1:
    print("Iteration {}".format(k))
    while j < len(mylist) - 1:
        if (mylist[j] > mylist[i]):
            temp = mylist[j]
            mylist[j] = mylist[i]
            mylist[i] = temp
        else:
            pass
        print(mylist)
        i += 1
        j += 1
    j = 0
    i = 1
    k += 1

    if (mylist == mylistcp):
        break

print(mylist)
