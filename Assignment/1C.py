# Write a program that create a dictionary with the frequency of the 
# vowels from an inputted string. For example: input:’institute’. 
# Output:{‘i’:2,’u’:1,’e’:1}

def CV(okay):
    vowels = "aeiou"
    a = {}   
    okay = okay.lower()

    for i in okay:
        if i in vowels:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1   
    return a

okay = input("Enter a string: ")

b = CV(okay)
print(b)
