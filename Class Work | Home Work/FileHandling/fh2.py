# using loops, counting letters, digits, and words etc..,

# f=open('sample.txt','r')

# #using loop to print lines
# for line in f:
#     print(line)    
# f.close()

#counting letters,digits, and words

f=open('sample.txt','r')

txt=f.read()

letters=sum(char.isalpha() for char in txt)

words=len(txt.split())

digits=sum(char.isdigit() for char in txt)

print("\nNumber of Letters in this file :",letters)
print("\nNumber of words in this :",words)
print("\nNumber of digits in this file :",digits)