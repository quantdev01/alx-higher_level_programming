#!/usr/bin/python3
"""
My module python inherite
"""


class MyList(list):
    """
    class MyList inherits from list
    """
    def print_sorted(self):
        """
        class method that prints the sorted list
        """
        mylist = self[:]

        k = 0
        i = 1
        j = 0

        while k < len(mylist):
            while j < len(mylist) - 1:
                if (mylist[j] > mylist[i]):
                    temp = mylist[j]
                    mylist[j] = mylist[i]
                    mylist[i] = temp
                else:
                    pass
                i += 1
                j += 1
            j = 0
            i = 1
            k += 1
        print(mylist)
