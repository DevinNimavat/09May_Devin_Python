# How Do You Handle Exceptions With Try/Except/Finally In Python? 
# Explain with coding snippets.

a=10
b='20'

try:
    if a>b:
        print(f'Sum of A+B= {a+b}')
except Exception as e:
    print(e)
finally:
    print('Executed scode....')