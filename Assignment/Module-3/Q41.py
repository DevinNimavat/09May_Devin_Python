'''Q42. Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). '''

A={'a':100,'b':200,'c':300}
B={'a':100,'b':200,'c':400}

C={}

D=list(A.values())
E=list(B.values())

for i in range(len(D)):
    Z=D[i] + E[i]
    for j in A:
        C[j] = Z


print(A)
print(B)
print(C)