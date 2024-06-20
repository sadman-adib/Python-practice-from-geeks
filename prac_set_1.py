# Program to accept the strings which contains all vowels

def accept(string):
    if len(set(string.lower()).intersection("aeiou")) >= 5:
        return ('accepted')
    else:
        return ("not accepted")
 
 

string = "aeiousadman"
print(accept(string))

    