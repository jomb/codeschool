'''__author__ = 'jomb'
def reverse(word):
    x=[]
    for i in range(len(word)):
        x.append(word[i])
    return str(x)



print reverse("Pavel")'''
x="word"
def a(x):
    s=""
    for i in range(len(x)-1, -1, -1):
        s+=str(x[i])
    return s
       # print m
    #return " ," .join(m)

print a("word")