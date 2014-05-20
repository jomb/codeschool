__author__ = 'jomb'
def anti_vowel(text):
    s=""
    for r in range(0,len(text)):
        if text[r] in "aeiouAEIOU":
            s+=str("")
        else:
            s+=str(text[r])
    return s
    
print anti_vowel("Hey You!")