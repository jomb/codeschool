__author__ = 'jomb'
def censor(text, word):
    a=text.split()
    while word in a:
        number=a.index(word)
        a[number]=len(word)*"*"
    return " ".join(a)

censor("this hack is wack hack", "hack") 
censor("hey hey hey","hey")