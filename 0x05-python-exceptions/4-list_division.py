#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            newlist[i] = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")

        except (TypeError, ValueError):
            newlist[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            print("Done")


    return newlist
