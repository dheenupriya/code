sh = open("test.txt")
l = list(sh)
ls = l[0]
lst = ls.rstrip().split(' ')
print(lst)

n = len(lst)

di = dict()
for i in range(n):
    if(lst[i]=="from"):
        di[lst[i+1]] = di.get(lst[i+1],0)+1
print(di)
