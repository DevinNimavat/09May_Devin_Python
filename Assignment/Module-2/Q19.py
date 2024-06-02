'''# Statement before changing substring

print("test","\n")

# Statement after changing substring

select_not=test.index("not")
select_poor=test.index("poor")

if select_not != -1 and select_poor != -1 or select_not < select_poor:
    result=test[:select_not] + "good" + test[select_poor + 4:]
    print(result,"\n")'''

'''def not_poor(string):
snot = string.find('not')
spoor = string.find('poor')
if spoor > snot and snot>0 and spoor>0:
    string = string.replace(string[snot:(spoor+4)], 'good')
return string
print(not_poor('The food is not that poor'))

#This will return 'The food is good'.'''