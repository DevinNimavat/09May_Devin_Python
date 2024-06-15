'''Q46.Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output:
Counter ({'item1': 1150, 'item2': 300}) '''

Data=[{'item': 'item1', 'amount': 2500}, {'item': 'item2', 'amount':300}, {'item': 'item1', 'amount': 5555}]

A={}

for i in Data:
    if i['item'] not in A:
        A[i['item']]=i['amount']
    else:
        A[i['item']]+=i['amount']

print(A)