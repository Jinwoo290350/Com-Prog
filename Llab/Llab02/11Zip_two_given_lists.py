## main begins here

def myzip(m,n):
    result = []
    if len(m) == len(n):
        for i in range(len(m)):
            result.append(m[i] + n[i])
        return result
    
    else:
        return result


testcase = int(input("Testcase nb: "))
if testcase==1:
    m = [[1, 3], [5, 7], [9, 11]]
    n = [[2, 4], [6, 8], [10, 12, 14]]
    res = myzip(m,n)
    print(res)
elif testcase==2:
    m = [[1, [3]], [5, 7], [9, 11]]
    n = [[[[2], 4]], [6, 8], [10, 12, 14]]
    res = myzip(m,n)
    print(res)
elif testcase==3:
    m = [[1, [3]], [5, 7], [9, 11], ['a', 'b']]
    n = [[[[2], 4]], [6, 8], [10, 12, 14], ['Hello']]
    res = myzip(m,n)
    print(res)
else:
    m = [[1, [3]], [5, 7], ['a', 'b']]
    n = [[[[2], 4]], [6, 8], [10, 12, 14], ['Hello']]
    res = myzip(m,n)
    print(res)