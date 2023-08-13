import string
f=open("C:/Users/kamini/Documents/sam.txt", "r")
text = f.read()
s=text.split()
w={}
for i in s:
    if i in w:
        w[i]+=1    
    else:
        w[i]=1
print(w) 
