def problem1(l):
    for i in l:
        if (2020-i) in l:
            print(i*(2020-i))
            return
def problem2(l):
    for i in l:
        for j in l:
            if (2020-i-j) in l:
                print(i*j*(2020-i-j))
                return
def main():
    t=0
    l=[]
    a=open('input.txt','r')
    s=a.read()
    l=s.split('\n')
    l=[int(i) for i in l if i!='']
    d={}
    for i in l:
        d[i]=True
    z=int(input('Enter 1-Problem 1 , 2-Problem 2: '))
    if z==1:
        problem1(d)
    elif z==2:
        problem2(d)
main()