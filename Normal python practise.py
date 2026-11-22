#Code here
#Function
L=[1,2,3]
print(L.append(4))
print(L)

def g(y):
    print(x)
    print(x+1)
x=5
g(x)
print(x)

def f(y):
    x=1
    x+=1
    print(x)
    x=5
    f(x)
    print(x)

def h(y):
    x+=1
x=5
h(x)
print(x)

def f(x):
    x=x+1
    print('in f(x): =', x)
    return x
x=3
z=f(x)
print('in main program scope: z=', z)
print('in main program scope: x=', x)

def f():
    def g():
        print('inside function f')
        f()
    g()
    print('inside function f')