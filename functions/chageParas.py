def change(n):
    n = "changed in fucntion"

def changeList(l):
    l[0]='%s has been chaged' %l[0]


# print(change('abc'))

l=[1,2,3]
print(l)
changeList(l)
print('the list has been changed')
print(l)
print("%20s" %'#')
#if don't want to change the list, one copy list could be passed in the function
l=[1,2,3]
print(l)
changeList(l[:])
print(l)

