def checkSubset(a,b):
    for i in a:
        if i in b:
            return True
    for i in b:
        if i in a:
            return 

    return False


choice = int(input("Test Set: "))
if choice==1:
    ## set 1
    list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    list2 = [[1, 3], [13, 15, 17]]
    print(checkSubset(list1, list2))
    print(checkSubset(list2, list1))
elif choice==2:
    ## set 2
    list1 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
    list2 = [[[3, 4], [5, 6]]]
    print(checkSubset(list1, list2))
    print(checkSubset(list2, list1))
elif choice==3:
    ## set 3
    list1 = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
    list2 = [[[3, 4], [5, 6]]]
    print(checkSubset(list1, list2))
    print(checkSubset(list2, list1))