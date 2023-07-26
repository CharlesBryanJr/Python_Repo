print(" ")

print(id(1))
print(id(2))

x = 1
y = x
x += 1
print(F"X: {id(x)}, Y: {id(y)}")

print(" ")

xx = []
yy = xx
xx.append(1)
print(F"XX: {id(xx)}, YY: {id(yy)}")

print(" ")

a = 1
b = a
print(a is b)
a += 1
print(a is b)
print(F"a: {id(a)}, b: {id(b)}")

print(" ")

xxx = (1, 2, 3)
yyy = (1, 2, 3)
print(xxx is yyy)
print(F"xxx: {id(xxx)}, yyy: {id(yyy)}")

print(" ")


def randomfunction(lst, x):
    print(id(lst))
    lst.append(x)


aa = []
print(id(aa))
randomfunction(aa, 2)
randomfunction(aa, 3)
print(aa)

print(" ")


def copyList(lst):
    print(id(lst))
    lst = lst[:]
    lst.append(4)
    print(id(lst))


l = [1, 2, 3]
copyList(l)
print(id(l))


print(" ")
nestedlist = [[1, 2, 3], [1, 2, 3]]
nestedlist[0].append(4)
print(nestedlist)

print(" ")
list1 = [1, 2, 3]
d = {1: list1}
list1.append(4)
print(d)

print(" ")
a1 = [1, 2]
b1 = [3, 4]
c1 = [5, 6]
tup = (a1, b1, c1)
a1.append(0)
b1.append(0)
c1.append(0)
print(tup)

print(" ")
alist = [[1, 2, 3]]
blist = alist[:]
clist = alist
clist.append(4)

print(alist, blist, clist)
print(F"alist: {id(alist)}, blist: {id(blist)}, clist: {id(clist)}")


print(" ")

    