'''
Caesar encryption
Write a Python program to create a Caesar encryption.

Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

Sample output 1

Enter text: abc
Enter step: 2
cde
Sample output 2

Enter text: The quick brown fox jumps over the lazy dog.
Enter step: 2
Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi.
Sample output 3

Enter text: The quick brown fox jumps over the lazy dog.
Enter step: -1
Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf.
'''

apa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
       'o','p','q','r','s','t','u','v','w','x','y','z']

x = input("Enter text: ").split()
y = int(input("Enter step: "))
for i in x:
    for j in i:
        if j.lower() in apa:
            n = apa.index(j.lower())
            if n+y >= 26 or n+y < 0:
                h = (n+y)%26
            else:
                h = n+y
            m = apa[h]
            if j == j.upper():
                m = m.upper()
            print(m, end = "")
        else:
            print(j,end="")
    print(" ", end = "")
